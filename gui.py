import tkinter as tk
from tkinter import scrolledtext
from business_layer import BusinessLayer


class DataViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IN450 Data Viewer")
        self.root.configure(bg="#f6e6ff")


        self.business = BusinessLayer()

        self.btn_count = tk.Button(root, text="Get Row Count (in450a)", command=self.show_count,  bg="#d9b3ff", fg="black")
        self.btn_count.pack(pady=5)

        self.btn_names = tk.Button(root, text="Show Names (in450b)", command=self.show_names, bg="#e6ccff", fg="black")
        self.btn_names.pack(pady=5)

        self.output = scrolledtext.ScrolledText(root, width=80, height=20)
        self.output.pack(pady=10)

    def show_count(self):
        count = self.business.get_row_count_in450a()
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, f"Total Rows in in450a: {count}")

    def show_names(self):
        names = self.business.get_names_in450b()
        self.output.delete("1.0", tk.END)
        for first, last in names:
            self.output.insert(tk.END, f"{first} {last}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataViewerApp(root)
    root.mainloop()
