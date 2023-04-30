import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x300")  # set window size
        self.master.configure(background="#1a1a1a")  # set background color
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def count_up(self):
            filename = "tracker_counter.txt" #file name to update
            with open(filename, "r") as file:
                count = int(file.read())
            count+=1
            with open(filename, "w") as file:
                file.write(str(count))

    def read_count(self):
        filename = "tracker_counter.txt" #file name to read
        with open(filename, "r") as file:
            return int(file.read())

    #the options
    def create_widgets(self):
        self.options = [
            tk.BooleanVar(value=False),
            tk.BooleanVar(value=False),
            tk.BooleanVar(value=False),
            tk.BooleanVar(value=False),
            tk.BooleanVar(value=True)
        ]
        
        #Change option names here
        for i, option in enumerate(["opt1", "opt2", "opt3", "opt4", "days done: "+ str(self.read_count())]): #option names/customiztions
            tk.Checkbutton(self, text=option, variable=self.options[i], font=("Terminal", 16), fg="#ababab", bg="#1a1a1a", activebackground="#1a1a1a", activeforeground="#ababab", selectcolor="#1a1a1a", highlightthickness=10, bd=0, command=self.check_all_options).pack(pady=10)

    #the end is here
    def check_all_options(self):
        all_toggled = all(option.get() for option in self.options)
        if all_toggled:
            self.count_up()
            self.master.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("T-bone")
    app = Application(master=root)
    app.mainloop()
