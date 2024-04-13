import tkinter as tk
import ctypes
import os
from typing import Dict, Union


'''

Kawaii Kit
Window Manager Package for Tkinter

Author: thirdtype
https://github.com/thethirdtype

'''


def is_dark_mode() -> Union[bool, None]:
    try:
        # Check the system-wide color preferences using GETCLIENTAREAANIMATION
        ui_param = ctypes.c_uint(0)
        ctypes.windll.user32.SystemParametersInfoW(0x1042, 0, ctypes.byref(ui_param), 0)
        return ui_param.value == 1
    except Exception as e:
        print(f"Error detecting dark mode: {e}")
        return None


def load_color_schemes_from_css(css_file: str) -> Dict[str, Dict[str, str]]:
    color_schemes = {}
    if css_file:
        try:
            with open(css_file, 'r') as f:
                lines = f.readlines()
                current_widget = None
                for line in lines:
                    line = line.strip()
                    if line.startswith('.'):
                        current_widget = line.split('.')[1].split('{')[0].strip()
                        color_schemes[current_widget] = {}
                    elif current_widget and ':' in line:
                        key, value = line.split(':')
                        key = key.strip()
                        value = value.strip().rstrip(';')
                        color_schemes[current_widget][key] = value
        except FileNotFoundError:
            print(f"CSS file '{css_file}' not found. Skipping color scheme loading.")
        except Exception as e:
            print(f"Error loading color schemes from CSS file: {e}")
    return color_schemes


class Window:
    def __init__(self, title: str = None, width: int = 300, height: int = 200, center_screen: bool = True,
                 x: int = 0, y: int = 0, icon: str = None, disable_dark_mode: bool = False,
                 force_theme: bool = False, css_file: str = None) -> None:

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        if center_screen:
            screenwidth = self.root.winfo_screenwidth()
            screenheight = self.root.winfo_screenheight()
            alignment = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            self.root.geometry(alignment)
        else:
            self.root.geometry(f"+{x}+{y}")

        # Get the current directory
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Set themes directory
        themes_dir = f"{current_directory}\\themes"

        # If css_file is not provided, use the default CSS file name
        if css_file is None:
            css_file = os.path.join(themes_dir, "dark_mode.css")
        elif not os.path.isfile(css_file):
            # If it doesn't exist, assume it's in the themes directory
            css_file = os.path.join(themes_dir, css_file)

        # Set default icon and path
        default_icon = "brush.ico"
        icons_dir = current_directory

        # If icon is not provided, use the default ICO file name
        if icon is None:
            icon = os.path.join(icons_dir, default_icon)
        elif not os.path.isfile(icon):
            # If it doesn't exist, assume it's in the icons directory
            icon = os.path.join(icons_dir, icon)

        # If icon is still invalid, use the default ICO file name
        if not os.path.isfile(icon):
            icon = os.path.join(icons_dir, default_icon)

        # Check if dark mode is enabled
        dark_mode = is_dark_mode()

        # Set window colors for dark mode
        if force_theme or (not disable_dark_mode and dark_mode):
            # Load color schemes from CSS file if provided
            self.color_schemes = load_color_schemes_from_css(css_file)

            # Set background color for the root window
            if "Toplevel" in self.color_schemes:
                color_scheme = self.color_schemes["Toplevel"]
                bg_color = color_scheme.get("bg", "")
                if bg_color:
                    self.root.configure(bg=bg_color)

        # Set Icon
        if os.path.isfile(icon):
            self.root.iconbitmap(icon)

    def button(self, **kwargs):
        return self.create("Button", **kwargs)

    Button = button

    def canvas(self, **kwargs):
        return self.create("Canvas", **kwargs)

    Canvas = canvas

    def checkbutton(self, **kwargs):
        return self.create("Checkbutton", **kwargs)

    Checkbutton = checkbutton

    def create(self, widget_type: Union[type, str], **kwargs) -> Union[tk.Widget, None]:
        if not isinstance(widget_type, type):
            # Prepend tk. if widget_type is not a class
            widget_type = getattr(tk, widget_type)

        # Create the widget with provided parameters
        widget = widget_type(self.root, **kwargs)

        # Apply color scheme if available
        if hasattr(self, 'color_schemes') and widget.winfo_class() in self.color_schemes:
            color_scheme = self.color_schemes[widget.winfo_class()]
            for attr, value in color_scheme.items():
                # Check if the attribute can be configured for the widget
                if hasattr(widget, 'configure') and widget.configure().keys().__contains__(attr.replace("-", "_")):
                    # Set the attribute dynamically
                    widget.configure(**{attr.replace("-", "_"): value})

        # Pack the widget into the window
        widget.pack()

        # Return the created widget
        return widget

    Create = create

    def entry(self, **kwargs):
        return self.create("Entry", **kwargs)

    Entry = entry

    def frame(self, **kwargs):
        return self.create("Frame", **kwargs)

    Frame = frame

    def label(self, **kwargs):
        return self.create("Label", **kwargs)

    Label = label

    def listbox(self, **kwargs):
        return self.create("Listbox", **kwargs)

    Listbox = listbox

    def menu(self, **kwargs):
        return self.create("Menu", **kwargs)

    Menu = menu

    def menubutton(self, **kwargs):
        return self.create("Menubutton", **kwargs)

    Menubutton = menubutton

    def message(self, **kwargs):
        return self.create("Message", **kwargs)

    Message = message

    def radiobutton(self, **kwargs):
        return self.create("Radiobutton", **kwargs)

    Radiobutton = radiobutton

    def run(self) -> None:
        self.root.mainloop()

    Run = run

    def scale(self, **kwargs):
        return self.create("Scale", **kwargs)

    Scale = scale

    def scrollbar(self, **kwargs):
        return self.create("Scrollbar", **kwargs)

    Scrollbar = scrollbar

    def text(self, **kwargs):
        return self.create("Text", **kwargs)

    Text = text

    def toplevel(self, **kwargs):
        return self.create("Toplevel", **kwargs)

    Toplevel = toplevel
