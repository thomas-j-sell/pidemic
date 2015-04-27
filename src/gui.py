from Tkinter import *
import sys
import platform
import game

width = 480
height = 320
is_epidemic = False

class Gui(object):

  def __init__(self):
    self.tk = Tk()
    self.tk.title("Pidemic")
    if platform.system() == 'Linux':
      self.canvas = Canvas(self.tk, width=width,height=height, cursor="none")
      self.tk.attributes("-fullscreen", True)
    else:
      self.canvas = Canvas(self.tk, width=width,height=height)
    self.canvas.pack()
    self.state = False
    self.tk.bind("<Escape>", self.toggle_fullscreen)
    self.display_start_screen()


  def clear_canvas(self):
    items = self.canvas.find_all()
    for i in items:
      self.canvas.delete(i)


  def create_text_background(self, text, color):
    # add padding on sides of text background
    text_box = self.canvas.bbox(text)
    x1 = text_box[0] - 10
    y1 = text_box[1]
    x2 = text_box[2] + 10
    y2 = text_box[3]
    background = self.canvas.create_rectangle(x1,y1,x2,y2,fill=color)
    # background needs to be drawn under the text
    self.canvas.tag_lower(background,text)


  def create_main_background(self):
    self.canvas.create_rectangle(0,0,width/2,height/2,fill="Red")
    self.canvas.create_rectangle(0,height/2,width/2,height,fill="Yellow")
    self.canvas.create_rectangle(width/2,0,width,height/2,fill="Black")
    self.canvas.create_rectangle(width/2,height/2,width,height,fill="Blue")


  def create_card_title(self, title):
    text = self.canvas.create_text(width/2,50,text=title,font=("Monospace",50))
    self.create_text_background(text,"White")


  def create_continue_button(self):
    id = self.canvas.create_text(375,290,text='Continue',font=("Monospace",50))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id, "<Button-1>", self.display_main_screen)


  def toggle_fullscreen(self, event=None):
    self.state = not self.state  # Just toggling the boolean
    self.tk.attributes("-fullscreen", self.state)
    return "break"


  def new_game(self, *args):
    cards = game.new_game()
    self.clear_canvas()
    self.display_cards(cards,0,True,False)


  def epidemic_draw(self, *args):
    global is_epidemic
    card = game.epidemic_draw()
    city = card[0]
    color = card[1]
    self.clear_canvas()

    self.canvas.create_rectangle(0,0,width,height,fill=color)
    self.create_card_title(city)
    id = self.canvas.create_text(width/2,height/2,text="Place 3 cubes",font=("Monospace",50))
    self.create_text_background(id,"White")

    id = self.canvas.create_text(375,290,text='Continue',font=("Monospace",50))
    self.create_text_background(id,"White")
    is_epidemic = True
    self.canvas.tag_bind(id, "<Button-1>", self.display_main_screen)


  def epidemic_shuffle(self, *args):
    global is_epidemic
    game.epidemic_shuffle()
    is_epidemic = False
    self.display_main_screen()


  def infection(self,*args):
    cards = game.infect()
    self.display_cards(cards,0,True,False)


  def show_discard_pile(self,*args):
    cards = game.discard_pile()
    if len(cards) > 0:
      self.display_cards(cards,0,False,False)
    else:
      self.display_main_screen()


  def troubleshoot(self,*args):
    cards = game.troubleshoot()
    self.display_cards(cards,0,False,False)


  def display_cards(self, cards, current_card, show_cube_text, show_removal_button):
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
        self.create_text_background(id,"White")
      elif current_card <= 5 and len(cards) == 9:
        id = self.canvas.create_text(width/2,height/2,text="Place 2 cubes",font=("Monospace",50))
        self.create_text_background(id,"White")
      elif current_card <= 8 or len(cards) <= 4:
        id = self.canvas.create_text(width/2,height/2,text="Place 1 cube",font=("Monospace",50))
        self.create_text_background(id,"White")
    elif show_removal_button:
      id = self.canvas.create_text(width/2,height/2,text="Remove",font=("Monospace",50))
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", lambda x: self.remove_card(card))

    if current_card < len(cards) - 1:
      id = self.canvas.create_text(420,290,text='Next',font=("Monospace",50))
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", lambda x: self.display_cards(cards,current_card+1,show_cube_text,show_removal_button))
    else:
      self.create_continue_button()

    if current_card > 0:
      id = self.canvas.create_text(60,290,text='Prev',font=("Monospace",50))
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", lambda x: self.display_cards(cards,current_card-1,show_cube_text,show_removal_button))


  def display_start_screen(self, *args):
    self.create_main_background()
    id = self.canvas.create_text(width/2,height/4,text="New Game",font=("Monospace",60))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id, "<Button-1>", self.new_game)

    id = self.canvas.create_text(width/2,height/4*3,text="Quit",font=("Monospace",60))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id, "<Button-1>", sys.exit)


  def display_main_screen(self, *args):
    global is_epidemic
    self.clear_canvas()
    self.create_main_background()

    id = self.canvas.create_text(40,20,text="End",font=("Monospace",30))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id,"<Button-1>", self.display_start_screen)

    id = self.canvas.create_text(430,20,text="Event",font=("Monospace",30))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id,"<Button-1>", self.display_event_screen)

    id = self.canvas.create_text(width/2,50,text="Discard",font=("Monospace",50))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id, "<Button-1>", self.show_discard_pile)

    id = self.canvas.create_text(width/2,height/2,text="Infect",font=("Monospace",50))
    if is_epidemic:
      self.create_text_background(id,"Grey")
    else:
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", self.infection)

    rate = game.infection_rate()
    will_change = game.infection_rate_will_change()
    if will_change:
      id = self.canvas.create_text(450,height/2,text="%d+" % rate,font=("Monospace",50))
    else:
      id = self.canvas.create_text(450,height/2,text=rate,font=("Monospace",50))
    self.create_text_background(id,"White")

    id = self.canvas.create_text(width/4,260,text="Epidemic\nDraw",font=("Monospace",50))
    if is_epidemic:
      self.create_text_background(id,"Grey")
    else:
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", self.epidemic_draw)

    id = self.canvas.create_text(width/4*3,260,text="Epidemic\nShuffle",font=("Monospace",50))
    if is_epidemic:
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", self.epidemic_shuffle)
    else:
      self.create_text_background(id,"Grey")


  def display_event_screen(self,*args):
    self.clear_canvas()
    self.create_main_background()

    id = self.canvas.create_text(40,20,text="Back",font=("Monospace",30))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id,"<Button-1>", self.display_main_screen)

    id = self.canvas.create_text(width/2,70,text="Troubleshooter (character)",font=("Monospace",30))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id, "<Button-1>", self.troubleshoot)

    id = self.canvas.create_text(width/2,120,text="Forecast (event)",font=("Monospace",30))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id, "<Button-1>", self.forecast)

    id = self.canvas.create_text(width/2,170,text="Resilient Population (event)",font=("Monospace",30))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id, "<Button-1>", self.resilient_population)

    id = self.canvas.create_text(width/2,220,text="Commercial Travel Ban (event)",font=("Monospace",30))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id, "<Button-1>", self.toggle_travel_ban)


  def toggle_travel_ban(self, *args):
    game.toggle_travel_ban()
    self.display_main_screen()


  def resilient_population(self,*arbs):
    cards = game.discard_pile()
    if len(cards) > 0:
      self.display_cards(cards,0,False,True)
    else:
      self.display_main_screen()


  def remove_card(self,card):
    game.remove_card(card)
    self.display_main_screen()


  def display_forecast(self,cards,position):
    if position > 6:
      position = 1

    self.clear_canvas()
    self.create_main_background()

    id = self.canvas.create_text(50,20,text='Done',font=("Monospace",40))
    self.create_text_background(id,"White")
    self.canvas.tag_bind(id, "<Button-1>", lambda x: self.forecast_append(cards))

    id = self.canvas.create_text(width/2,40,text="Forecast",font=("Monospace",50))
    self.create_text_background(id,"White")

    id = self.canvas.create_text(450,20,text=position,font=("Monospace",40))
    self.create_text_background(id,"White")

    id = self.canvas.create_text(width/2,90,text=cards[0][0],font=("Monospace",30))
    if position < 2:
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", lambda f: self.forecast_rearrange(cards,cards[0],position))
    else:
      self.create_text_background(id,"Grey")
    id = self.canvas.create_text(width/2,130,text=cards[1][0],font=("Monospace",30))
    if position < 3:
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", lambda x: self.forecast_rearrange(cards,cards[1],position))
    else:
      self.create_text_background(id,"Grey")
    id = self.canvas.create_text(width/2,170,text=cards[2][0],font=("Monospace",30))
    if position < 4:
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", lambda x: self.forecast_rearrange(cards,cards[2],position))
    else:
      self.create_text_background(id,"Grey")
    id = self.canvas.create_text(width/2,210,text=cards[3][0],font=("Monospace",30))
    if position < 5:
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", lambda x: self.forecast_rearrange(cards,cards[3],position))
    else:
      self.create_text_background(id,"Grey")
    id = self.canvas.create_text(width/2,250,text=cards[4][0],font=("Monospace",30))
    if position < 6:
      self.create_text_background(id,"White")
      self.canvas.tag_bind(id, "<Button-1>", lambda x: self.forecast_rearrange(cards,cards[4],position))
    else:
      self.create_text_background(id,"Grey")
    id = self.canvas.create_text(width/2,290,text=cards[5][0],font=("Monospace",30))
    self.create_text_background(id,"White")
    # if position < 4:
    self.canvas.tag_bind(id, "<Button-1>", lambda x: self.forecast_rearrange(cards,cards[5],position))


  def forecast(self,*args):
    cards = game.forecast_pop()
    self.display_forecast(cards,1)


  def forecast_rearrange(self,cards,placement_card,position):
    place_index = position - 1

    new_cards = cards[0:place_index]
    new_cards.append(placement_card)
    for card in new_cards:
      cards.remove(card)

    for card in cards:
      new_cards.append(card)
    
    self.display_forecast(new_cards, position+1)


  def forecast_append(self,cards):
    game.forecast_append(cards)
    self.display_main_screen()

if __name__ == '__main__':
  w = Gui()
  w.tk.mainloop()
