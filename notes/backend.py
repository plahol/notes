class Note(object):
    
    def __init__(self, file_name, existence):
        if existence == True:
            self.file = open("file_name" + ".note", "r+")
        else:
            self.file = open("file_name" + ".note", "w+")
        
    def read(self):
        print(self.file.tell())
        lines = file.readlines()
        title = lines[0]
        content = lines[1:] 
        return title, content
        
    def write(self, input):
        self.file.write(input)
        self.file.flush()
        #self.file.osflush()
        
        
class Backend(object):
    
    def __init__(self):
        self.notes = []
                
    def add_note(self, note_name):
        self.notes.append(Note(note_name))
        
    def remove_note(self, note_name):
        pass
        
    def write_to_note(self, note_name):
        pass            
                        
test = Note("file_name")                        

                                
