from kawaiikit import Window


class MyApp:
    def __init__(self):
        self.main_window = Window(title="Hello World!", width=300, height=100, force_theme=False, css_file=None)
        self.create_widgets()
        self.main_window.run()

    def create_widgets(self):
        label = self.main_window.Label(text="ハローワールド！", font=("Arial", 24))
        label.pack(expand=True)


if __name__ == "__main__":
    app = MyApp()
