from wm import Window
import tkinter as tk


'''

wm-lib
Window Manager Library for Tkinter

Author: thirdtype
https://github.com/thethirdtype

'''


def main():
    # Create a window manager instance, Toplevel
    main_window = Window(title="Dark Theme Test", width=600, height=1160, disable_dark_mode=False, force_dark_mode=True)

    # Create and configure widgets from dark_theme.css
    widgets = {
        "Button": {"text": "Button"},
        "Canvas": {"width": 200, "height": 100},
        "Checkbutton": {"text": "Checkbutton"},
        "Entry": {},
        "Frame": {"width": 200, "height": 100},
        "Label": {"text": "Label"},
        "Listbox": {"height": 4},
        # "Menu": {},  # Not added as Menu cannot be directly added to the window
        "Menubutton": {"text": "Menubutton"},
        "Message": {"text": "This is a Message widget."},
        "Radiobutton": {"text": "Radiobutton"},
        "Scale": {},
        "Scrollbar": {"orient": tk.HORIZONTAL},
        "Text": {"width": 50, "height": 10}
    }

    # Create and pack widgets
    for widget_type, kwargs in widgets.items():
        # Create a frame to contain the label and the widget
        frame = tk.Frame(main_window.root)
        frame.pack(anchor="w", padx=4, pady=4)

        # Create a label indicating the widget type
        # label = tk.Label(frame, text=widget_type)
        label = main_window.create("Label", text=widget_type)
        # label.pack(side="left")

        # Create the widget
        widget = main_window.create(widget_type, **kwargs)

    # Run the window
    main_window.run()

if __name__ == "__main__":
    main()
