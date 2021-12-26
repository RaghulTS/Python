from tkinter import *
root = Tk()
root.title("Convert Your Mark!")

def operation1():
    global total_mark_test_entry
    global how_much_conversion_entry
    # getting input from the user the total mark they written
    total_mark_test_entry = Entry(root)
    total_mark_test_entry.grid(row = 1, column = 1)

    # input from the user how much they need to convert
    how_much_conversion_entry = Entry(root)
    how_much_conversion_entry.grid(row = 2, column = 1)

operation1()

def final_function():

    # Topic of the app
    heading_application = Label(root, text = "Convert Mark From One To Another!", bg = "black", fg = "white")
    heading_application.grid(row = 0, column = 0)

    # labeling the total test mark
    total_mark_test = Label(root, text = "Total Mark")
    total_mark_test.grid(row = 1, column = 0)

    # labeling the conversion mark
    how_much_conversion = Label(root, text = "How Much Do You\nWant to Convert")
    how_much_conversion.grid(row = 2, column = 0)

    # heading subject
    subjectText = Label(root, text = "Subject", fg = "red")
    subjectText.grid(row = 3, column = 0)

    # heading mark entry
    marks_entryText = Label(root, text = "Enter Your Mark Here", fg = "red")
    marks_entryText.grid(row = 3, column = 1)

    # labeling the subjects
    subEnglish = Label(root, text = "English")
    subEnglish.grid(row = 4, column = 0)

    subFrench = Label(root, text = "Tamil/French")
    subFrench.grid(row = 5, column = 0,)

    subMath = Label(root, text = "Mathematics")
    subMath.grid(row = 6, column = 0)

    subCsc = Label(root, text = "Computer Science")
    subCsc.grid(row = 7, column = 0)

    subPhysics = Label(root, text = "Physics")
    subPhysics.grid(row = 8, column = 0)

    subChemistry = Label(root, text = "Chemistry")
    subChemistry.grid(row = 9, column = 0)


    # creating entry to make input the user
    entryEng = Entry(root)
    entryEng.grid(row = 4, column = 1)

    entrytam = Entry(root)
    entrytam.grid(row = 5, column = 1)

    entrymath = Entry(root)
    entrymath.grid(row = 6, column = 1)

    entrycsc = Entry(root)
    entrycsc.grid(row = 7, column = 1)

    entryphy = Entry(root)
    entryphy.grid(row = 8, column = 1)

    entrychem = Entry(root)
    entrychem.grid(row = 9, column = 1)

    def Operation():# operation for the next button 

        global labelFinal1
        global labelFinal2
        global labelFinal3
        global labelFinal4
        global labelFinal5
        global labelFinal6
        global labelTotalMarks
        global labelFinalMark
        global mylab1
        global mylab2
        global mylab3
        global mylab4
        global mylab5
        global mylab6
        global mylab7

        
        gettingEntryTotalMark = total_mark_test_entry.get()
        gettingEntryConversion = how_much_conversion_entry.get()

        gettingEntryEng = entryEng.get()
        gettingEntryTam = entrytam.get()
        gettingEntryMath = entrymath.get()
        gettingEntryCsc = entrycsc.get()
        gettingEntryPhy = entryphy.get()
        gettingEntrychem = entrychem.get()

        final_ans1 = (float(gettingEntryEng) / float(gettingEntryTotalMark)) * float(gettingEntryConversion)
        final_ans2 = (float(gettingEntryTam) / float(gettingEntryTotalMark)) * float(gettingEntryConversion)
        final_ans3 = (float(gettingEntryMath) / float(gettingEntryTotalMark)) * float(gettingEntryConversion)
        final_ans4 = (float(gettingEntryCsc) / float(gettingEntryTotalMark)) * float(gettingEntryConversion)
        final_ans5 = (float(gettingEntryPhy) / float(gettingEntryTotalMark)) * float(gettingEntryConversion)
        final_ans6 = (float(gettingEntrychem) / float(gettingEntryTotalMark)) * float(gettingEntryConversion)

        totalMarksObtained = final_ans1 + final_ans2 + final_ans3 + final_ans4 + final_ans5 + final_ans6

        labelFinal1 = Label(root, text = final_ans1)
        labelFinal1.grid(row = 4, column = 2)
        labelFinal2 = Label(root, text = final_ans2)
        labelFinal2.grid(row = 5, column = 2)
        labelFinal3 = Label(root, text = final_ans3)
        labelFinal3.grid(row = 6, column = 2)
        labelFinal4 = Label(root, text = final_ans4)
        labelFinal4.grid(row = 7, column = 2)
        labelFinal5 = Label(root, text = final_ans5)
        labelFinal5.grid(row = 8, column = 2)
        labelFinal6 = Label(root, text = final_ans6)
        labelFinal6.grid(row = 9, column = 2)

        label_total = Label(root, text = "Total")
        label_total.grid(row = 10, column = 1)

        labelTotalMarks = Label(root, text = totalMarksObtained)
        labelTotalMarks.grid(row = 10, column = 2)

        labelFinalMark = Label(root, text = "Your Final\nMark", fg = "red")
        labelFinalMark.grid(row = 3, column = 2)

        nextButton = Button(root, text = "Next", state = DISABLED, fg = "green")
        nextButton.grid(row = 10, column = 0)

        mylab1 = Label(root, text = "/ " + str(gettingEntryConversion))
        mylab1.grid(row = 4, column = 3)

        mylab2 = Label(root, text = "/ " + str(gettingEntryConversion))
        mylab2.grid(row = 5, column = 3)
    
        mylab3 = Label(root, text = "/ " + str(gettingEntryConversion))
        mylab3.grid(row = 6, column = 3)
    
        mylab4 = Label(root, text = "/ " + str(gettingEntryConversion))
        mylab4.grid(row = 7, column = 3)

        mylab5 = Label(root, text = "/ " + str(gettingEntryConversion))
        mylab5.grid(row = 8, column = 3)

        mylab6 = Label(root, text = "/ " + str(gettingEntryConversion))
        mylab6.grid(row = 9, column = 3)

        totalMult = float(gettingEntryConversion) * 6
        mylab7 = Label(root, text = "/ " + str(totalMult))
        mylab7.grid(row = 10, column = 3)

    nextButton = Button(root, text = "Next", command = Operation, fg = "green")
    nextButton.grid(row = 10, column = 0)

final_function()

def operation2():
    labelFinal1.destroy()
    labelFinal2.destroy()
    labelFinal3.destroy()
    labelFinal4.destroy()
    labelFinal5.destroy()
    labelFinal6.destroy()
    labelTotalMarks.destroy()
    labelFinalMark.destroy()
    mylab1.destroy()
    mylab2.destroy()
    mylab3.destroy()
    mylab4.destroy()
    mylab5.destroy()
    mylab6.destroy()
    mylab7.destroy()
    final_function()

def operation3():
    operation1()


newFormBtton1 = Button(root, text = "NewForm", command = operation2)
newFormBtton1.grid(row = 11, column = 0)

newFormBtton2 = Button(root, text = "NewForm", command = operation3)
newFormBtton2.grid(row = 1, column = 2)

root.mainloop()


