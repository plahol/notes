import os, sys


class Note(object):
    
    def __init__(self, file_name, existence):
        if existence == True:
            self.file = open(file_name + ".note", "r+")
        else:
            self.file = open(file_name + ".note", "w+")
        
    def read(self):
        self.file.seek(0)
        lines = file.readlines()
        title = lines[0]
        content = lines[1:] 
        return title, content
        
    def write(self, input):
        self.file.seek(0)
        self.file.write(input)
        self.file.flush()
        #self.file.osflush()
        
        
class Backend(object):
    
    """def __init__(self):
        self.notes = []
        #if sys.platform == "linux"
        current_working_directory = os.getcwd()
        for file in os.listdir(current_working_directory):
            if file.endswith(".note"):
                self.notes.append(Note(file, True))"""
                
    def __init__(self):
        try:
            note_order = open("note_order.note", "r+")
            lines = note_order.readlines()
            print(lines)
            self.pinned = lines[1].split()
            self.normal = lines[3].split()
        except FileNotFoundError:
            note_order = open("note_order.note", "w+")
            note_order.write("pinned_notes = \n\nnormal_notes = \n\n")         
            self.pinned = []
            self.normal = []
        
        self.pinned_notes = []
        self.normal_notes = []
        for file_name in self.pinned:
            self.pinned_notes.append(Note(file_name, True))
        for file_name in self.normal:
            self.normal_notes.append(Note(file_name, True))
            
    def save_note_order(self):
        pinned_string = " ".join(self.pinned)
        normal_string = " ".join(self.normal)
        with open("note_order.note", "r+") as note_order:
            test = "pinned notes = \n%s\nnormal_notes = \n%s" % (pinned_string, normal_string) 
            note_order.write(test)             
                                               
    def add_note(self, file_name):
        self.normal.append(file_name)
        self.normal_notes.append(Note(file_name, False))
        self.save_note_order()
                
    def remove_note(self, note_name):
        pass
        
    def change_order(self):
        pass       
        
    def read_from_note(self, note_name):
        pass    
        
    def write_to_note(self, note_name):
        pass            
                        
backend = Backend()
backend.add_note("01")
                       

                                
