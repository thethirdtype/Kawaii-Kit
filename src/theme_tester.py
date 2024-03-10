import tkinter as tk
from kawaiikit import Window


'''

Kawaii Kit
Window Manager Package for Tkinter

Author: thirdtype
https://github.com/thethirdtype

'''


class ThemeTester:
    def __init__(self):
        self.main_window = Window(title="Kawaii Kit Theme Tester", width=620, height=274, disable_dark_mode=False,
                                  force_theme=False, css_file=None)
        self.create_widgets()
        self.main_window.run()

    def create_widgets(self):
        initial_padding_frame = self.main_window.Frame(height=10)
        initial_padding_frame.pack(anchor="w", padx=4, pady=4, side=tk.TOP)

        widgets = [
            ("Button", {"text": "  Button  "}),
            ("Canvas", {"width": 80, "height": 40}),
            ("Checkbutton", {"text": "Checkbutton"}),
            ("Entry", {"width": 10}),
            ("Frame", {"width": 80, "height": 40}),
            ("Label", {"text": "Label"}),
            ("Listbox", {"height": 3, "width": 10}),
            ("Menubutton", {"text": "Menubutton"}),
            ("Message", {"text": "Message"}),
            ("Radiobutton", {"text": "Radiobutton"}),
            ("Scale", {"length": 60}),
            ("Text", {"width": 10, "height": 4}),
        ]

        frame = None
        for i, (widget_type, kwargs) in enumerate(widgets):
            if i % 3 == 0:
                frame = self.main_window.Frame()
                frame.pack(anchor="w", padx=4, pady=4, side=tk.TOP)

            if widget_type == "Listbox":
                self.create_listbox(frame, widget_type, kwargs)
            elif widget_type == "Text":
                self.create_text_widget(frame, widget_type, kwargs)
            elif widget_type in ["Checkbutton", "Radiobutton"]:
                self.create_check_or_radio_button(frame, widget_type, kwargs)
            else:
                self.create_default_widget(frame, widget_type, kwargs)

    def create_listbox(self, frame, widget_type, kwargs):
        label = self.main_window.Label(text=f"{widget_type}: ", anchor="e", width=15)
        label.pack(in_=frame, side=tk.LEFT, padx=(0, 5))

        widget_frame = self.main_window.Frame()
        widget_frame.pack(in_=frame, side=tk.LEFT)

        widget = self.main_window.create(widget_type, selectmode=tk.MULTIPLE, exportselection=False, **kwargs)
        for item in range(10):
            widget.insert(tk.END, f"Item {item + 1}")
        widget.pack(in_=widget_frame, side=tk.LEFT)

    def create_text_widget(self, frame, widget_type, kwargs):
        text_frame = self.main_window.Frame()
        text_frame.pack(in_=frame, side=tk.LEFT, padx=(0, 5))

        label = self.main_window.Label(text="Text &\nScrollbar: ", anchor="e", width=15)
        label.pack(in_=text_frame, side=tk.LEFT, padx=(0, 5))

        widget = self.main_window.create(widget_type, **kwargs)
        widget.pack(in_=text_frame, side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = self.main_window.Scrollbar(command=widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, in_=text_frame)
        widget.config(yscrollcommand=scrollbar.set)

    def create_check_or_radio_button(self, frame, widget_type, kwargs):
        label = self.main_window.Label(text=f"{widget_type}: ", anchor="e", width=15)
        label.pack(in_=frame, side=tk.LEFT, padx=(0, 5))

        widget = self.main_window.create(widget_type, **kwargs)
        widget.pack(in_=frame, side=tk.LEFT)

    def create_default_widget(self, frame, widget_type, kwargs):
        label = self.main_window.Label(text=f"{widget_type}: ", anchor="e", width=15)
        label.pack(in_=frame, side=tk.LEFT, padx=(0, 5))

        widget = self.main_window.create(widget_type, **kwargs)
        widget.pack(in_=frame, side=tk.LEFT, padx=(0, 5))


if __name__ == "__main__":
    app = ThemeTester()
