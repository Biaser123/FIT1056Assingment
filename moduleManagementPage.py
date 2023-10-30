import tkinter as tk
from moduleFrame import moduleFrame


class ModuleManagementPage(tk.Frame):
    def __init__(self, master, user, return_page):
        super().__init__(master)
        self.module_buttons = {}
        self.user = user
        self.master = master
        self.return_page = return_page

        self.canvas = tk.Canvas(self, width=1200, height=500)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollable_frame = tk.Frame(self.canvas)
        self.canvas.create_window((100, 25), window=self.scrollable_frame, anchor='nw')
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        for module in range(1, 6):
            self.create_module_button(f"Module {module}")

        return_button = tk.Button(self.scrollable_frame, text="Return", command=self.return_func,width=10,height=3,bg="lightgray")
        return_button.grid(row= 3, column=3)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.module_states = {}
        self.load_module_states()

    def on_frame_configure(self, event):
        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def access_module(self, module_selected):
        if self.module_buttons[module_selected]["active"]:
            print(f"Accessing {module_selected}")
            self.place_forget()
            module_page = moduleFrame(self.master, self, module_selected, self.user)
            module_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            print(f"{module_selected} is inactive and cannot be accessed.")

    def create_module_button(self, module_name):
        module_button = tk.Button(self.scrollable_frame, text=module_name,
                                  command=lambda m=module_name: self.access_module(m),width=16,height=6,font=(14))
        module_button.grid(row=1, column=len(self.module_buttons) + 1,padx=10,pady=10)

        active_button = tk.Button(self.scrollable_frame, text="Inactive",
                                  command=lambda m=module_name: self.toggle_module_status(m),width=16,height=6,font=(14))
        active_button.grid(row=2, column=len(self.module_buttons) + 1,padx=10,pady=10)

        self.module_buttons[module_name] = {"module_button": module_button, "active_button": active_button,
                                            "active": False}  # Set the initial state to Inactive

    def toggle_module_status(self, module_name):
        self.module_buttons[module_name]["active"] = not self.module_buttons[module_name]["active"]
        self.save_module_states()

        if self.module_buttons[module_name]["active"]:
            self.module_buttons[module_name]["active_button"].config(text="Active\n(Click to deactivate)")
            self.module_buttons[module_name]["active_button"].config(bg="light green")
        else:
            self.module_buttons[module_name]["active_button"].config(text="Inactive\n(Click to activate)")
            self.module_buttons[module_name]["active_button"].config(bg="#FFCCCC")

    def load_module_states(self):
        try:
            with open('data/module_states.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    module_name, state = line.strip().split(',')
                    if module_name in self.module_buttons:
                        self.module_buttons[module_name]["active"] = (state == 'Active')
                        if state == 'Active':
                            self.module_buttons[module_name]["active_button"].config(text="Active\n(Click to deactivate)")
                            self.module_buttons[module_name]["active_button"].config(bg="light green")
                        else:
                            self.module_buttons[module_name]["active_button"].config(text="Inactive\n(Click to activate)")
                            self.module_buttons[module_name]["active_button"].config(bg="#FFCCCC")
        except FileNotFoundError:
            pass

    def save_module_states(self):
        with open('data/module_states.txt', 'w') as file:
            for module_name, data in self.module_buttons.items():
                state = 'Active' if data["active"] else 'Inactive'
                file.write(f"{module_name},{state}\n")

    def return_func(self):
        self.place_forget()
        self.return_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
