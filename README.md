When you want to export the subtitles you made on Adobe Premiere Pro as TXT, the file that gives you is not a normal text file. To avoid this, you can use this program.
Also this program will delete blank and duplicated lines.
![pwemiewe](https://github.com/ErenEksen/PremiereTXTtoTextConverter/assets/97560144/eba5cb43-b372-4641-a6a8-8793eba8c562)
![Application](https://github.com/ErenEksen/PremiereTXTtoTextConverter/assets/97560144/758e95c3-2351-472d-be38-d6c95f4a4b93)
![BeforeAfter](https://github.com/ErenEksen/PremiereTXTtoTextConverter/assets/97560144/c7e2f2a6-86a4-401a-8922-3a93ca5e1ae4)



## 🔨 To Compile it Yourself
```
pip install pyinstaller
pip install pytk

pyinstaller main.py --onefile  --windowed --icon=pwemiere.ico
#or
pyinstaller main.py --onefile  --windowed --icon=pwemiere.icns
```
Dependencies to compile:
- Python 3 or above
- pyinstaller 
- TKinter ("pytk" pip package)




