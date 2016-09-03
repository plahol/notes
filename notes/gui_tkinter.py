import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Gui(object):
    
    def __init__(self):
        self.root = tk.Tk()
        self.selector = Selector(self.root)
        self.editor = Editor(self.root)
        
        self.selector.grid(row=0, column=0)
        self.editor.grid(row=0, column=1)
        
        self.root.mainloop()
        
    
class Selector(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        self.toolbar()
        card = CardFrame(self, 0)
        card.grid(row=1, column=0)
        
        card2 = Card(self, 0, 100, 100)
        card2.grid(row=2, column=0)
        
        
    def toolbar(self):
        add_note = tk.Button(self, text="Add Note")
        add_note.grid(row=0, column=0)
        
    def cards(self):
        pass
            
    def scrollbar(self):
        pass
    
class Editor(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
    def toolbar(self):
        pass
        
    def textfield(self):
        pass
        
class Card(tk.Canvas):

    def __init__(self, parent, note_name, width, height):
        tk.Canvas.__init__(self, parent, width=width, height=height)
        self.config(background="white")
        self.bind("<Button-1>", self.select)
        
        self.note_name = note_name
        
        remove_note = tk.Button(self, text="x")
        self.create_window((width, 0), anchor=tk.NE, window=remove_note)
        
        self.create_text((0,0), text="Canvas Card\nSecond Line", anchor=tk.NW)
        
    def select(self, event):
        if self.cget("background") == "grey":
            self.config(background="white")
        elif self.cget("background") == "white":
            self.config(background="grey")
        
        
class CardFrame(tk.Frame):

    def __init__(self, parent, note_name):
        tk.Frame.__init__(self, parent)
        
        self.note_name = note_name
        
        preview = tk.Text(self, width=10, height=2)
        preview.insert(tk.END, "text")
        preview.config(state=tk.DISABLED)
        
        preview.grid(row=0, column=0)
        
        remove_note = tk.Button(self, text="x")
        remove_note.grid(row=0, column=1, sticky=tk.N)
        
        
        
if __name__ == "__main__":
    gui = Gui()
