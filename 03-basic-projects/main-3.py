from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = "my-text.txt"
with open(file_path, "rt", encoding="UTF8") as f:
    read_file = f.read()

# text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=read_file, lang="ko")
tts.save("hi.mp3")

playsound("hi.mp3")
