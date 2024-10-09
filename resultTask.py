from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

# Функция для обновления метки с названием криптовалюты
def update_crypto_label(event):
    # Получаем полное название криптовалюты из словаря и обновляем метку
    crypto_code = crypto_combobox.get()
    name = cryptocurrencies[crypto_code]
    crypto_label.config(text=name)

# Функция для обновления метки с названием целевой валюты
def update_target_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    target_code = target_combobox.get()
    name = currencies[target_code]
    target_label.config(text=name)

# Функция для получения курса обмена
def get_exchange_rate():
    target_code = target_combobox.get()
    crypto_code = crypto_combobox.get()

    if target_code and crypto_code:
        try:
            exchange_rate  = requests.get(f'https://api.coingecko.com/api/v3/coins/{crypto_code}')
            exchange_rate .raise_for_status()
            data  = exchange_rate .json()

            if target_code in data ['market_data']['current_price']:
                exchange_rate = data ['market_data']['current_price'][target_code]
                base_currency = cryptocurrencies[crypto_code]
                target_currency = currencies[target_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {target_currency} за 1 {base_currency}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Пожалуйста, выберите коды валют")

# Словарь кодов криптовалют и их полных названий
cryptocurrencies = {
    "bitcoin": "Биткоин",
    "ethereum": "Эфириум",
    "ripple": "Рипли",
    "litecoin": "Лайткоин",
    "cardano": "Кардано"
}

# Словарь кодов валют и их полных названий
currencies = {
    "usd": "Американский доллар",
    "eur": "Евро",
    "jpy": "Японская йена",
    "gbp": "Британский фунт стерлингов",
    "aud": "Австралийский доллар",
    "cad": "Канадский доллар",
    "chf": "Швейцарский франк",
    "cny": "Китайский юань",
    "rub": "Российский рубль",
    "kzt": "Казахстанский тенге",
    "uzs": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Конвертор крипты")
window.geometry("360x300")

# Метка и комбобокс для выбора криптовалюты
Label(text="Криптовалюта:").pack(padx=10, pady=5)
crypto_combobox = ttk.Combobox(values=list(cryptocurrencies.keys()))
crypto_combobox.pack(padx=10, pady=5)
crypto_combobox.bind("<<ComboboxSelected>>", update_crypto_label)

# Метка для отображения полного названия криптовалюты
crypto_label = ttk.Label()
crypto_label.pack(padx=10, pady=10)

# Метка и комбобокс для выбора целевой валюты
Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)

# Метка для отображения полного названия целевой валюты
target_label = ttk.Label()
target_label.pack(padx=10, pady=10)

# Кнопка для получения курса обмена
Button(text="Получить курс обмена", command=get_exchange_rate).pack(padx=10, pady=10)

# Запуск главного цикла приложения
window.mainloop()
