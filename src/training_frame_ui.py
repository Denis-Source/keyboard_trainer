import tkinter as tk
from config import Config


class TrainingFrameUI(tk.Frame, Config):
    """
    Defines ui structure and components of the training frame
    """

    def __init__(self, root, **kwargs):
        """
        Initializes following ui elements:
            category label
            canvas
        Configures colors, fonts and other features of ui elements
        Uses canvas element to display training text
        :param parent: Tk
        :param kw: dict
        """
        super().__init__(**kwargs)
        self.root = root
        self.configure(bg=self.BACKGROUND)

        self.label = tk.Label(
            self,
            font=(self.FONT_FAMILY, 24),
            text="Text selected from category:",
            bg=self.BACKGROUND,
            fg=self.FG_MAIN
        )
        self.sub_label = tk.Label(
            self, text="category",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_COMP,
        )
        self.canvas = tk.Canvas(
            self,
            width=724,
            height=390,
            highlightthickness=0,
            relief="ridge"
        )
        self.draw_ui()

    def draw_ui(self):
        """
        Packs all of the ui elements to the frame
        Sets padding of the ui elements
        :return:
        """
        self.label.pack(pady=(50, 0))
        self.sub_label.pack(pady=(5, 0))
        self.redraw_bg()
        self.canvas.configure(bg=self.BACKGROUND)
        self.canvas.pack(pady=(30, 10))

    def redraw_bg(self):
        """
        Redraws canvas
        Used for clearing the text
        :return:
        """
        self.draw_rectangle(0, 0, 724, 390, 25, fill=self.FG_MAIN)

    def draw_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        """
        Drawing canvas rectangle with the specified coordinates and border
        :param x1: int x top left corner
        :param y1: int y top left corner
        :param x2: int x bottom right corner
        :param y2: int y bottom right corner
        :param radius: int border radius
        :param kwargs: dict
        :return: None
        """
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        self.canvas.create_polygon(points, **kwargs, smooth=True)
