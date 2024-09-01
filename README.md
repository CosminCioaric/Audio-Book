# Audio-Book
A simple way to create audio books from pdf's.


pyttsx3: This is a Python library that allows text-to-speech conversion. It's used here to read out loud the text extracted from the PDF file.

PyPDF2: This library is used for working with PDF files. It can read, extract text, and manipulate pages in a PDF document.

tkinter.filedialog: This is part of the tkinter library, which is used for creating graphical user interfaces (GUIs) in Python. The filedialog module allows the user to select a file from their computer through a GUI dialog box.

askopenfilename(): This function opens a graphical dialog box that allows the user to select a file from their computer.

PdfReader(book): This command opens the selected PDF file and creates a pdfReader object, which provides access to the contents of the PDF.

len(pdfReader.pages): This calculates the total number of pages in the PDF file. Each page in the PDF is stored as an object in pdfReader.pages, and len() gives you the total count of these pages.

for num in range(0, pages):: This is a for loop that iterates over all the pages in the PDF, from the first page (0) to the last page.

page = pdfReader.pages[num]: During each iteration, this line selects the current page from the PDF based on the index num.

text = page.extract_text(): This command extracts all the text from the current page and stores it in the text variable.

player = pyttsx3.init(): This initializes the text-to-speech engine.

player.say(text): This line sends the extracted text to the text-to-speech engine, preparing it to be read out loud.

player.runAndWait(): This command starts the process of converting text to speech and waits until the reading is finished before continuing to the next page.
