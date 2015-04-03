from Tkinter import *
import game

width = 480
height = 320

class Gui(object):

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Pidemic")
        self.canvas = Canvas(self.tk, width=width,height=height)
        self.canvas.pack()
        id = self.canvas.create_rectangle(0,0,width/2,height/2,fill="Red")
        # self.canvas.tag_bind(id, "<Button-1>", self.epidemic)
        self.canvas.create_rectangle(0,height/2,width/2,height,fill="Yellow")
        self.canvas.create_rectangle(width/2,0,width,height/2,fill="Black")
        self.canvas.create_rectangle(width/2,height/2,width,height,fill="Blue")
        id = self.canvas.create_text(width/2,height/2,text="Start Game",font=("Helvetica",50))
        self.create_text_background(id)
        self.canvas.tag_bind(id, "<Button-1>", self.new_game)
        self.state = False
        self.tk.bind("<Escape>", self.toggle_fullscreen)

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

    def create_card_title(self, title):
        text = self.canvas.create_text(width/2,50,text=title,font=("Monospace",50))
        self.create_text_background(text)
        
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def new_game(self, *args):
        cards = game.new_game()
        self.clear_canvas()
        self.display_cards(cards,0)
        # navigate through cards

    def epidemic(self, *args):
        card = game.epidemic()
        city = card[0]
        color = card[1]
        print "card: %s, color: %s" % (city, color)
        self.clear_canvas()

        self.canvas.create_rectangle(0,0,width,height,fill=color)
        self.canvas.create_rectangle(100,130,380,190,fill="White")
        id = self.canvas.create_text(width/2,height/2,text=city,font=("Monospace",50))

    def display_cards(self, cards, current_card):
        print "displaying card number %d", current_card
        card = cards[current_card]
        city = card[0]
        color = card[1]

        self.clear_canvas()
        self.canvas.create_rectangle(0,0,width,height,fill=color)
        self.create_card_title(city)

        if current_card <= 2:
            id = self.canvas.create_text(width/2,height/2,text="Place 3 cubes",font=("Monospace",50))
            self.create_text_background(id)
        elif current_card <= 5:
            id = self.canvas.create_text(width/2,height/2,text="Place 2 cubes",font=("Monospace",50))
            self.create_text_background(id)
        elif current_card <= 8:
            id = self.canvas.create_text(width/2,height/2,text="Place 1 cube",font=("Monospace",50))
            self.create_text_background(id)

        if current_card < len(cards) - 1:
            id = self.canvas.create_text(420,290,text='next',font=("Monospace",50))
            self.create_text_background(id)
            self.canvas.tag_bind(id, "<Button-1>", lambda x: self.display_cards(cards,current_card+1))
        else:
            print "done"

        if current_card > 0:
            id = self.canvas.create_text(60,290,text='prev',font=("Monospace",50))
            self.create_text_background(id)
            self.canvas.tag_bind(id, "<Button-1>", lambda x: self.display_cards(cards,current_card-1))



if __name__ == '__main__':
    w = Gui()
    w.tk.mainloop()

# create methods that change UI based on game state