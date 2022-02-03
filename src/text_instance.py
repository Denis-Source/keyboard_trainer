import time


class TextInstance:
    """
    Tracks selected text and text category
    Provides all logic to key presses
    Tracks right and wrong presses, typing accuracy and speed
    in specified time time periods
    """

    # signal constants that indicate key press
    RIGHT = 0
    WRONG = 1
    FINISH = 2

    def __init__(self, text):
        """
        Sets start time
        Initializes key presses history lists and strings
        Sets current index to 0
        :param text:
        """
        self.start_time = time.time()
        self.end_time = None
        self.text = text
        self.printed_text = ""
        self.wrong_text = ""
        self.category = None
        self.current_index = 0
        self.wrongs = 0
        self.right_timings = []
        self.wrong_timings = []

    def add_char(self, char):
        """
        Adds pressed character to the history
        Tracts whether the pressed key is correct
        Returns signal code to the corresponding situation
        :param char: str
        :return: int
        """
        # checks whether the character char is correct
        # and all wrong characters are erased
        if self.text[self.current_index] == char and len(self.wrong_text) == 0:
            self.printed_text += self.text[self.current_index]
            self.wrong_text = ""
            self.current_index += 1
            self.right_timings.append(time.time())

            # if current index is out of bounds (the last character was already typed)
            # returns the FINISH signal
            if self.current_index == len(self.text):
                self.end_time = time.time()
                return self.FINISH
            return self.RIGHT

        # if the current character is Backspace
        elif char == '\x08':
            # erases the last wrong character
            self.wrong_text = self.wrong_text[:-1]
            # if there are still wrong characters
            if len(self.wrong_text) > 0:
                # returns the WRONG signal
                return self.WRONG
            else:
                # if there are no wrong character left
                # returns the RIGHT signal
                return self.RIGHT
        else:
            # returns the WRONG signal
            self.wrongs += 1
            self.wrong_timings.append(time.time())
            self.wrong_text += char
            return self.WRONG

    def set_category(self, category):
        """
        Sets the category
        :param category: str
        :return: None
        """
        self.category = category

    def get_category(self):
        """
        Gets the category
        :return: str
        """
        return self.category

    def get_text(self):
        """
        Gets the text
        :return: str
        """
        return self.text

    def get_printed_text(self):
        """
        Gets the printed text
        :return: str
        """
        return self.printed_text

    def get_wrong_text(self):
        """
        Gets the wrong text
        :return: str
        """
        return self.printed_text + self.wrong_text

    def get_speed(self):
        """
        Calculates typing speed
        :return: float
        """
        time_spent = self.end_time - self.start_time
        value = len(self.text) / time_spent * 60
        return round(value)

    def get_accuracy(self):
        """
        Calculates typing accuracy
        :return: float
        """
        value = 100 - self.wrongs / len(self.text) * 100
        return round(value, 2)

    def get_total(self):
        """
        Gets total text length
        :return: int
        """
        return len(self.text)

    def get_plot_data(self, interval=5):
        """
        Prepares typing history data for the plot
        Returns dictionary with the amount of right and wrong presses
        divided into specified time periods
        :param interval: int seconds
        :return: dict
        """
        chunked_data = {
            "rights": ([], []),
            "wrongs": ([], [])
        }

        # for each time period
        for chunk_time in range(0, round(self.end_time - self.start_time) + interval, interval):
            # appends time chunk (key presses for period)
            chunked_data["rights"][0].append(chunk_time)
            chunked_data["wrongs"][0].append(chunk_time)

            chunked_data["rights"][1].append(0)
            chunked_data["wrongs"][1].append(0)

            # for each key press
            for r in self.right_timings:
                # if press in the time period
                # adds it to time chung
                if chunk_time - interval < r - self.start_time < chunk_time:
                    chunked_data["rights"][1][-1] += 60 / interval

            for r in self.wrong_timings:
                if chunk_time - interval < r - self.start_time < chunk_time:
                    chunked_data["wrongs"][1][-1] += 60 / interval

        return chunked_data
