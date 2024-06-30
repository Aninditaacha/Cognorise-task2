import tkinter as tk
import time

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.geometry("250x150")

        
        self.hour_label = tk.Label(master, text="Hours:")
        self.hour_label.pack()
        self.hour_entry = tk.Entry(master, width=5)
        self.hour_entry.pack()

        self.minute_label = tk.Label(master, text="Minutes:")
        self.minute_label.pack()
        self.minute_entry = tk.Entry(master, width=5)
        self.minute_entry.pack()

        self.second_label = tk.Label(master, text="Seconds:")
        self.second_label.pack()
        self.second_entry = tk.Entry(master, width=5)
        self.second_entry.pack()

       
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        
        self.countdown_label = tk.Label(master, text="", font=("Helvetica", 24))
        self.countdown_label.pack()

      
        self.timer_running = False
        self.time_left = 0

    def start_timer(self):
        
        hours = int(self.hour_entry.get())
        minutes = int(self.minute_entry.get())
        seconds = int(self.second_entry.get())

      
        self.time_left = hours * 3600 + minutes * 60 + seconds

      
        self.timer_running = True
        self.update_timer()

       
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)

    def stop_timer(self):
     
        self.timer_running = False

        
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def update_timer(self):
        if self.timer_running:
            
            hours, remainder = divmod(self.time_left, 3600)
            minutes, seconds = divmod(remainder, 60)

           
            self.countdown_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

          
            self.time_left -= 1

            
            self.master.after(1000, self.update_timer)

           
            if self.time_left <= 0:
                self.timer_running = False
                self.countdown_label.config(text="Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()