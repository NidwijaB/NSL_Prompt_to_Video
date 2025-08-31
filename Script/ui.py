import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from translator import translate_text_to_sign
from PIL import Image, ImageTk
import os, sys


def resource_path(relative_path):
    """Get absolute path to resource."""
    if hasattr(sys, "_MEIPASS"):  # for PyInstaller so that it bundles files into temp folder
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class SignTranslatorApp(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title(" Nepali Sign Language: Text to Sign Translator 🇳🇵")
        self.geometry("1250x650")
        self.minsize(800, 500)

        # Main container
        container = tb.Frame(self, padding=20)
        container.grid(row=0, column=0, sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Header
        tb.Label(
            container,
            text="Nepali Sign Language ✋ Text to Sign Translator",
            font=("Segoe UI Semibold", 28),
            bootstyle=INFO
        ).grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="ew")

        # Text entry
        self.entry = tb.Entry(container, width=40, font=("Segoe UI", 13))
        self.entry.grid(row=1, column=0, columnspan=3, pady=5, sticky="ew")
        self.entry.bind("<Return>", lambda e: self.on_translate())

        self.icon_translate = ImageTk.PhotoImage(
            Image.open(resource_path("icons/translate.png")).resize((20, 20))
        )
        self.icon_clear = ImageTk.PhotoImage(
            Image.open(resource_path("icons/clear.png")).resize((20, 20))
        )
        self.icon_info = ImageTk.PhotoImage(
            Image.open(resource_path("icons/info.png")).resize((20, 20))
        )

        # Buttons
        tb.Button(container, text=" Translate", image=self.icon_translate,
                  compound="left", bootstyle=SUCCESS, command=self.on_translate)\
          .grid(row=2, column=0, padx=5, pady=10, sticky="ew")

        tb.Button(container, text=" Clear", image=self.icon_clear,
                  compound="left", bootstyle=DANGER, command=self.clear_text)\
          .grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        tb.Button(container, text=" Info", image=self.icon_info,
                  compound="left", bootstyle=WARNING, command=self.toggle_info)\
          .grid(row=2, column=2, padx=5, pady=10, sticky="ew")

        # Persistent status/history label
        self.status = tb.Label(
            container,
            text="",
            font=("Segoe UI", 12),
            bootstyle=PRIMARY,
            padding=8,
            anchor="w",
            justify="left"
        )
        self.status.grid(row=3, column=0, columnspan=3, pady=10, sticky="ew")

        # Collapsible info
        self.info_visible = False
        self.info_label = tb.Label(
            container,
            text="",
            font=("Segoe UI", 12),
            wraplength=500,
            justify="center",
            bootstyle=INFO,
            padding=10
        )

        # Responsive columns
        for i in range(3):
            container.columnconfigure(i, weight=1)

    def on_translate(self):
        txt = self.entry.get().strip()

        if not txt:
            messagebox.showwarning("⚠️ Oops!", "Please enter some text.")
            self.append_status("⚠️ No prompt entered — please type something above.", WARNING)
            return

        ok, missing = translate_text_to_sign(txt)

        if missing:
            self.append_status(f"❌ Missing clips: {', '.join(missing)}", DANGER)

        if not ok:
            messagebox.showwarning("⚠️ Not found", f"No clips could be played for '{txt}'.")
            self.append_status(f"⚠️ Prompt not found: '{txt}'", DANGER)
        else:
            self.append_status(f"✨ Translated: {txt}", PRIMARY)

    def append_status(self, message, style):
        prev_text = self.status.cget("text")
        new_text = prev_text + "\n" + message if prev_text else message
        self.status.config(text=new_text, bootstyle=style)

    def clear_text(self):
        self.entry.delete(0, "end")
        self.status.config(text="", bootstyle=PRIMARY)
        self.info_label.grid_remove()
        self.info_visible = False

    def toggle_info(self):
        if self.info_visible:
            self.info_label.grid_remove()
            self.info_visible = False
        else:
            creators = (
                "🎇Created by:\n"
                "- Nidwija Bhatta \n"
                "- Anjesh Ojha \n"
                "- Bishow Raj Pangeni \n"
                "- Prabin Dahal \n"
                " *_*_*_*_*_*_*_*_*_*_*_*_*_*_* \n"
                " MSCSK BATCH 081 GROUP A"
            )
            self.info_label.config(text=creators)
            self.info_label.grid(row=4, column=0, columnspan=3, pady=5, sticky="nsew")
            self.info_visible = True


if __name__ == "__main__":
    app = SignTranslatorApp()
    app.mainloop()
