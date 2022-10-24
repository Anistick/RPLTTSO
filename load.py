import re # Regular Expressions
import threading # Threading
import pygame # The sound starter thingy majingy
import time # Time.sleep for delaying in spaces
import wave # wave
import uuid # rand
import string
pygame.init() # Init
pygame.mixer.init() # Init
class TextToSpeech: # Main Class

    def __init__(self, words_pron_dict:str='cmudict-0.7b.txt'):
        self._l = {}
        self._fml = []
        self._load_words(words_pron_dict)

    def _load_words(self, words_pron_dict:str):
        with open(words_pron_dict, 'r') as file:
            for line in file:
                if not line.startswith(';;;'):
                    key, val = line.split('  ',2)
                    self._l[key] = re.findall(r"[A-Z]+",val)

    def get_pronunciation(self, str_input):
        list_pron = []
        for word in re.findall(r"[\w']+",str_input.upper()):
            if word in self._l:
                list_pron += self._l[word]
        print(list_pron)
        delay=0
        for pron in list_pron:
            
            threading.Thread(target=self._play_audio, args=(pron,delay,)).start()
            delay += 0.145
            
        for i in list_pron:
            i = f"sounds/{i}.wav"
            self._fml.append(i)
        try:
            of = "output/"+str(uuid.uuid4())+".wav"
            ofd = []
            for x in self._fml:
                xi = wave.open(x,'rb')
                ofd.append([xi.getparams(),xi.readframes(xi.getnframes())])
                xi.close()
            op = wave.open(of,'wb')
            op.setparams(ofd[0][0])
            for xix in range(len(ofd)):
                op.writeframes(ofd[xix][1])
            op.close()
            print(f"Output File: {of}")
            self._fml = []
        except:
            import traceback; traceback.print_exc()
		
            
    
    def _play_audio(self, sound, delay):
        try:
            time.sleep(delay)
            prefix = "sounds/"
            suffix = ".wav"
            s = pygame.mixer.Sound(f"{prefix}{sound}{suffix}")
            s.play()
            return
        except:
            pass
    
 
 

if __name__ == '__main__':
    tts = TextToSpeech()
    while True:
        try:
            tts.get_pronunciation(input('Enter a word or phrase: '))
        except:
            exit()