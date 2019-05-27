#!/usr/bin/env python

import sys
from googletrans import Translator
# from glossary import Glossary

# glossary_path = './glossary.json'

class Translation():
    def __init__(self, src):
        self.src = src
        self.translator = Translator()
        # self.glossary = Glossary(glossary_path)

    @property
    def language(self):
        return self.translator.detect(self.src).lang

    @property
    def dest(self):
        if self.language != 'en':
            return 'en'
        else:
            return 'zh-CN'

    def translate(self):
        translation = self.translator.translate(self.src, dest=self.dest)
        # self.glossary.add(self.src, translation.text)
        print(translation.text)

if __name__ == '__main__':
    Translation(' '.join(sys.argv[1:])).translate()