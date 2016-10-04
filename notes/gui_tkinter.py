import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# http://tcltk.free.fr/tcltkfaq.php3?idxquery=157

class Gui(object):
    
    def __init__(self):
        self.root = tk.Tk()

        self.selector = Selector(self.root)
        self.editor = Editor(self.root)
        
        # with minsize set and the widgets sticking to all borders
        # the widget size doesn't actually matter
        self.root.rowconfigure(0, weight=1, minsize=300)
        self.root.columnconfigure(0, weight=2, minsize=300)
        self.root.columnconfigure(1, weight=3, minsize=500)
        self.selector.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.editor.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        self.root.mainloop()
        
    
class Selector(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        self.toolbar()
        self.cards = []
        
    def toolbar(self):
        button_add_note = tk.Button(self, text="Add Note", command=self.add_note)
        # button isn't centred until a note is added, why?
        button_add_note.grid(row=0, column=0)

    def add_note(self):
        self.cards.append(Card(self, "placeholder", 0, 0))
        index_last = len(self.cards)
        # first row is occupied by button_add_note, hence note x occupying row x + 1
        self.cards[-1].grid(row=index_last, column=0, 
                            sticky=tk.N+tk.S+tk.E+tk.W)
        self.rowconfigure(index_last, weight=1)
        self.columnconfigure(0, weight=1)

        
    def cards(self):
        pass
            
    def scrollbar(self):
        pass
    
class Editor(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.textfield()
        
    def toolbar(self):
        pass
        
    def textfield(self):
        textfield = tk.Text(self)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        textfield.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        

class Card(tk.Canvas):

    def __init__(self, parent, note_name, width, height): 
        tk.Canvas.__init__(self, 
                           parent, 
                           width=width, height=height,
                           background="white")
        self.bind("<Button-1>", self.select)
        self.bind("<Configure>", self.on_resize)
        
        self.note_name = note_name
        
        self.button_size = 30 
        self.icon_close = tk.PhotoImage(file="button.gif")
        self.remove_note = tk.Button(self,
                                     image=self.icon_close,
                                     width=self.button_size, height=self.button_size)
        
        self.pin_note = tk.Button(self,
                                  image=self.icon_close,
                                  width=self.button_size, height=self.button_size)
        self.window_remove = self.create_window((width, 0),
                                                window=self.remove_note,
                                                anchor=tk.NE)
        self.window_pin = self.create_window((width, self.button_size),
                                             window=self.pin_note,
                                             anchor=tk.NE)    
        self.preview_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        preview_width = width - self.button_size
        #for whatever reason self.cget("width") is a String
        #whereas             remove_note.cget("width") is an Int
        self.preview = self.create_text((0,0), 
                                        text=self.preview_text,
                                        anchor=tk.NW,
                                        width=preview_width)


    def select(self, event):
        if self.cget("background") == "grey":
            self.config(background="white")
        elif self.cget("background") == "white":
            self.config(background="grey")
    
    def on_resize(self, event):
        self.create_window((self.winfo_width(), 0),
                           window=self.remove_note,
                           anchor=tk.NE)
        self.create_window((self.winfo_width(), self.button_size),
                           window=self.pin_note,
                           anchor=tk.NE)
        # needs to be tested for correct preview_width
        preview_width = self.winfo_width() - 50 
        self.itemconfig(self.preview, 
                        width=preview_width)

class CardFrame(tk.Frame):

    def __init__(self, parent, note_name):
        tk.Frame.__init__(self, parent)
        self.config(background="white", borderwidth=0)
        
        
        
        self.note_name = note_name
        
        preview = tk.Text(self, 
                          width=15, height=5, 
                          relief=tk.FLAT, 
                          wrap=tk.WORD,
                          state=tk.DISABLED, 
                          background="white")
        preview.insert(tk.END, "text \n asdfjakdfj ksdjföksfjks d afjksdfs\n asfjskfjkdf")
        preview.grid(row=0, column=0)
        
        remove_note = tk.Button(self, 
                                text="x", 
                                background="white",
                                width=1, height=1,
                                relief=tk.FLAT)
        remove_note.grid(row=0, column=1, 
                         sticky=tk.N)
        

        
if __name__ == "__main__":
    gui = Gui()
