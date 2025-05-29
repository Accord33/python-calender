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

        # 日付情報の取得
        now = datetime.now()
        year, month, today = now.year, now.month, now.day
        month_calendar = calendar.monthcalendar(year, month)

        # 曜日ラベル（日～土）
        days = ['日', '月', '火', '水', '木', '金', '土']
        for idx, day in enumerate(days):
            lbl = ttk.Label(self.calendar_frame, text=day, width=5, anchor='center', font=("Arial", 10, "bold"))
            lbl.grid(row=0, column=idx, padx=2, pady=2)

        # 日付表示エリア
        for row_idx, week in enumerate(month_calendar):
            for col_idx, date in enumerate(week):
                if date == 0:
                    text = ""
                else:
                    text = str(date)
                # 本日を強調表示
                label_kwargs = {"text": text, "width": 5, "anchor": 'center', "relief": 'ridge'}
                if date == today:
                    # PEP 8に従い、TODAY_HIGHLIGHT_COLOR = '#ffeb3b' のような定数を定義することを検討してください
                    label_kwargs["background"] = '#ffeb3b' # または TODAY_HIGHLIGHT_COLOR を使用
                date_lbl = ttk.Label(self.calendar_frame, **label_kwargs)
                date_lbl.grid(row=row_idx+1, column=col_idx, padx=2, pady=2)

if __name__ == "__main__":
    app = CalendarApp()
    app.mainloop()
