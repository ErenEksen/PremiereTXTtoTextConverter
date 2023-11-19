import tkinter as tk
from tkinter import filedialog, messagebox
import startConverting as Conversion

filePath = ''

#Things that will happen after user press the Add File button
def fileAdd():
    global filePath
    filePath = filedialog.askopenfilename(filetypes=(('Text Files', 'txt'),))
    if filePath != '':
        fileNameText.config(text=filePath.split('/')[-1], foreground='Yellow') #Last index of "/" split is the name of the file.
    else:
        fileNameText.config(text='Nothing Selected', foreground='White')

#Things that will happen after user press the Start button
def startFunc():
    global filePath
    if filePath != '':
        status = Conversion.StartFunc(filePath, selected.get())

        if status == 'Success':
            fileNameText.config( foreground='Green')
        elif status == 'ErrorThatIsNotSRT':
            fileNameText.config(foreground='Red')
            tk.messagebox.showerror("Error", "That is not a Premiere TXT subtitle file")
    else:
        tk.messagebox.showerror("Nothing Selected.", "You did not select a proper text file")



#GUI creation
root = tk.Tk()
root.title('Premiere Pro CC Subtitle Converter')
root.geometry('250x230')
root.resizable(False, False)

#Row and column configuration
root.rowconfigure(tuple(range(4)), weight=1)
root.columnconfigure(tuple(range(3)), weight=1)


#GUI Items
selected = tk.StringVar(value='Graph')
r1 = tk.Radiobutton(root, text='Graphic', value='Graph', variable=selected)
r2 = tk.Radiobutton(root, text='Subtitle', value='Sub', variable=selected)

addFileText = tk.Label( text='Select the\nSubtitle file')
addFileButton = tk.Button(root, width=15, height=2, text='Add Files', command=lambda: fileAdd())

fileNameText = tk.Label(padx=2, text='Nothing is Selected', foreground='White')

startConversionButton = tk.Button(root, width=10, height=5, text='Start', padx=10, command=lambda: startFunc())

#Place
r1.grid(row=0, column=0, sticky='w', padx=10)
r2.grid(row=0, column=2, sticky='e', padx=10)
addFileText.grid(row=1, column=0, columnspan=1)
addFileButton.grid(row=1, column=1, columnspan=2)
fileNameText.grid(row=2, column=0, columnspan=3)
startConversionButton.grid(row=3, column=0, columnspan=3, sticky='s')

#Starts the GUI
tk.mainloop()
