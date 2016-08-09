import os, sys
from textwrap import dedent

class Note(object):
    
    def __init__(self, file_name, existence):
        self.file_name = file_name  
        if existence == False:
            with open(self.file_name + ".note", "w") as file:
                file.write("\n\n")
                file.flush()        
        
    def read(self):
        with open(self.file_name + ".note", "r") as file:
            file.seek(0)
            lines = file.readlines()
            title = lines[0]
            content = "".join(lines[1:])
        return title, content
        
    def write(self, input):
        with open(self.file_name + ".note", "w") as file:
            file.write(input)
            file.flush()
            #self.file.osflush()
        
    def write_title(self, input):
        content = self.read()[1]
        self.write(input + "\n" + content)
        
    def write_content(self, input):
        title = self.read()[0]
        self.write(title + input + "\n")                    
        
    def delete(self):
        os.remove(self.file_name + ".note")        
        
        
class Backend(object):
    
    """def __init__(self):
        self.notes = []
        #if sys.platform == "linux"
        current_working_directory = os.getcwd()
        for file in os.listdir(current_working_directory):
            if file.endswith(".note"):
                self.notes.append(Note(file, True))"""
                
    def __init__(self):
        self.pinned_objects = []
        self.normal_objects = []
        try:
            with open("note_order.note", "r") as note_order:
                lines = note_order.readlines()
                self.pinned_names = lines[1].split()
                self.normal_names = lines[3].split()
                for file_name in self.pinned_names:
                    self.pinned_objects.append(Note(file_name, True))
                for file_name in self.normal_names:
                    self.normal_objects.append(Note(file_name, True))
        except FileNotFoundError:
            with open("note_order.note", "w") as note_order:
                note_order.write("pinned_names = \n\nnormal_names = \n\n")         
                self.pinned_names = []
                self.normal_names = []       
            
    def save_note_order(self):
        self.pinned_names = []
        self.normal_names = []
        for objekt in self.pinned_objects:
            self.pinned_names.append(objekt.file_name)
        for objekt in self.normal_objects:
            self.normal_names.append(objekt.file_name)
        pinned_string = " ".join(self.pinned_names)
        normal_string = " ".join(self.normal_names)
                
        with open("note_order.note", "w") as note_order:
            # see if you can get this line under 80 columns
            string = """\
                      pinned notes = 
                      %s
                      normal_notes = 
                      %s
                     """ % (pinned_string, normal_string) 
            note_order.write(dedent(string))             
                                               
    def add_note(self, pinned):
        number_of_notes = len(self.normal_objects) + len(self.pinned_objects)
        file_name = str(number_of_notes)
        if pinned == False:
            self.normal_objects.append(Note(file_name, False))
        elif pinned == True:
            self.pinned_objects.append(Note(file_name, False))
        self.save_note_order()
                
    def remove_note(self, file_name):
        position = self.normal_names.index(file_name)
        self.normal_objects[position].delete()
        del self.normal_objects[position]
        self.save_note_order()
        
    def change_order(self, file_name, new_position):
        try:
            position = self.normal_names.index(file_name)
            cache = self.normal_objects.pop(position)
            self.normal_objects.insert(new_position, cache)
        except ValueError:
            position = self.pinned_names.index(file_name)
            cache = self.pinned_objects.pop(position)
            self.pinned_objects.insert(new_position, cache)
        self.save_note_order()            
                
    def read_note(self, file_name):
        try:
            position = self.normal_names.index(file_name)
            title, content = self.normal_objects[position].read()
        except ValueError:
            position = self.pinned_names.index(file_name)
            title, content = self.pinned_objects[position].read()
        return title, content   
        
    def write_note_title(self, file_name, input):
        try:    
            position = self.normal_names.index(file_name)
            self.normal_objects[position].write_title(input)
        except ValueError:
            position = self.pinned_names.index(file_name)
            self.pinned_objects[position].write_title(input)           
        
    def write_note_content(self, file_name, input):
        try:
            position = self.normal_names.index(file_name)
            self.normal_objects[position].write_content(input)
        except ValueError:
            position = self.pinned_names.index(file_name)
            self.pinned_objects[position].write_content(input)
        
    def pin_note(self, file_name):
        # todo: check if note is already pinned
        position = self.normal_names.index(file_name)
        self.pinned_objects.append(self.normal_objects[position])
        del self.normal_objects[position]
        self.save_note_order()
        
    def unpin_note(self, file_name):
        # todo: check if note is already unpinned
        position = self.pinned_names.index(file_name)
        self.normal_objects.append(self.pinned_objects[position])
        del self.pinned_objects[position]
        self.save_note_order()
        
    def display(self):
        self.save_note_order()
        print(self.normal)
                        
"""note = Note("test", False)
print(note.read())
note.write_title("title")
print(note.read())
note.write_content("content")
print(note.read())
note.write_title("new title")
print(note.read())
note.write_content("new content\nnew content second line")
print(note.read())
note.write_content("")"""


backend = Backend()
for i in range(0, 3):
    backend.add_note(True)
    a = []
"""backend.change_order("0", 2)
backend.change_order("0", 1)
backend.change_order("1", 1)"""

#print(backend.read_note("0"))
"""backend.write_note_title("0", "newtitle")
backend.write_note_content("0", "content")
backend.write_note_title("0", "")
backend.write_note_content("0", "")
"""

backend.unpin_note("0")
backend.add_note(False)
backend.pin_note("3")
print(backend.read_note("0"))






                                
