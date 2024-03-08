import customtkinter as ctk
from PIL import Image, ImageTk

class TopFrame(ctk.CTkFrame):
    """
    Top frame for containing the SimpliCT logo.

    -----------
    Attributes:

    image : CTkImage
        The logo image.
    """
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)

        self.image = ctk.CTkImage(light_image=Image.open('SimpliCT_logo.png'), size=(271, 70))
        image_label = ctk.CTkLabel(self, image=self.image, text="")
        image_label.grid(sticky="ew")