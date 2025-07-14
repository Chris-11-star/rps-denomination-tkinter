import tkinter as tk

root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x500")
root.config(bg="white")

denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

def calculate():
    amount = entry.get()
    result_text.delete("1.0", tk.END)
    if not amount.isdigit():
        result_text.insert(tk.END, "Enter a valid number.")
        return
    amount = int(amount)
    for denom in denominations:
        count = amount // denom
        if count:
            result_text.insert(tk.END, f"{denom} × {count}\n")
            amount = amount % denom
    if amount > 0:
        result_text.insert(tk.END, f"Remaining: {amount}")

title = tk.Label(root, text="Denomination Calculator", font=("Arial", 18), bg="white")
title.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

calc_btn = tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate)
calc_btn.pack(pady=10)

result_text = tk.Text(root, height=15, width=30, font=("Arial", 12))
result_text.pack(pady=10)

root.mainloop()
