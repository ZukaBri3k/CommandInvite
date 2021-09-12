import tkinter as tk
import commands

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.root.geometry('400x500')
        self.root.config(bg='black')
        self.root.title("Command invite by ZukaBriek")
        self.root.resizable(0,0)
        self.create_widget()
        self.listbox.pack(side='top', fill='y')
        self.frame.pack(side='bottom')
        self.label.pack(side='left', fill='y')
        self.entry.pack(side='right')
        self.root.bind('<Return>', self.add_listbox)

    def create_widget(self):
        self.listbox = tk.Listbox(self.root, width=66, height=30, bg='black', fg='green', highlightthickness=0)
        self.frame = tk.Frame(self.root)
        self.label = tk.Label(self.frame, text='>>>', fg='white', bg='black')
        self.entry = tk.Entry(self.frame, width=61, bg='grey', fg='yellow')

    def add_listbox(self, event):
        self.listbox.insert('end', '>>>' + self.entry.get())
        cmd = self.entry.get().split(' ')
        self.entry.delete(0, 'end')
        print(cmd)
        if cmd[0] == 'add':
            commands.add(cmd)
        elif cmd[0] == 'rem':
            commands.rem(cmd)
        elif cmd[0] == 'cd':
            commands.cd(cmd)
        elif cmd[0] == 'cdlist':
            commands.cdlist(cmd)
        elif cmd[0] == 'ren':
            commands.ren(cmd)
        elif cmd[0] == 'addfold':
            commands.addfold(cmd)
        elif cmd[0] == 'remfold':
            commands.remfold(cmd)
        elif cmd[0] == 'help':
            commands.help(cmd)
        else:
            self.print_screen("[!] ERROR [!] Unknow command")

    def print_screen(self, text):
        self.listbox.insert('end', text)      

root = tk.Tk()
root = App(root)
root.mainloop()