import json
import tkinter as tk
from random import choice

from src.text_instance import TextInstance
from src.success_frame import SuccessFrame
from src.training_frame_ui import TrainingFrameUI
from config import Config


class TrainingFrame(TrainingFrameUI, Config):
    """
    Inherits ui components and their configurations from StartFrameUI class
    Adds frame functionality
    """

    def __init__(self, parent, **kwargs):
        """
        Initializes text instance, success frame
        :param parent:
        :param kwargs:
        """
        super().__init__(parent, **kwargs)
        self.root = parent

        # filename to store texts
        self.texts_filepath = "text.json"

        # allowed keys to press while typing text
        self.keys_allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.'\"?!-0123456789\x08"

        self.text_instance = None
        self.success_frame = SuccessFrame(parent)

    def load_text(self, category):
        """
        Loads text from json file
        Uses TextInstance class
        Sets category and text to the TextInstance
        Sets category label
        :param category:
        :return:
        """
        self.root.bind("<KeyPress>", self.text_input)
        self.canvas.delete("all")
        self.redraw_bg()
        data = json.load(
            open(self.TEXTS_FILEPATH, "r")
        )
        if category != "random":
            category_texts = [text for text in data if text["category"] == category]
        else:
            category_texts = data

        self.text_instance = TextInstance(
            choice(category_texts)["text"]
        )
        self.text_instance.set_category(category)
        self.sub_label["text"] = category
        self.draw_text(self.text_instance.get_text(), self.TEXT_DEFAULT)

    def draw_text(self, text, color):
        """
        Draws text on canvas with specified font and color
        Justify to the left
        Font width (boldness) 700
        :param text:
        :param color:
        :return:
        """
        self.canvas.create_text(
            20, 20, fill=color,
            anchor=tk.NW,
            font=f"{self.FONT_FAMILY} {self.FONT_SIZE} bold",
            width=700,
            justify=tk.LEFT,
            text=text,
        )

    def text_input(self, event):
        """
        Draws typed characters on canvas
        Checks whether the character is correct or not
        Redraws whole text with an each allowed button press
        Draws the text in appropriate color
        Checking is done with the TextInstance class
        If the text is done, calls finish() method
        :param event:
        :return:
        """
        # gets a pressed character
        if event.char in self.keys_allowed and event.char != "":
            # if the character is allowed and not empty
            # ads character to the TextInstance
            signal = self.text_instance.add_char(event.char)

            # redraws canvas each button press
            # using appropriate color
            if signal == self.text_instance.RIGHT:
                self.canvas.delete("all")
                self.redraw_bg()
                self.draw_text(self.text_instance.get_text(), self.TEXT_DEFAULT)
                self.draw_text(self.text_instance.get_printed_text(), self.TEXT_GOOD)
            elif signal == self.text_instance.WRONG:
                self.canvas.delete("all")
                self.redraw_bg()
                self.draw_text(self.text_instance.get_wrong_text(), self.TEXT_BAD)
            elif signal == self.text_instance.FINISH:
                self.finish()

    def finish(self):
        """
        Calls success frame to show stats
        Hides all the other ui components
        Unbinds all key presses bind before
        :return: None
        """
        self.root.unbind("<KeyPress>")
        self.pack_forget()
        self.success_frame.load_stats(self.text_instance)
        self.success_frame.load_plot(self.text_instance)
        self.success_frame.pack()
