import ctypes
import json
from threading import Thread
import time

from src.start_frame_ui import StartFrameUI
from config import Config


class StartFrame(StartFrameUI, Config):
    """
    Inherits ui components and their configurations from StartFrameUI class
    Adds frame functionality
    """
    # System language selection constants
    languages = {
        134809609:
            {
                "full": "English/UK",
                "short": "en"
            },
        67700745:
            {
                "full": "English/US",
                "short": "en"
            },
        68755456:
            {
                "full": "Russian",
                "short": "ru"
            }
    }

    def __init__(self, parent, **kw):
        """
        Initializes ui components
        Gets categories from the json file
        Inserts categories to the ListBox category selection menu
        :param parent: Tk
        :param kw: dict
        """
        super().__init__(parent, **kw)
        categories = self.get_categories()
        self.insert_categories(categories)
        self.set_language()

    def get_categories(self):
        """
        Gets category names from the json file
        :return: list
        """
        data = json.load(
            open(self.TEXTS_FILEPATH, "r")
        )
        categories = set([cat["category"] for cat in data])
        return categories

    def set_language_threaded(self, event=None):
        """
        Calls language selection function to change language label
        The function is threaded as the event key event comes before system language change
        :param event: Event
        :return: None
        """
        Thread(target=self.set_language).start()

    def set_language(self):
        """
        Sets language label
        :return:
        """
        time.sleep(0.2)
        self.set_selected_language(
            self.get_system_language()["short"]
        )

    def get_system_language(self):
        """
        Gets selected system language
        Converts it form integer to string using class constant
        If the language is not predefined returns Unknown, na
        :return: dict
        """
        layout = ctypes.windll.user32.GetKeyboardLayout(0)
        return self.languages.get(layout, {
            "full": "Unknown",
            "short": "na"
        })
