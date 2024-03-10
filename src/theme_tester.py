import tkinter as tk
from kawaiikit import Window


'''

Kawaii Kit
Window Manager Package for Tkinter

Author: thirdtype
https://github.com/thethirdtype

'''


def main():
    # Create a window manager instance, Toplevel
    main_window = Window(title="Kawaii Kit Theme Tester", width=620, height=274, disable_dark_mode=False,
                         force_dark_mode=False)

    # Create a frame for initial padding
    initial_padding_frame = main_window.Frame(height=10)
    initial_padding_frame.pack(anchor="w", padx=4, pady=4, side=tk.TOP)

    # Create and configure widgets from theme
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

    # Create and pack widgets
    for i, (widget_type, kwargs) in enumerate(widgets):
        if i % 3 == 0:
            frame = main_window.Frame()
            frame.pack(anchor="w", padx=4, pady=4, side=tk.TOP)

        # Create the widget
        if widget_type == "Listbox":
            label = main_window.Label(text=f"{widget_type}: ", anchor="e", width=15)
            label.pack(in_=frame, side=tk.LEFT, padx=(0, 5))

            widget_frame = main_window.Frame()
            widget_frame.pack(in_=frame, side=tk.LEFT)

            widget = main_window.create(widget_type, selectmode=tk.MULTIPLE, exportselection=False, **kwargs)
            for item in range(10):  # Adding dummy entries to the listbox
                widget.insert(tk.END, f"Item {item + 1}")
            widget.pack(in_=widget_frame, side=tk.LEFT)

        elif widget_type == "Text":
            text_frame = main_window.Frame()
            text_frame.pack(in_=frame, side=tk.LEFT, padx=(0, 5))

            label = main_window.Label(text="Text &\nScrollbar: ", anchor="e", width=15)
            label.pack(in_=text_frame, side=tk.LEFT, padx=(0, 5))

            widget = main_window.create(widget_type, **kwargs)
            widget.pack(in_=text_frame, side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar = main_window.Scrollbar(command=widget.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y, in_=text_frame)
            widget.config(yscrollcommand=scrollbar.set)

        elif widget_type == "Checkbutton" or widget_type == "Radiobutton":
            label = main_window.Label(text=f"{widget_type}: ", anchor="e", width=15)
            label.pack(in_=frame, side=tk.LEFT, padx=(0, 5))

            widget = main_window.create(widget_type, **kwargs)
            widget.pack(in_=frame, side=tk.LEFT)

        else:
            label = main_window.Label(text=f"{widget_type}: ", anchor="e", width=15)
            label.pack(in_=frame, side=tk.LEFT, padx=(0, 5))

            widget = main_window.create(widget_type, **kwargs)
            widget.pack(in_=frame, side=tk.LEFT, padx=(0, 5))

    # Run the window
    main_window.run()


if __name__ == "__main__":
    main()
