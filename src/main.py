from wm import Window
import tkinter as tk

def main():
    # Create a window manager instance
    main_window = Window(title="Hello World", width=400, height=300, disable_dark_mode=False, force_dark_mode=False)
    close_button = main_window.create("Button", text="Close", command=main_window.root.destroy)

    # Run the window
    main_window.run()

if __name__ == "__main__":
    main()
