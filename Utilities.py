import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler  
import importlib
import SentimentAnalysis

import math, re, string, requests, json
from itertools import product
from inspect import getsourcefile
from os.path import abspath, join, dirname


class FileChangeEventHandler(PatternMatchingEventHandler):
    patterns = ["*.txt"]

    def process(self,event):
         msg = "{} {}".format(event.src_path, event.event_type)  # print now only for debug
         try:
           importlib.reload(SentimentAnalysis)
           print('re-loaded successfully!')
         except Exception as inst: 
            print ("Error:{} ".format(inst))                 

    def on_modified(self, event):
        self.process(event)


path = "./vaderSentiment"
observer = Observer()
observer.schedule(FileChangeEventHandler(), path, recursive=True)
observer.start()

def loadlexicon():
  _this_module_file_path_ = abspath(getsourcefile(lambda:0))
  lexicon_file = "vader_lexicon.txt"
  lexicon_full_filepath = join(join(dirname(_this_module_file_path_),'vaderSentiment'), lexicon_file)
  print("path",lexicon_full_filepath)
  lex_dict = {}  
  startEdiable = False
  with open(lexicon_full_filepath) as f:
      for line in f.read().split('\n'):            
            if len(line.strip()) > 0:                                
                if not line.startswith("#"):                                        
                    (word, measure) = line.strip().split('\t')[0:2]
                    if startEdiable:
                      lex_dict [word] = float(measure)     
                else:
                    if line.startswith("#Editable"):
                          startEdiable = True
  return lex_dict
