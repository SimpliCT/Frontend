from typing import Tuple
import customtkinter as ctk
import textwrap

class MessageFrame(ctk.CTkFrame):
    """
    Subframe for the ChatFrame, containing a single message from either the user or bot.

    -----------
    Attributes:

    isBot : bool
        Bool telling the class if the message comes from the user or the bot.
    entry : str
        The chat entry to be displayed in the frame.
    self.title : CTkLabel
        Top string of the message frame displaying who the message came from.
        Can either be "You: " or "SimpliCT: ".
    self.message : CTkLabel
        The actual message that will be displayed.
    """
    def __init__(self, master, isBot:bool, entry):
        super().__init__(master)

        wrapper = textwrap.TextWrapper(width=64) 
        self.entry = wrapper.fill(text=entry) # This ensures that the message boxes never go wider than 64 characters. Inserts newline in whitespace nearest to this limit.

        titleFont = ctk.CTkFont(family="Roboto", size=14, weight="bold")
        messageFont = ctk.CTkFont(family="Roboto", size=14)
        titleSticky = ""

        if isBot:
            self.configure(fg_color="#272727")
            self.title = ctk.CTkLabel(self, 
                                      text="SimpliCT", 
                                      anchor="sw", 
                                      justify="left", 
                                      font=titleFont, 
                                      height=titleFont._size+10)
            titleSticky = "w"
            self.message = ctk.CTkLabel(self, 
                                        text=self.entry, 
                                        anchor="w", 
                                        justify="left", 
                                        font=messageFont, 
                                        text_color="#e0e0e0")
        else:
            self.configure(fg_color="#303030")
            self.title = ctk.CTkLabel(self, 
                                      text="You", 
                                      anchor="se", 
                                      justify="right", 
                                      font=titleFont, 
                                      height=titleFont._size+10)
            titleSticky = "e"
            self.message = ctk.CTkLabel(self, 
                                        text=self.entry, 
                                        anchor="e", 
                                        justify="right", 
                                        font=messageFont, 
                                        text_color="#e0e0e0")

        self.title.grid(row=0, column=0, padx=10, sticky=titleSticky)
        self.message.grid(row=1, column=0, padx=10, pady=5, sticky="w")