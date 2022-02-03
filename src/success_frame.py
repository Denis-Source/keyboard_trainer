from src.success_frame_ui import SuccessFrameUI


class SuccessFrame(SuccessFrameUI):
    """
    Inherits ui components and their configurations from StartFrameUI class
    Adds frame functionality
    """
    def __init__(self, parent, **kw):
        """
        Initializes ui components
        """
        super().__init__(parent, **kw)
        self.parent = parent

    def load_stats(self, text_instance):
        """
        Sets stats to the labels
        :param text_instance:
        :return:
        """
        self.speed_value["text"] = f"{text_instance.get_speed()}ppm"
        self.accuracy_value["text"] = f"{text_instance.get_accuracy()}%"
        self.total_symbols_value["text"] = text_instance.get_total()

    def load_plot(self, text_instance):
        """
        Sets matplotlib plot with typing speed history
        :param text_instance: TextInstance
        :return: None
        """
        self.figure.clear()
        data = text_instance.get_plot_data()
        plot = self.figure.add_subplot()
        plot.plot(data["rights"][0], data["rights"][1], color=self.TEXT_GOOD)
        plot.plot(data["wrongs"][0], data["wrongs"][1], color=self.TEXT_BAD)
        self.canvas.draw()
