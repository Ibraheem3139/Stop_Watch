import tkinter as tk
from time import strftime, time

class DigitalClockStopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock and Stopwatch")
        self.root.geometry("400x300")
        self.root.configure(bg='lightgray')
        self.clock_time = tk.StringVar()
        self.running = False
        self.start_time = 0

        self.clock_label = tk.Label(self.root, textvariable=self.clock_time, font=('calibri', 50, 'bold'), background='lightgray', foreground='black')
        self.clock_label.pack(pady=20)
        self.center_widget(self.clock_label)

        self.date_label = tk.Label(self.root, font=('calibri', 16, 'bold'), background='lightgray', foreground='black')
        self.date_label.pack(pady=10)
        self.center_widget(self.date_label)

        self.stopwatch_label = tk.Label(self.root, text="00:00:00", font=('calibri', 30, 'bold'), background='lightgray', foreground='black')
        self.stopwatch_label.pack(pady=20)
        self.center_widget(self.stopwatch_label)

        self.start_stop_button = tk.Button(self.root, text="Start", command=self.toggle_stopwatch, width=10)
        self.start_stop_button.pack(pady=10)
        self.center_widget(self.start_stop_button)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_stopwatch, width=10)
        self.reset_button.pack(pady=10)
        self.center_widget(self.reset_button)

        self.update_time()

    def toggle_stopwatch(self):
        if not self.running:
            self.start_time = time()
        self.running = not self.running

    def reset_stopwatch(self):
        self.running = False
        self.start_time = 0
        self.stopwatch_label.config(text="00:00:00")

    def update_time(self):
        current_time = strftime('%I:%M:%S %p')  # 12-hour format
        date_string = strftime('%A, %d %B %Y')
        self.clock_time.set(current_time)
        self.date_label.config(text=date_string)
        if self.running:
            elapsed_time = time() - self.start_time
            self.stopwatch_label.config(text=self.format_time(elapsed_time))
        self.root.after(1000, self.update_time)

    def format_time(self, elapsed_seconds):
        hours, remainder = divmod(elapsed_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    def center_widget(self, widget):
        widget.update_idletasks()
        widget.pack_configure(anchor='center')

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClockStopwatch(root)
    root.mainloop()
