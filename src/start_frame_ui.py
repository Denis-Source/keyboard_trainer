import tkinter as tk

from config import Config


class StartFrameUI(tk.Frame, Config):
    """
    Defines ui structure and components of the start frame
    """
    def __init__(self, parent, **kw):
        """
        Initializes following ui elements:
            language frame to contain current language label
            category selection label
            category selection Listbox
            start button
        Configures colors, fonts and other features of ui elements
        :param parent: Tk
        :param kw: dict
        """
        super().__init__(**kw)
        self.parent = parent
        self.configure(bg=self.BACKGROUND)

        self.language_frame = tk.Frame(
            self,
            bg=self.BACKGROUND,
        )

        self.language_label = tk.Label(
            self.language_frame,
            font=(self.FONT_FAMILY, 24),
            bg=self.BACKGROUND,
            fg=self.FG_COMP
        )

        self.select_category_frame = tk.Frame(
            self,
            bg=self.BACKGROUND
        )

        self.main_label = tk.Label(
            self.select_category_frame,
            text="Start typing",
            font=(self.FONT_FAMILY, 36),
            bg=self.BACKGROUND,
            fg=self.FG_MAIN
        )

        self.select_category_label = tk.Label(
            self.select_category_frame,
            text="Select Category",
            font=(self.FONT_FAMILY, 24),
            bg=self.BACKGROUND,
            fg=self.FG_COMP
        )

        self.category_select = tk.Listbox(
            self.select_category_frame,
            font=(self.FONT_FAMILY, 16),
            bg=self.BACKGROUND,
            fg=self.FG_MAIN,
            selectforeground=self.FG_MAIN,
            selectbackground=self.TEXT_DEFAULT,
            height=0
        )

        self.start_button = tk.Button(
            self,
            text="Start",
            font=(self.FONT_FAMILY, 24),
            bg=self.FG_MAIN,
            fg=self.BACKGROUND,
            width=12,
            borderwidth=0
        )

        self.draw_ui()

    def draw_ui(self):
        """
        Packs all of the ui elements to the frame
        Sets padding of the ui elements
        :return: None
        """
        self.language_frame.pack()
        self.language_label.pack(padx=(420, 0), pady=20)
        self.main_label.pack(pady=(50, 20))

        self.select_category_frame.pack()
        self.select_category_label.pack(pady=(30, 0))
        self.category_select.pack(pady=(20, 0))
        self.start_button.pack(pady=(50, 50))

    def insert_categories(self, categories):
        """
        Inserts category names into the ListBox selection menu
        Sorts them alphabetically
        Ads additional 'random' category
        :param categories: list
        :return: None
        """
        categories = sorted(list(categories), reverse=True)
        categories.append("random")
        for c in categories:
            self.category_select.insert(0, c)
        self.category_select.select_set(0)

    def set_selected_language(self, language):
        """
        Sets selected language label to the current system language
        :param language:
        :return:
        """
        self.language_label["text"] = f"selected language: {language}"

    def get_selected_category(self):
        """
        Gets selected category from the ListBox selection menu
        :return:
        """
        return self.category_select.get(self.category_select.curselection())
