import tkinter as tk
import ctypes


def is_dark_mode():
    try:
        # Check the system-wide color preferences using GETCLIENTAREAANIMATION
        ui_param = ctypes.c_uint(0)
        ctypes.windll.user32.SystemParametersInfoW(0x1042, 0, ctypes.byref(ui_param), 0)
        return ui_param.value == 1
    except Exception as e:
        print(f"Error detecting dark mode: {e}")
        return None


class Window:
    def __init__(self, title=None, width=300, height=200, center_screen=True, x=0, y=0, icon=None,
                 disable_dark_mode=False, force_dark_mode=False):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        if center_screen:
            self.root.eval("tk::PlaceWindow . center")
        else:
            self.root.geometry(f"+{x}+{y}")

        # Check if dark mode is enabled
        dark_mode = is_dark_mode()

        # Set window colors for dark mode
        if force_dark_mode or not disable_dark_mode and dark_mode:
            # Dictionary mapping widget types to color schemes
            self.color_schemes = {
                "Button": {"bg": "#383838", "fg": "#FFFFFF"},
                "Entry": {"bg": "#191919", "fg": "#FFFFFF"},
                "Text": {"bg": "#191919", "fg": "#8FD139"},
                "Window": {"bg": "#2C2C2C", "fg": "#FFFFFF"},
                # Add more widget types and their color schemes here
            }

            # Set background color for the root window
            color_scheme = self.color_schemes["Window"]
            self.root.configure(bg=color_scheme["bg"])

        # Set Icon
        if icon:
            self.root.iconbitmap(icon)

    def create(self, widget_type, **kwargs):
        if not isinstance(widget_type, type):
            # Prepend tk. if widget_type is not a class
            widget_type = getattr(tk, widget_type)
        
        # Create the widget with provided parameters
        widget = widget_type(self.root, **kwargs)

        # Apply color scheme if available
        if widget.winfo_class() in self.color_schemes:
            color_scheme = self.color_schemes[widget.winfo_class()]
            widget.config(bg=color_scheme["bg"], fg=color_scheme["fg"])

        # Pack the widget into the window
        widget.pack()

        # Return the created widget
        return widget

    def run(self):
        self.root.mainloop()
