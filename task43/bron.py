from tkinter import *
from tkinter import messagebox as mb

def bookSeat():
    seat_name = seat_entry.get().upper()
    try:
        if seats[seat_name]=="свободно":
            seats[seat_name] = "забронировано"
            updateCanvas()
            mb.showinfo("Успешно",f"Место {seat_name} успешно забронировано.")
        else:
            mb.showerror("Ошибка", f"Место {seat_name} уже забронировано или не существует.")
    except KeyError:
        mb.showerror("Ошибка", f"Место {seat_name} не существует.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")

def bookSeatDelete():
    seatName = seatEntryDelete.get().upper()
    try:
        if seats[seatName]=="забронировано":
            seats[seatName] = "свободно"
            updateCanvasDelete()
            mb.showinfo("Успешно",f"Бронь для места {seatName} успешно отменено.")
        else:
            mb.showerror("Ошибка", f"Место {seatName} уже свободно или не существует.")
    except KeyError:
        mb.showerror("Ошибка", f"Место {seatName} не существует.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")

def updateCanvas():
    canvas.delete("all")
    for i, (seat, stat) in enumerate(seats.items()):
        x=i * 40 + 20
        y=20
        color = "green" if stat=="свободно" else "red"
        canvas.create_rectangle(x,y,x+30,y+30,fill=color)
        canvas.create_text(x+15,y+15,text=seat)

def updateCanvasDelete():
    canvas.delete("all")
    for i, (seat, stat) in enumerate(seats.items()):
        x=i * 40 + 20
        y=20
        color = "red" if stat=="забронировано" else "green"
        canvas.create_rectangle(x,y,x+30,y+30,fill=color)
        canvas.create_text(x+15,y+15,text=seat)

window=Tk()
window.title("Бронирование мест")
window.geometry("400x300")

canvas=Canvas(width=400, height=60)
canvas.pack()

canvas2=Canvas(width=400, height=70)
canvas2.pack()
canvas2.create_rectangle(50,0,100,50,fill='green')
canvas2.create_text(150,25,text='Свободно')

canvas2.create_rectangle(200,0,250,50,fill='red')
canvas2.create_text(320,25,text='Забронировано')

seats = {f'Б{i}': "свободно" for i in range(1, 10)}

seat_entry=Entry()
seat_entry.pack()
seat_entry.focus_set()
seat_entry.bind("<Return>",bookSeat)

Button(text="Забронировать", command=bookSeat).pack(pady=10)

seatEntryDelete=Entry()
seatEntryDelete.pack()
seatEntryDelete.bind("<Return>",bookSeatDelete)

Button(text="Отменить бронь", command=bookSeatDelete).pack(pady=10)


updateCanvas()

window.mainloop()