import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("kalkulator sederhana")
root.geometry("400x380")

ttk.Label(root, text="Calculator Sederhana").pack(padx=20,pady=10)
ttk.Label(root, text="Kalkulator Sederhana", font=("Helvetica", 14, "bold")).pack(padx=20, pady=10)

# Variabel penyimpan input/hasil
expression = ""

# Entry / Layar Tampilan Hasil
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Helvetica", 18), justify="right")
entry.pack(padx=20, pady=10, fill="x")
# FUNGSI LOGIKA KALKULATOR
def press(symbol):
    global expression
    expression += str(symbol)
    entry_var.set(expression)

def clear():
    global expression
    expression = ""
    entry_var.set("")

def calculate():
    global expression
    try:
        # Evaluasi matematika dari string
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except Exception:
        entry_var.set("Error")
        expression = ""
# LAYOUT BAWAH: Menggunakan GRID untuk Tombol-tombol (Grid Container)
frame_buttons = ttk.Frame(root)
frame_buttons.pack(padx=20, pady=10)

# Daftar tombol kalkulator
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

# Membuat tombol secara dinamis memakai GRID
for (text, row, col) in buttons:
    if text == '=':
        btn = ttk.Button(frame_buttons, text=text, command=calculate)
    elif text == 'C':
        btn = ttk.Button(frame_buttons, text=text, command=clear)
    else:
        btn = ttk.Button(frame_buttons, text=text, command=lambda t=text: press(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=5, ipady=5)

root.mainloop()