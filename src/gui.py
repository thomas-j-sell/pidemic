from Tkinter import *
from game import Game

width = 480
height = 320

class Gui(object):

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Pidemic")
        w = Canvas(self.tk, width=width,height=height) #self.tk)
        w.pack()
        w.create_rectangle(0,0,width/2,height/2,fill="Red")
        w.create_rectangle(0,height/2,width/2,height,fill="Yellow")
        w.create_rectangle(width/2,0,width,height/2,fill="Black")
        w.create_rectangle(width/2,height/2,width,height,fill="Blue")
        id = w.create_rectangle(140,130,340,190,fill="White")
        w.tag_bind(id, "<Button-1>", self.new_game)
        id = w.create_text(width/2,height/2,text="Pidemic",font=("Helvetica",50))
        w.tag_bind(id, "<Button-1>", self.new_game)
        self.state = False
        self.tk.bind("<Escape>", self.toggle_fullscreen)
        #self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def new_game(*args):
        print "New game"

if __name__ == '__main__':
    w = Gui(object)()
    w.tk.mainloop()
