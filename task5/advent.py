from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time

t = None

def set_reminder():
    global t
    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24-часовой формат)")
    if rem:
        if ":" in rem:
            parts = rem.split(":")
            if len(parts) == 2:
                try:
                    hour = int(parts[0])
                    minute = int(parts[1])
                    now = datetime.datetime.now()
                    dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                    if dt < now:
                        dt += datetime.timedelta(days=1)
                    t = dt.timestamp()
                    label.config(text=f"Напоминание установлено на: {hour:02}:{minute:02}")
                except ValueError:
                    mb.showerror("Ошибка", "Неверный формат времени")
            else:
                mb.showerror("Ошибка", "Введите время в формате ЧЧ:ММ")
        else:
            mb.showerror("Ошибка", "Введите время в формате ЧЧ:ММ")

def check_reminder():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_sound()
            show_reminder()
            t = None
    window.after(10000, check_reminder)

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()

def stop_sound():
    pygame.mixer.music.stop()

def show_reminder():
    current_time = datetime.datetime.now().strftime("%H:%M")
    mb.showinfo("Напоминание", f"Напоминание, сейчас {current_time}")

window = Tk()
window.title("Напоминание")

label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set_reminder)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", command=stop_sound)
stop_button.pack(pady=10)

check_reminder()

window.mainloop()