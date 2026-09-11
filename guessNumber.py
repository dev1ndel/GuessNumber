import tkinter as tk
import random

secret = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="Введи целое число!", fg="red")
        return

    if not 1 <= guess <= 100:
        result_label.config(text="Число должно быть от 1 до 100", fg="red")
        return

    attempts += 1

    if guess < secret:
        result_label.config(text=f"{guess} — меньше. Пробуй ещё!", fg="blue")
    elif guess > secret:
        result_label.config(text=f"{guess} — больше. Пробуй ещё!", fg="blue")
    else:
        result_label.config(
            text=f"🎉 Угадал! Это {secret}. Попыток: {attempts}",
            fg="green"
        )
        button.config(state="disabled")
        entry.config(state="disabled")
        restart_button.pack(pady=5)

    entry.delete(0, tk.END)
    entry.focus()

def restart():
    global secret, attempts
    secret = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Новая игра! Введи число.", fg="black")
    button.config(state="normal")
    entry.config(state="normal")
    entry.delete(0, tk.END)
    restart_button.pack_forget()
    entry.focus()

root = tk.Tk()
root.title("Угадай число")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Угадай число от 1 до 100",
         font=("Arial", 14, "bold")).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)
entry.focus()

button = tk.Button(root, text="Проверить", command=check_guess,
                   font=("Arial", 12), width=15)
button.pack(pady=5)

root.bind("<Return>", lambda event: check_guess())

result_label = tk.Label(root, text="Введи число и нажми «Проверить»",
                        font=("Arial", 11), wraplength=300)
result_label.pack(pady=15)

restart_button = tk.Button(root, text="Играть снова", command=restart,
                           font=("Arial", 12), width=15)

root.mainloop()
