import customtkinter as ctk

class ChatFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="#212121")

        