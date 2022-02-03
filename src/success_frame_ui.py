import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from config import Config


class SuccessFrameUI(tk.Frame, Config):
    """
    Defines ui structure and components of the start frame
    """
    def __init__(self, parent, **kw):
        """
        Initializes following ui elements:
            label and selected category label
            information frame with such stats as accuracy, total symbols and speed
            figure element to show matplotlib plot
        Configures colors, fonts and other features of ui elements
        :param parent: Tk
        :param kw: dict
        """

        super().__init__(**kw)
        self.parent = parent
        self.configure(bg=self.BACKGROUND)

        self.label = tk.Label(
            self,
            font=(self.FONT_FAMILY, 24),
            text="Text selected from category:",
            bg=self.BACKGROUND,
            fg=self.FG_MAIN
        )
        self.sub_label = tk.Label(
            self,
            text="category",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_COMP,
        )

        self.info_frame = tk.Frame(
            self,
            bg=self.BACKGROUND,
        )

        self.figure = Figure(
            figsize=(5.2, 3.9),
            dpi=100
        )

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=self.info_frame
        )

        self.stat_frame = tk.Frame(
            self.info_frame,
            width=240,
            height=390,
            bg=self.BACKGROUND
        )

        self.speed_label = tk.Label(
            self.stat_frame,
            text="Speed:",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_MAIN,
            anchor="e"
        )

        self.speed_value = tk.Label(
            self.stat_frame,
            text="100",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_COMP,
            anchor="e"
        )

        self.accuracy_label = tk.Label(
            self.stat_frame,
            text="Accuracy:",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_MAIN,
            anchor="e"
        )

        self.accuracy_value = tk.Label(
            self.stat_frame,
            text="100",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_COMP,
            anchor="e"
        )

        self.total_symbols_label = tk.Label(
            self.stat_frame,
            text="Total Symbols:",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_MAIN,
            anchor="e"
        )

        self.total_symbols_value = tk.Label(
            self.stat_frame,
            text="100",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_COMP,
            anchor="e"
        )

        self.category_label = tk.Label(
            self.stat_frame,
            text="Category:",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_MAIN,
            anchor="e"
        )

        self.category_value = tk.Label(
            self.stat_frame,
            text="test",
            font=(self.FONT_FAMILY, 18),
            bg=self.BACKGROUND,
            fg=self.FG_COMP,
            anchor="e"
        )
        self.draw_ui()

    def draw_ui(self):
        """
        Packs all of the ui elements to the frame
        Sets padding of the ui elements
        :return: None
        """
        self.label.pack(pady=(50, 0))
        self.sub_label.pack(pady=(5, 0))
        self.info_frame.pack(pady=(30, 0))
        self.canvas.get_tk_widget().pack(side=tk.LEFT)

        self.stat_frame.pack(padx=(20, 0), side=tk.RIGHT, fill="both")
        self.speed_label.pack(pady=(10, 0), fill="both")
        self.speed_value.pack(pady=(5, 0), fill="both")
        self.accuracy_label.pack(pady=(10, 0), fill="both")
        self.accuracy_value.pack(pady=(5, 0), fill="both")
        self.total_symbols_label.pack(pady=(10, 0), fill="both")
        self.total_symbols_value.pack(pady=(5, 0), fill="both")
        self.category_label.pack(pady=(10, 0), fill="both")
        self.category_value.pack(pady=(10, 0), fill="both")
