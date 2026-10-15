import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.resizable(False, False)

# Поле вывода
display = tk.Entry(root, font=("Arial", 22), justify="right", bd=8)
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")


def press(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def backspace():
    display.delete(len(display.get()) - 1, tk.END)


def calculate():
    expr = display.get()
    try:
        result = eval(expr)  # считает выражение из строки
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Ділення на 0")
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Помилка")


# Кнопки: (текст, строка, столбец)
buttons = [
    ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2),
]

for text, row, col in buttons:
    if text == "C":
        cmd = clear
    elif text == "⌫":
        cmd = backspace
    elif text == "=":
        cmd = calculate
    else:
        cmd = lambda t=text: press(t)

    span = 2 if text == "=" else 1
    tk.Button(root, text=text, font=("Arial", 16), width=5, height=2,
              command=cmd).grid(row=row, column=col, columnspan=span,
                                padx=2, pady=2, sticky="nsew")

root.mainloop()