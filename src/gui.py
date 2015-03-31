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
        self.canvas.tag_bind(id, "<Button-1>", self.epidemic)
        self.canvas.create_rectangle(0,height/2,width/2,height,fill="Yellow")
        self.canvas.create_rectangle(width/2,0,width,height/2,fill="Black")
        self.canvas.create_rectangle(width/2,height/2,width,height,fill="Blue")
        self.canvas.create_rectangle(100,130,380,190,fill="White")
        id = self.canvas.create_text(width/2,height/2,text="Start Game",font=("Helvetica",50))
        self.canvas.tag_bind(id, "<Button-1>", self.new_game)
        self.state = False
        self.tk.bind("<Escape>", self.toggle_fullscreen)

    def clear_canvas(self):
        items = self.canvas.find_all()
        for i in items:
            self.canvas.delete(i)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def new_game(self, *args):
        cards = game.newGame()
        # self.clear_canvas()
        # navigate through cards


    def epidemic(self, *args):
        card = game.epidemic()
        city = card[0]
        color = card[1]
        print "card: %s, color: %s" % (city, color)
        self.clear_canvas()

        self.canvas.create_rectangle(0,0,width,height,fill=color)
        self.canvas.create_rectangle(100,130,380,190,fill="White")
        id = self.canvas.create_text(width/2,height/2,text=city,font=("Helvetica",50))


if __name__ == '__main__':
    w = Gui()
    w.tk.mainloop()

# create methods that change UI based on game state