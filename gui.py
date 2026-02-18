import tkinter as tk
from tkinter import messagebox, scrolledtext
from business_layer import BusinessLayer


class LoginWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Database Login")
        self.geometry("350x300")
        self.configure(bg="#f6e6ff")
        self.resizable(False, False)

        tk.Label(self, text="Server", bg="#f6e6ff").pack()
        self.server_entry = tk.Entry(self)
        self.server_entry.insert(0, "localhost")
        self.server_entry.pack()

        tk.Label(self, text="Database", bg="#f6e6ff").pack()
        self.database_entry = tk.Entry(self)
        self.database_entry.insert(0, "postgres")
        self.database_entry.pack()

        tk.Label(self, text="Username", bg="#f6e6ff").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password", bg="#f6e6ff").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login, bg="#d9b3ff", fg="black").pack(pady=10)

    def login(self):
        host = self.server_entry.get()
        database = self.database_entry.get()
        user = self.username_entry.get()
        password = self.password_entry.get()

        try:
            business = BusinessLayer(host, database, user, password)
            business.test_connection()
            self.destroy()
            MainViewer(business, user).mainloop()
        except Exception:
            messagebox.showerror("Login Failed", "Invalid credentials or access denied.")


class MainViewer(tk.Tk):

    def __init__(self, business, username):
        super().__init__()
        self.business = business
        self.username = username
        self.title("IN450 Secure Viewer")
        self.geometry("650x450")
        self.configure(bg="#f6e6ff")

        tk.Label(
            self,
            text=f"Welcome, {self.username}",
            bg="#f6e6ff",
            fg="#5e3b8c",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        tk.Button(self, text="Count IN450a", command=self.show_a, bg="#d9b3ff", fg="black").pack(pady=5)
        tk.Button(self, text="Names IN450b", command=self.show_b, bg="#e6ccff", fg="black").pack(pady=5)
        tk.Button(self, text="Count IN450c", command=self.show_c, bg="#d9b3ff", fg="black").pack(pady=5)

        self.output = scrolledtext.ScrolledText(self, width=75, height=18)
        self.output.pack(pady=10)

    def show_a(self):
        try:
            result = self.business.get_row_count_in450a()
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, f"Row Count IN450a: {result}")
        except PermissionError as e:
            messagebox.showerror("Access Denied", str(e))

    def show_b(self):
        try:
            results = self.business.get_names_in450b()
            self.output.delete("1.0", tk.END)
            for first, last in results:
                self.output.insert(tk.END, f"{first} {last}\n")
        except PermissionError as e:
            messagebox.showerror("Access Denied", str(e))

    def show_c(self):
        try:
            result = self.business.get_row_count_in450c()
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, f"Row Count IN450c: {result}")
        except PermissionError as e:
            messagebox.showerror("Access Denied", str(e))


if __name__ == "__main__":
    LoginWindow().mainloop()

