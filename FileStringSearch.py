import os
import tkinter as tk
import codecs

def map_file_system(start_dir, find_str):

    print("searching " + start_dir + " for " + find_str)
    
    filepaths = []

    for root, dirs, files in os.walk(start_dir, topdown=False):
        
        for name in files:
            filepath = os.path.join(root,name)
            if(".txt" in filepath):
                file = open(filepath)
                contents = file.read()
                if(find_str in contents):
                    filepaths.append(filepath)

    if (len(filepaths) == 0):
        filepaths.append("No matches found")

    print(filepaths)
    """
    for entry in filepaths:
        entry = entry.encode().decode('unicode_escape')
    """

    result = tk.Tk()
    label = tk.Text(result)
    label.pack()

    for entry in filepaths:
        label.insert(tk.END, entry + "\n")

    result.mainloop()

if __name__ == "__main__":

    """
    start_dir = input(r"Starting Directory: ")
    
    find_str = input("String to find: ")

    print(start_dir)

    map_file_system(start_dir, find_str)
    """

    root = tk.Tk()

    filepathlabel = tk.Label(text = "Starting Directory")
    filepathlabel.pack()
    filepathentry = tk.Entry()
    filepathentry.pack()

    stringlabel = tk.Label(text = "String to Find")
    stringlabel.pack()
    stringentry = tk.Entry()
    stringentry.pack()

    runbutton = tk.Button(root, text = "Submit", command = lambda : map_file_system(filepathentry.get(), stringentry.get()))
    runbutton.pack()

    outputlabel = tk.Label()

    root.mainloop()