import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Error", "Weight and Height must be greater than 0.")
            return

        # Convert cm to meters
        height_m = height_cm / 100

        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif bmi < 25:
            category = "Normal Weight"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        result_label.config(
            text=f"BMI : {bmi:.2f}\nCategory : {category}",
            fg=color
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def clear():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="", fg="black")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")
root.configure(bg="lightblue")

title = tk.Label(root, text="BMI CALCULATOR",
                 font=("Arial", 18, "bold"),
                 bg="lightblue", fg="navy")
title.pack(pady=15)

tk.Label(root, text="Weight (kg)", font=("Arial", 12),
         bg="lightblue").pack()

weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

tk.Label(root, text="Height (cm)", font=("Arial", 12),
         bg="lightblue").pack()

height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

tk.Button(root, text="Calculate BMI",
          font=("Arial", 12),
          bg="green", fg="white",
          command=calculate_bmi).pack(pady=10)

tk.Button(root, text="Clear",
          font=("Arial", 12),
          bg="gray", fg="white",
          command=clear).pack()

result_label = tk.Label(root,
                        text="",
                        font=("Arial", 14, "bold"),
                        bg="lightblue")
result_label.pack(pady=20)

root.mainloop()