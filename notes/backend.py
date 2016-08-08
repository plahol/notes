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
    
    """def __init__(self):
        self.notes = []
        #if sys.platform == "linux"
        current_working_directory = os.getcwd()
        for file in os.listdir(current_working_directory):
            if file.endswith(".note"):
                self.notes.append(Note(file, True))"""
                
    def __init__(self):
        try:
            note_order = open(note_order.note, "r+")
        except FileNotFoundError:
            note_order = open(note_order.note, "w+")
            note_order.write("pinned_notes = \n\nnormalnotes = \n"            
        lines = note_order.readlines()
        self.pinned = lines[1].split()
        self.normal = lines[3].split()
        
        self.pinned_notes = []
        self.normal_notes = []
        for file_name in pinned:
            self.pinned_notes.append(Note(file_name, True))
        for file_name in normal:
            self.normal_notes.append(Note(file_name, True))
            
    def save_note_order(self):
        pinned_string = " ".join(pinned)
        normal_string = " ".join(pinned)
        with note_order as open(note_order.note, "r+"):
            note_order.write("""
                pinned_notes = 
                %s
                normalnotes = 
                %s
                """ % (pinned_string, normal_string)              
                                               
    def add_note(self, file_name):
        self.notes.append(Note(file_name))
        self.normal.append(file_name)
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
                       

                                
