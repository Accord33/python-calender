import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

class CalendarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("カレンダーアプリケーション")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # カレンダー表示用フレーム
        self.calendar_frame = ttk.Frame(self)
        self.calendar_frame.pack(pady=20)

        # 曜日ラベル（日～土）
        days = ['日', '月', '火', '水', '木', '金', '土']
        for idx, day in enumerate(days):
            lbl = ttk.Label(self.calendar_frame, text=day, width=5, anchor='center', font=("Arial", 10, "bold"))
            lbl.grid(row=0, column=idx, padx=2, pady=2)

        # 日付表示エリア（空のまま）
        for row in range(1, 7):
            for col in range(7):
                date_lbl = ttk.Label(self.calendar_frame, text="", width=5, anchor='center', relief='ridge')
                date_lbl.grid(row=row, column=col, padx=2, pady=2)

if __name__ == "__main__":
    app = CalendarApp()
    app.mainloop()
