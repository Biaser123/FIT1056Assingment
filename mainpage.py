import tkinter as tk


class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        login_canvas = tk.Canvas(master=self, width=128, height=128)
        login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        login_title = tk.Label(master=self,
                               text="Welcome to CodeVenture",
                               font=("Arial Bold", 25))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

    def edit_profile(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("960x540")
    app = MainPage(root)
    root.mainloop()
