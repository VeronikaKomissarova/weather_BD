import requests
import tkinter as tk
import tksheet as tks
import weather

URL = 'http://api.openweathermap.org/data/2.5/forecast'
APPID = '58a889be127f7f70338ecc32ab86f89b'

window = tk.Tk()
window.title('Погода в городе на 5 дней')
window.geometry('700x550')
label = tk.Label(text = 'Город')
label.pack()
entry = tk.Entry(width=50)
entry.pack()
scrl = tk.Frame(window, pady=35)
table = tks.Sheet(scrl,show_row_index=False,  headers= ("Дата и время", "Температура", "Состояние"),column_width=200, width=650)
table.pack_forget()
scrl.pack()


def get_weather():
    city = entry.get()
    w = weather.weather(URL,APPID, city).get_data()
    table.set_sheet_data(data=[ [w[i][j] for i in range(len(w)) ] for j in range(len(w[0]))])
    table.pack()


btn = tk.Button(window, text="ОК", command= get_weather)
btn.pack()

window.mainloop()
