import tkinter as tk
from config import Config
from src.training_frame import TrainingFrame
from src.start_frame import StartFrame


class KeyboardT(tk.Tk, Config):
    """
    Main program class based on tkiner Tk
    Consists of main, starting (configuration), training frame
    Has no components, hosts other frames
    Methods:
        start hosts start screen
        training hosts start screen
    """
    def __init__(self):
        """
        Initializes root and others frames
        """
        super().__init__()
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.configure(bg=self.BACKGROUND)

        self.start_frame = StartFrame(self)
        self.training_frame = TrainingFrame(self)
        self.main_frame = tk.Frame(self)

    def start(self, event=None):
        """
        Draws start frame
        Binds buttons to call start frame events
        Hide other frames
        :param event: Event
        :return: None
        """
        self.start_frame.start_button.bind("<Button-1>", self.training)
        self.unbind("<Escape>")
        self.bind("<Return>", self.training)
        self.bind("<KeyPress>", self.start_frame.set_language_threaded)
        self.training_frame.pack_forget()
        self.training_frame.success_frame.pack_forget()
        self.start_frame.pack()

    def training(self, event=None):
        """
        Draws training frame
        Binds buttons to call training frame events
        Hide other frames
        :param event: Event
        :return: None
        """
        self.bind("<Escape>", self.start)
        self.unbind("<Return>")
        self.start_frame.pack_forget()
        self.training_frame.pack()
        self.training_frame.load_text(self.start_frame.get_selected_category())

    def mainloop(self, n=0):
        """
        Initially draws start frame
        :param n: int
        :return: None
        """
        self.start()
        super().mainloop()


if __name__ == '__main__':
    KeyboardT().mainloop()
