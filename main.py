import customtkinter as ctk

from Classes.MessageFrame import MessageFrame
from Classes.EntryFrame import EntryFrame
from Classes.ChatFrame import ChatFrame
from Classes.TopFrame import TopFrame

messageRow = 0

class Root(ctk.CTk):
    """
    -----------
    Attributes:

    topFrame : TopFrame
        Top frame for containing the SimpliCT logo.
    chatFrame : ChatFrame
        Scrollable frame containing all chat messages.
    entryFrame : EntryFrame
        Bottom frame containing text box and "send" button.
    """
    def __init__(self):
        super().__init__()

        self.title("SimpliCT") # root window title
        self.geometry('800x900') # root window size (widthxheight)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # top frame for containing the SimpliCT logo
        self.topFrame = TopFrame(self)
        self.topFrame.grid(row=0, column=0, sticky="new")

        # Scrollable frame containing all chat messages
        self.chatFrame = ChatFrame(self)
        self.chatFrame.grid(row=1, column=0, sticky="nsew")

        # Bottom frame containing text box and "send" button
        self.entryFrame = EntryFrame(self)
        self.entryFrame.grid(row=2, column=0, sticky="ews")

        self.entryFrame.entry.after(10, self.entryFrame.entry.focus_set)

    def insertUserChat(self):
        """ Callback function for inserting chat messages from the user.
            The function inserts the message into a MessageFrame, which is inserted into the ChatFrame.
            Once the function has been run, it calls the insertBotChat function. 
        """
        global messageRow
        userEntry = self.entryFrame.entry.get()

        if not userEntry == "":
            print("User entry: " + userEntry)

            self.chatMessage = MessageFrame(self.chatFrame, entry=userEntry, isBot=False)
            self.chatMessage.grid(row=messageRow, padx=10, pady=10, sticky="e")
            self.entryFrame.entry.delete(0, len(userEntry))

            messageRow += 1

            self.insertBotChat(userEntry)
    
    def insertUserChatByEnter(self, event):
        """ Callback function for inserting chat messages from the user when pressing the Enter key.
            This is done because a button event apparently needs an "event" parameter, which messes up when pressing the Send button.
        """
        self.insertUserChat()
    
    def insertBotChat(self, userEntry):
        """ 
        This function fetches the response from the chatbot module.

        ----------
        Parameters:

        userEntry : str
            The chat input from the user 
        """
        global messageRow

        #TODO: implement functionality for fetching bot answer

        # Can be deleted once chatbot responses can be fetched.
        botEntry = ["I'll get you two. You're nothing but pure evil! Just like newspaper comics.",
                    "I've had enough of your dastardly deeds, Dirty Dan! I'm gonna get you and your partner, Pinhead Larry, or my name ain't Sheriff Sandy!",
                    "I warned ya, Dirty Dan, now, you've just crossed the border into Hurtville!",
                    "I'm gonna catch you and throw you in jail at taxpayers' expense!",
                    "Gonna skin y'all and make a pair of size six boots!"]

        # print("Bot entry: " + botEntry)

        # When we can fetch chatbot responses, edit the "entry" parameter for the MessageFrame object.
        self.chatMessage = MessageFrame(self.chatFrame, entry=botEntry[messageRow%5], isBot=True)
        self.chatMessage.grid(row=messageRow, padx=10, pady=10, sticky="w")

        messageRow += 1

        self.chatFrame._parent_canvas.yview_moveto()

root = Root()
root.mainloop()