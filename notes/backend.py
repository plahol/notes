import os, sys


class Note(object):
    
    def __init__(self, file_name, existence):
        if existence == True:
            self.file = open(file_name, "r+")
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
    
    def __init__(self):
        self.notes = []
        #if sys.platform == "linux"
        current_working_directory = os.getcwd()
        for file in os.listdir(current_working_directory):
            if file.endswith(".note"):
                self.notes.append(Note(file, True))
                
    def add_note(self):
        self.notes.append(Note(note_name))
        
    def remove_note(self, note_name):
        pass
        
    def read_from_note(self, note_name):
        pass    
        
    def write_to_note(self, note_name):
        pass            
                        
backend = Backend()
                       

                                
