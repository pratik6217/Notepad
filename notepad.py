from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import *
import os

global_path = " "
global_title = ' '
save_flag = False

window = Tk()
window.title('Notepad')

scrollbar = Scrollbar(window)
editor = Text(yscrollcommand = scrollbar.set)

scrollbar.pack(side= RIGHT, fill= Y)
scrollbar.config(command= editor.yview)
editor.pack(fill= 'both', expand= True)

def Print(event = 'p'):
    if global_path == " ":
        showerror('Error', 'Please save the file before printing !!')
    else:
        os.startfile(global_path, 'print')

def run():
    if global_path == " ":
        showerror('Error', 'Please save your file first !!')
    else:
        if '.py' in global_path:
            code = editor.get('1.0', END) 
            out = exec(code)
            print(out)
            editor.insert('END', exec(code))
        else:
            showerror('Error', 'This is not a valid Python File !!')
    code = editor.get('1.0', END)
    exec(code)

def saveAs():
    global global_path
    global global_title
    save_file_path = asksaveasfilename(filetypes= [('Any File', '*.txt, *.py....')])
    with open(save_file_path, 'w') as file:
        text = editor.get('1.0', END)
        file.write(text)
    global_path = save_file_path
    window.title(save_file_path)
    global_title = save_file_path

def save(event= 's'):
    global save_flag 
    global global_title

    save_flag = True
    text = editor.get('1.0', END)
    if global_path == ' ':
        saveAs()
    else:
        with open(global_path, 'w') as file:
            file.write(text)

    window.title(global_path)
    global_title = global_path
  

def open_file(event= 'o'):
    global global_path
    global global_title
    opened_file_path = askopenfilename()
    with open(opened_file_path, 'r') as file:
        text = file.read()
    editor.delete('1.0', END)
    editor.insert('1.0', text)
    # output = Text(window)
    # output.insert('1.0', text)
    # output.pack()
    global_path = opened_file_path
    window.title(opened_file_path)
    global_title = opened_file_path
    
def new(event= 'n'):
    global global_path
    window.title('Notepad')
    editor.delete('1.0', END)
    global_path = ' '

def Exit():
    text = editor.get('1.0', END)
    print(len(text))
    if len(text) == 1:
        exit()
    elif save_flag:
        exit()
    elif global_path == ' ' and len(text) > 0:
        choice = askyesnocancel('Notepad', 'Are you sure you want to quit, Your work is not saved !!\nDo you want to save it ?')
        # print(choice)
        if choice:
            save()
            window.destroy()
            exit()
        elif choice == None:
            pass
        else:
            window.destroy()
            exit()
    else:
        choice = askyesnocancel('Notepad', 'Do you want to save your changes to ' + global_path)
        if choice:
            save()
            window.destroy()
            exit()   
        elif choice == None:
            pass
        else:
            window.destroy()
            exit()
            
    

def about():
    showinfo('About', '''    Notepad
    
    This is a simple notepad created in Tkinter - Python by Pratik Mishra.''')


menu_bar = Menu(window)

file_bar = Menu(menu_bar, tearoff= 0)
file_bar.add_command(label= 'New', command= new)
file_bar.add_command(label= 'Open...', command= open_file)
file_bar.add_command(label= 'Save', command= save)
file_bar.add_command(label= 'Save as...', command= saveAs)
file_bar.add_separator()
file_bar.add_command(label= 'Print...', command = Print)
file_bar.add_separator()
file_bar.add_command(label= 'Exit', command= Exit)

help_bar = Menu(menu_bar, tearoff= 0)
help_bar.add_command(label= 'About', command= about)

run_bar = Menu(menu_bar, tearoff= 0)
run_bar.add_command(label= 'run', command = run)

menu_bar.add_cascade(label= 'File', menu = file_bar)
menu_bar.add_cascade(label= 'Run', menu= run_bar)
menu_bar.add_cascade(label= 'Help', menu= help_bar)

window.config(menu= menu_bar)

window.bind('<Control-n>', new )
window.bind('<Control-s>', save)
window.bind('<Control-o>', open_file)

window.protocol('WM_DELETE_WINDOW', Exit)
 
window.mainloop()