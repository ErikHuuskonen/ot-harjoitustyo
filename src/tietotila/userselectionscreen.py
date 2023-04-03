import tkinter as tk

class UserSelectionScreen:
    def __init__(self, window, user_management):
        self.window = window
        self.user_management = user_management
        
        self.frame = tk.Frame(self.window)
        
        self.title_label = tk.Label(self.frame, text="Select User")
        self.title_label.pack(pady=10)
        
        self.user_listbox = tk.Listbox(self.frame)
        self.user_listbox.pack(pady=10)
        
        self.new_user_button = tk.Button(self.frame, text="New User", command=self.create_new_user)
        self.new_user_button.pack(pady=10)
        
        self.select_user_button = tk.Button(self.frame, text="Select User", command=self.select_user)
        self.select_user_button.pack(pady=10)
        
        self.on_user_selected = None

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.update_user_list()

    def hide(self):
        self.frame.pack_forget()

    def update_user_list(self):
        self.user_listbox.delete(0, tk.END)
        users = self.user_management.get_users()
        for user in users:
            self.user_listbox.insert(tk.END, user)

    def create_new_user(self):
        new_user_name = tk.simpledialog.askstring("New User", "Enter a new user name:")
        if new_user_name:
            self.user_management.create_user(new_user_name)
            self.update_user_list()

    def select_user(self):
        selected_user_index = self.user_listbox.curselection()
        if selected_user_index:
            user = self.user_listbox.get(selected_user_index)
            if self.on_user_selected:
                self.on_user_selected(user)

    