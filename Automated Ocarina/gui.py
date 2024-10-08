from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter.ttk import Progressbar
import time
import threading

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\tryst\OneDrive\Notebook\Automated Ocarina\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def run_progress(duration):
    for i in range(101):
        progress_bar['value'] = i
        time.sleep(duration / 100)  # Progress bar updates in steps proportional to the total duration
    progress_bar['value'] = 0  # Reset progress bar once done


def on_button_click(duration):
    threading.Thread(target=run_progress, args=(duration,)).start()


window = Tk()
window.geometry("700x550")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=550,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Button 1 (30 seconds)
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click(5),
    relief="flat"
)
button_1.place(
    x=121.0,
    y=144.0,
    width=457.0,
    height=88.0
)

# Button 2 (60 seconds)
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click(10),
    relief="flat"
)
button_2.place(
    x=122.0,
    y=395.0,
    width=457.0,
    height=88.0
)

# Button 3 (90 seconds)
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click(15),
    relief="flat"
)
button_3.place(
    x=121.0,
    y=261.0,
    width=457.0,
    height=88.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    110.0,
    fill="#B30000",
    outline=""
)

canvas.create_text(
    110.0,
    29.0,
    anchor="nw",
    text="Song Selector",
    fill="#FFFFFF",
    font=("Inter Bold", 64 * -1)
)

# Create the progress bar
progress_bar = Progressbar(window, orient="horizontal", length=500, mode="determinate")
progress_bar.place(x=100, y=500)

window.resizable(False, False)
window.mainloop()
