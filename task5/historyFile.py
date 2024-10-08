from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import pyperclip
import json
import os


def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files=files)
                response.raise_for_status()  # проверка на ошибки
                download_link = response.json()["link"]
                entry.insert(0, download_link)
                pyperclip.copy(download_link)
                save_history(filepath, download_link)
                mb.showinfo("Успешно!", "Ссылка успешно скопирована")
        else:
            raise ValueError("Не удалось отправить файл")

    except ValueError as v:
        mb.showerror("Ошибка", f"Произошла ошибка {v}")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")


def save_history(file_path, download_link):
    hist_list = []
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            hist_list = json.load(file)

    hist_list.append({"file_path": os.path.basename(file_path),
                      "download_link": download_link})
    with open(history_file, "w") as file:
        json.dump(hist_list, file, indent=1)


def show_history():
    history_window = Toplevel(window)
    history_window.title("История загрузок")
    history_window.geometry("400x300")

    hist_list = []
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            hist_list = json.load(file)

    for item in hist_list:
        file_label = f"Файл: {item['file_path']}, Ссылка: {item['download_link']}"
        ttk.Label(history_window, text=file_label).pack(anchor='w')


history_file = "history.json"

window = Tk()
window.title("Файл в облако")
window.geometry("400x200")

upload_button = ttk.Button(text="Загрузить файл", command=upload)
upload_button.pack()

entry = ttk.Entry()
entry.pack()

history_button = ttk.Button(text="Показать историю загрузок", command=show_history)
history_button.pack(pady=10)

window.mainloop()
