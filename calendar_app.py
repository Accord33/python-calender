import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

# 本日強調色
TODAY_HIGHLIGHT_COLOR = '#ffecb3'

class CalendarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("カレンダーアプリケーション")
        self.geometry("400x350")
        now = datetime.now()
        self.current_year = now.year
        self.current_month = now.month
        self.today = now.day
        self.create_widgets()
        self.draw_calendar()

    def create_widgets(self):
        # 年月表示ラベルとボタン
        top_frame = ttk.Frame(self)
        top_frame.pack(pady=10)
        self.prev_btn = ttk.Button(top_frame, text="前月へ", command=self.show_prev_month)
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        self.month_label = ttk.Label(top_frame, text="", font=("Arial", 12, "bold"))
        self.month_label.pack(side=tk.LEFT, padx=10)
        self.next_btn = ttk.Button(top_frame, text="次月へ", command=self.show_next_month)
        self.next_btn.pack(side=tk.LEFT, padx=5)

        # カレンダー表示用フレーム
        self.calendar_frame = ttk.Frame(self)
        self.calendar_frame.pack(pady=10)

    def draw_calendar(self):
        # 週の始まりを日曜日に固定
        calendar.setfirstweekday(calendar.SUNDAY)
        # 既存カレンダー消去
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        # 年月ラベル更新
        self.month_label.config(text=f"{self.current_year}年{self.current_month}月")
        # 曜日ラベル
        days = ['日', '月', '火', '水', '木', '金', '土']
        for idx, day in enumerate(days):
            lbl = ttk.Label(self.calendar_frame, text=day, width=5, anchor='center', font=("Arial", 10, "bold"))
            lbl.grid(row=0, column=idx, padx=2, pady=2)
        # 日付表示
        month_calendar = calendar.monthcalendar(self.current_year, self.current_month)
        for row_idx, week in enumerate(month_calendar):
            for col_idx, date in enumerate(week):
                if date == 0:
                    text = ""
                else:
                    text = str(date)
                label_kwargs = {"text": text, "width": 5, "anchor": 'center', "relief": 'ridge'}
                _now = datetime.now() # Get current datetime once for this check
                if (self.current_year, self.current_month, date) == (_now.year, _now.month, _now.day):
                    label_kwargs["background"] = TODAY_HIGHLIGHT_COLOR
                date_lbl = ttk.Label(self.calendar_frame, **label_kwargs)
                date_lbl.grid(row=row_idx+1, column=col_idx, padx=2, pady=2)

    def show_prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.draw_calendar()

    def show_next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.draw_calendar()

if __name__ == "__main__":
    app = CalendarApp()
    app.mainloop()
