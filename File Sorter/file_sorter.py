import os
import shutil
from tkinter import *
from tkinter import messagebox

# Window's settings.
root = Tk()
root.title('File Sorter')
root.geometry('320x160')

# Creates a Label Widget.
frame_a = Frame()
frame_a.pack(side=TOP)
label = Label(
    master=frame_a,
    text=" Please enter the folder path below \nExample: C:/User/username/Files/",
    height=3)
label.pack(expand=True, padx=8)

# Entry Widget.
ent_directory = Entry(root, width=50, relief=SUNKEN)
path = ent_directory.get()
ent_directory.pack(fill=X, side=TOP, padx=8, pady=15)


def sort_files():
    '''Sorts the following file types in folders:'.jpg','.png','.docx','.doc','.pdf','.xlsx','.csv','.txt'.'''
    try:
        path = ent_directory.get()
        names = os.listdir(path)
        folder_name = [
            "Images",
            "Word Documents",
            'PDF Documents',
            'Excel Files',
            'Text Documents']
        # Create folders in the selected directory.
        for x in range(0, len(folder_name)):
            if not os.path.exists(path + folder_name[x]):
                os.makedirs(path + folder_name[x])
        # Loops through the files.
        for file in names:
            if (file.endswith(".jpg") or file.endswith(".png") or file.endswith(
                    '.gif')) and not os.path.exists(path + 'Images/' + file):
                shutil.move(path + file, path + 'Images/' + file)
            if (file.endswith(".docx") or file.endswith('.doc')
                    ) and not os.path.exists(path + 'Word Documents/' + file):
                shutil.move(path + file, path + 'Word Documents/' + file)
            if file.endswith(".pdf") and not os.path.exists(
                    path + 'PDF Documents/' + file):
                shutil.move(path + file, path + 'PDF Documents/' + file)
            if (file.endswith(".xlsx") or file.endswith(".csv")
                    ) and not os.path.exists(path + 'Excel Files/' + file):
                shutil.move(path + file, path + 'Excel Files/' + file)
            if file.endswith(".txt") and not os.path.exists(
                    path + 'Text Documents/' + file):
                shutil.move(path + file, path + 'Text Documents/' + file)
        # Info message.
        messagebox.showinfo(title='Information',
                            message="Files sorted successfully!\nThank you!")
        root.quit()
    except FileNotFoundError:
        # Error message.
        messagebox.showerror(title="Error",
                             message="Please enter a valid directory")


# Button Widget
mybutton = Button(
    root,
    text="Sort",
    command=sort_files,
    width=12,
    height=2,
    bg='#A9A9A9',
    relief=RAISED)
mybutton.pack()


root.mainloop()