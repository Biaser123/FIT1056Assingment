# Third party imports
import tkinter as tk

# Local application imports
from loginframe import LoginFrame


class Interface(tk.Tk):
    """
    Class definition for the Interface class
    """
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.overrideredirect(True)

        close_button = tk.Button(self, text="X", command=self.destroy,width=5,height=1,bg="lightgray")
        close_button.pack(anchor="ne", padx=10, pady=10)
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        #Constructor for the Interface class,
        #the main window for the HCMS.
        
if __name__ == "__main__":
    # DO NOT MODIFY THIS
    hcms = Interface("CodeVenture")
    login = LoginFrame(hcms)
    login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    hcms.mainloop()
    print("--- End of program execution ---")
