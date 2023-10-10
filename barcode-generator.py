import tkinter as tk
from tkinter import ttk
import barcode
from barcode.writer import ImageWriter

class BarcodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barcode Generator")

        # 输入框
        self.label_data = ttk.Label(root, text="Enter Data:")
        self.label_data.grid(column=0, row=0, pady=10)
        self.entry_data = ttk.Entry(root, width=30)
        self.entry_data.grid(column=1, row=0, pady=10)

        self.label_dpi = ttk.Label(root, text="Enter DPI:")
        self.label_dpi.grid(column=0, row=1, pady=10)
        self.entry_dpi = ttk.Entry(root, width=10)
        self.entry_dpi.grid(column=1, row=1, pady=10)

        self.label_name = ttk.Label(root, text="Enter File Name:")
        self.label_name.grid(column=0, row=2, pady=10)
        self.entry_name = ttk.Entry(root, width=10)
        self.entry_name.grid(column=1, row=2, pady=10)
        # 生成按钮
        self.button = ttk.Button(root, text="Generate Barcode", command=self.generate_barcode)
        self.button.grid(column=1, row=4, pady=10)

    def generate_barcode(self):
        data = self.entry_data.get()
        dpi = int(self.entry_dpi.get())
        name = str(self.entry_name.get())
        if data:
            code = barcode.get_barcode_class('code128')
            code_instance = code(data, writer=ImageWriter())
            code_instance.save(name, {"dpi":dpi})
            ttk.Label(self.root, text="Barcode generated successfully!").grid(column=1, row=3)
        else:
            ttk.Label(self.root, text="Please enter data!").grid(column=1, row=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = BarcodeGeneratorApp(root)
    root.mainloop()