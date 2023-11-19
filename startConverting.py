# First it imports the input from the file, then it searches for the lines that starting with V Plus Number.
# If it can't find any line that starting with V Plus Number, error message will return.
# It inserts the line to output, and checks if there is another line after that.
# If there is, it inserts that line to output variable and checks again.
# If the line is empty or same with previous line, it skips it.
def premiereGraphTxtConvert(text):
    newText = ['']
    isSomethingChanged = False
    i = 0
    while i < len(text) - 1:
        if text[i][0] == 'V' and text[i][1].isdigit():
            isSomethingChanged = True
            i += 1
            if newText[-1] != text[i]:
                while text[i] != '\n' and text[i] != ' \n':
                    newText.append(text[i])
                    i += 1
        else:
            i += 1
    if isSomethingChanged:
        return newText
    else:
        return 0


# Same with upper function. Only difference is it searches for the lines that starts with "number plus number plus :"
def premiereSubTxtConvert(text):
    newText = ['']
    isSomethingChanged = False
    i = 1
    while i < len(text) - 1:
        if text[i][0].isdigit() and text[i][1].isdigit() and text[i][2] == ':':
            isSomethingChanged = True
            i += 1
            if newText[-1] != text[i]:
                while text[i] != '\n' and text[i] != ' \n':
                    newText.append(text[i])
                    i += 1
        else:
            i += 1
    if isSomethingChanged:
        return newText
    else:
        return 0

# GUI will start that function with the path of Input file.
# Converts the Input file into a list
# Will start the conversion for selected file type.
def StartFunc(filePath, inputType):
    # Importing txt file
    file = open(filePath, "r")
    text = file.readlines()

    # Converts premiereTxt file into newText list as text
    if inputType == 'Graph':
        convertedText = premiereGraphTxtConvert(text)
    elif inputType == 'Sub':
        convertedText = premiereSubTxtConvert(text)


    # Close the file and rewrite changes if it do not return error code.
    if convertedText != 0:
        file.close()
        file = open(filePath, "w")
        file.writelines(convertedText)
        file.close()
        return 'Success'
    else:
        return 'ErrorThatIsNotSRT'
