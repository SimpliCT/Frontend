import customtkinter as ctk

from Classes.ChatFrame import ChatFrame

class EntryFrame(ctk.CTkFrame):
    """
    Bottom frame containing the entry box and "Send" button.

    -----------
    Attributes:

    self.entry : CTkEntry
        Entry box allowing for user input
    self.btn : CTkButton
        Button for sending the user input from self.entry.
    """
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color="#212121")

        self.entry = ctk.CTkEntry(self)
        self.entry.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
        
        # calls the insertUserChatByEnter function when pressing Enter key
        self.entry.bind(sequence="<Return>", command = master.insertUserChatByEnter)

        self.btn = ctk.CTkButton(self, text = "Send", command = master.insertUserChat)
        self.btn.grid(column=1, row=0, padx=10, pady=10, sticky="nsew")
