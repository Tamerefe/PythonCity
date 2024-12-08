import time 
import tkinter as tk

class StopWatch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Stopwatch')
        self.geometry('300x100')
        self.time = 0
        self.running = False
        self.label = tk.Label(self, text='0:00:00', font=('Helvetica', 48))
        self.label.pack()
        self.button = tk.Button(self, text='Start', command=self.start_stop)
        self.button.pack()
        self.reset_button = tk.Button(self, text='Reset', command=self.reset)
        self.reset_button.pack()

    def start_stop(self):
        self.running = not self.running
        if self.running:
            self.button.config(text='Stop')
            self.update()
        else:
            self.button.config(text='Start')

    def update(self):
        if self.running:
            self.time += 1
            minutes = self.time // 60
            seconds = self.time % 60
            hours = minutes // 60
            minutes %= 60
            self.label.config(text=f'{hours}:{minutes:02d}:{seconds:02d}')
            self.after(1000, self.update)

    def reset(self):
        self.time = 0
        self.label.config(text='0:00:00')
        self.button.config(text='Start')
        self.running = False

if __name__ == '__main__':
    stopwatch = StopWatch()
    stopwatch.mainloop()

