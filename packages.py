from gtts import gTTS
import os

g=gTTS(text="hello how are you",lang="en")
g.save("welcome.mp3")
os.system("start welcome.mp3")
