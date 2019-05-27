import os
import sys 
import json
import codecs

class Glossary():
    def __init__(self, path):
        self.file_path = path

    
    def export(self):
        print(self.glossary)

    def add(self, src, translation):
        if os.path.exists(self.file_path):
            with codecs.open(self.file_path, 'r', encoding='utf-8') as json_file:  
                glossary = json.load(json_file)
        else:
            glossary = {}

        glossary[src] = translation
        with codecs.open(self.file_path, 'w', encoding='utf-8') as outfile:  
            json.dump(glossary, outfile, ensure_ascii=False)

    def remove(self):
        print("The word has been removed from the glossary")

    def import_glossary(self):
        print("The Glossary has been exported to")
