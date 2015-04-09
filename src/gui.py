from Tkinter import *
import sys
import game

width = 480
height = 320

class Gui(object):

  def __init__(self):
    self.tk = Tk()
    self.tk.title("Pidemic")
    self.canvas = Canvas(self.tk, width=width,height=height)
    self.canvas.pack()
    self.state = False
    self.tk.bind("<Escape>", self.toggle_fullscreen)
    self.display_start_screen()


  def clear_canvas(self):
    items = self.canvas.find_all()
    for i in items:
      self.canvas.delete(i)


  def create_text_background(self, text):
    # add padding on sides of text background
    text_box = self.canvas.bbox(text)
    x1 = text_box[0] - 10
    y1 = text_box[1]
    x2 = text_box[2] + 10
    y2 = text_box[3]
    background = self.canvas.create_rectangle(x1,y1,x2,y2,fill="White")
    # background needs to be drawn under the text
    self.canvas.tag_lower(background,text)


  def create_main_background(self):
    self.canvas.create_rectangle(0,0,width/2,height/2,fill="Red")
    self.canvas.create_rectangle(0,height/2,width/2,height,fill="Yellow")
    self.canvas.create_rectangle(width/2,0,width,height/2,fill="Black")
    self.canvas.create_rectangle(width/2,height/2,width,height,fill="Blue")


  def create_card_title(self, title):
    text = self.canvas.create_text(width/2,50,text=title,font=("Monospace",50))
    self.create_text_background(text)


  def create_continue_button(self):
    id = self.canvas.create_text(375,290,text='Continue',font=("Monospace",50))
    self.create_text_background(id)
    self.canvas.tag_bind(id, "<Button-1>", self.display_main_screen)


  def toggle_fullscreen(self, event=None):
    self.state = not self.state  # Just toggling the boolean
    self.tk.attributes("-fullscreen", self.state)
    return "break"


  def new_game(self, *args):
    cards = game.new_game()
    self.clear_canvas()
    self.display_cards(cards,0,True)


  def epidemic(self, *args):
    card = game.epidemic()
    city = card[0]
    color = card[1]
    print "card: %s, color: %s" % (city, color)
    self.clear_canvas()

    self.canvas.create_rectangle(0,0,width,height,fill=color)
    self.create_card_title(city)
    id = self.canvas.create_text(width/2,height/2,text="Place 3 cubes",font=("Monospace",50))
    self.create_text_background(id)
    self.create_continue_button()


  def infection(self,*args):
    cards = game.infect()
    self.display_cards(cards,0,True)


  def discard(self,*args):
    cards = game.discard_pile()
    if len(cards) > 0:
      self.display_cards(cards,0,False)
    else:
      self.display_main_screen()


  def troubleshoot(self,*args):
    cards = game.troubleshoot()
    self.display_cards(cards,0,False)


  def display_cards(self, cards, current_card, show_cube_text):
    # print "displaying card number %d" % current_card
    if len(cards) > 0:
      card = cards[current_card]
      city = card[0]
      color = card[1]

    self.clear_canvas()
    self.canvas.create_rectangle(0,0,width,height,fill=color)
    self.create_card_title(city)

    if show_cube_text:
      # len(cards) == 9 is the initiaL setup, len(cards) <= 4 is an infection event
      if current_card <= 2 and len(cards) == 9:
        id = self.canvas.create_text(width/2,height/2,text="Place 3 cubes",font=("Monospace",50))
        self.create_text_background(id)
      elif current_card <= 5 and len(cards) == 9:
        id = self.canvas.create_text(width/2,height/2,text="Place 2 cubes",font=("Monospace",50))
        self.create_text_background(id)
      elif current_card <= 8 or len(cards) <= 4:
        id = self.canvas.create_text(width/2,height/2,text="Place 1 cube",font=("Monospace",50))
        self.create_text_background(id)

    if current_card < len(cards) - 1:
      id = self.canvas.create_text(420,290,text='Next',font=("Monospace",50))
      self.create_text_background(id)
      self.canvas.tag_bind(id, "<Button-1>", lambda x: self.display_cards(cards,current_card+1,show_cube_text))
    else:
      self.create_continue_button()

    if current_card > 0:
      id = self.canvas.create_text(60,290,text='Prev',font=("Monospace",50))
      self.create_text_background(id)
      self.canvas.tag_bind(id, "<Button-1>", lambda x: self.display_cards(cards,current_card-1,show_cube_text))


  def display_start_screen(self,*args):
    self.create_main_background()
    id = self.canvas.create_text(width/2,height/4,text="New Game",font=("Monospace",60))
    self.create_text_background(id)
    self.canvas.tag_bind(id, "<Button-1>", self.new_game)

    id = self.canvas.create_text(width/2,height/4*3,text="Quit",font=("Monospace",60))
    self.create_text_background(id)
    self.canvas.tag_bind(id, "<Button-1>", sys.exit)


  def display_main_screen(self, *args):
    self.clear_canvas()
    self.create_main_background()

    id = self.canvas.create_text(40,20,text="End",font=("Monospace",30))
    self.create_text_background(id)
    self.canvas.tag_bind(id,"<Button-1>", self.display_start_screen)

    id = self.canvas.create_text(430,20,text="Event",font=("Monospace",30))
    self.create_text_background(id)
    self.canvas.tag_bind(id,"<Button-1>", self.display_event_screen)

    id = self.canvas.create_text(width/2,50,text="Discard",font=("Monospace",50))
    self.create_text_background(id)
    self.canvas.tag_bind(id, "<Button-1>", self.discard)

    id = self.canvas.create_text(width/2,height/2,text="Infect",font=("Monospace",50))
    self.create_text_background(id)
    self.canvas.tag_bind(id, "<Button-1>", self.infection)

    # rate = game.infection_rate()
    # id = self.canvas.create_text(450,height/2,text=rate,font=("Monospace",50))
    # self.create_text_background(id)

    id = self.canvas.create_text(width/2,270,text="Epidemic",font=("Monospace",50))
    self.create_text_background(id)
    self.canvas.tag_bind(id, "<Button-1>", self.epidemic)


  def display_event_screen(self,*args):
    self.create_main_background()

    id = self.canvas.create_text(40,20,text="Back",font=("Monospace",30))
    self.create_text_background(id)
    self.canvas.tag_bind(id,"<Button-1>", self.display_main_screen)

    id = self.canvas.create_text(width/2,70,text="Troubleshooter (character)",font=("Monospace",30))
    self.create_text_background(id)
    self.canvas.tag_bind(id, "<Button-1>", self.troubleshoot)

    id = self.canvas.create_text(width/2,120,text="Forecast (event)",font=("Monospace",30))
    self.create_text_background(id)
    # self.canvas.tag_bind(id, "<Button-1>", sys.exit)

    id = self.canvas.create_text(width/2,170,text="Resilient Population (event)",font=("Monospace",30))
    self.create_text_background(id)
    # self.canvas.tag_bind(id, "<Button-1>", sys.exit)

    id = self.canvas.create_text(width/2,220,text="Commercial Travel Ban (event)",font=("Monospace",30))
    self.create_text_background(id)
    # self.canvas.tag_bind(id, "<Button-1>", sys.exit)


if __name__ == '__main__':
  w = Gui()
  w.tk.mainloop()
