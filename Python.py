# dust
import tkinter as tk
import time

class TimerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Таймер")
        
        self.timer_running = False
        self.start_time = None
        self.elapsed_time = 0
        
        self.time_label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)
        
        self.start_button = tk.Button(self.root, text="Старт", command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.pause_button = tk.Button(self.root, text="Пауза", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(pady=10)
        
        self.reset_button = tk.Button(self.root, text="Сброс", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def start_timer(self):
        if not self.timer_running:
            self.start_time = time.time() - self.elapsed_time
            self.update_timer()
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
    
    def pause_timer(self):
        if self.timer_running:
            self.root.after_cancel(self.update_id)
            self.elapsed_time = time.time() - self.start_time
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
    
    def reset_timer(self):
        if not self.timer_running:
            self.elapsed_time = 0
            self.update_timer()
            self.reset_button.config(state=tk.DISABLED)
    
    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time + self.elapsed_time)
            hours = elapsed_time // 3600
            minutes = (elapsed_time % 3600) // 60
            seconds = elapsed_time % 60
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_label.config(text=time_str)
            self.update_id = self.root.after(1000, self.update_timer)
    
    def on_close(self):
        if self.timer_running:
            self.root.after_cancel(self.update_id)
        self.root.destroy()

if __name__ == "__main__":
    app = TimerApp()
    app.root.mainloop()
