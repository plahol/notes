import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Gui(object):
    
    def __init__(self):
        self.root = tk.Tk()
        self.selector = Selector(self.root)
        self.editor = Editor(self.root)
        
        self.selector.grid(row=0, column=0)
        self.editor.grid(row=0, column=1)
        
    
class Selector(tk.Frame):
    
    def __init__(self, parent):
        self.parent = parent
        
    def toolbar(self):
        pass
        
    def textfield(self):
        pass
        
    def scrollbar(self):
        pass
    
class Editor(tk.Frame):
    
    def __init__(self, parent):
        self.parent = parent
        
    def toolbar(self):
        pass
        
    def textfield(self):
        pass