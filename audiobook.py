#text-to-speech
import pyttsx3
#working with pdf
import PyPDF2
#filedialog => choose one file
from tkinter.filedialog import *

book = askopenfilename()
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

for num in range(0, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()  
    #converting text in audio
    player = pyttsx3.init()
    player.say(text)
    # starts the text-to-speech process and waits until the reading of the text is completed
    player.runAndWait()
    