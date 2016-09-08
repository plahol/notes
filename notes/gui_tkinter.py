import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# http://tcltk.free.fr/tcltkfaq.php3?idxquery=157

class Gui(object):
    
    def __init__(self):
        self.root = tk.Tk()

        self.selector = Selector(self.root)
        self.editor = Editor(self.root)
        
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.selector.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.editor.grid(row=0, column=1)
        
        self.root.mainloop()
        
    
class Selector(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(background="blue")
        
        self.toolbar()
        #card = CardFrame(self, 0)
        #card.grid(row=1, column=0)
        
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        card2 = Card(self, 0, 100, 100)
        card2.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        
        
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
        tk.Canvas.__init__(self, 
                           parent, 
                           width=width, height=height,
                           background="white")
        self.bind("<Button-1>", self.select)
        self.bind("<Configure>", self.on_resize)
        
        self.note_name = note_name
        
        self.x = tk.PhotoImage(file="button.gif")
        self.remove_note = tk.Button(self,
                                     image=self.x,
                                     width=40, height=40)
        """self.button = self.create_window((self.winfo_reqwidth(), 0), 
                                         anchor=tk.NE, 
                                         window=remove_note)"""
                                         
        self.remove_note.place(x=self.winfo_width(), 
                               y=0,
                               anchor=tk.NE)
        
        text = "This is the first line\nSecond Line\nThird Line"           
        width = self.winfo_width() - self.remove_note.cget("width")
        #for whatever reason self.cget("width") is a String
        #whereas             remove_note.cget("width") is an Int
        self.preview = self.create_text((0,0), 
                                        text=text,
                                        anchor=tk.NW,
                                        width=width)

    def select(self, event):
        if self.cget("background") == "grey":
            self.config(background="white")
        elif self.cget("background") == "white":
            self.config(background="grey")
    
    def on_resize(self, event):
        #print(self.cget("width"), self.cget("height"))
        #print(self.winfo_width(), self.winfo_height())
        
        self.remove_note.place(x=self.winfo_width(), anchor=tk.NE)
        width = self.winfo_width() - self.remove_note.cget("width")
        self.itemconfig(self.preview, width=width)
        

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
