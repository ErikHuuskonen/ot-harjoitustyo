import tkinter as tk


class LoadingScreen:
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(self.window)

        self.loading_label = tk.Label(self.frame, text="Loading Screen")
        self.loading_label.pack(pady=10)
        self.on_exit = None
        self.exit_button = tk.Button(self.frame, text="Continue", command= self.exit)
        self.exit_button.pack(pady=10)

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()
    
    def exit(self):
        if self.on_exit:
            self.on_exit()