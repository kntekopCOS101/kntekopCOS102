import tkinter as tk
from tkinter import messagebox

class Delivery():

    def __init__(self, location, weight, quantity):
        self.location = location
        self.weight = weight
        self.quantity = quantity
        self.cost = 0


    def pau(self):
        if self.weight >= 10:
            self.cost = 2000
        else:
            self.cost = 1500

    def Epe(self):
        if self.weight >= 10:
            self.cost = 5000
        else:
            self.cost = 4000

    def total(self):
        total = self.cost * self.quantity
        messagebox.showinfo("Total cost", f"The total cose id {total}")


def calculate_total():
    location = location_entry.get()
    try:
        weight = float(weight_entry.get())
        quantity = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and quantity.")
        return

    delivery = Delivery(location, weight, quantity)

    if location.lower() == "pau":
        delivery.pau()
    elif location.lower() == "epe":
        delivery.Epe()
    else:
        messagebox.showerror("Location Error", "Location must be either 'PAU' or 'Epe'")
        return

    delivery.total()


# GUI code
window = tk.Tk()
window.title("Delivery Cost Calculator")

tk.Label(window, text="Enter delivery location (PAU or Epe):").pack(pady=5)
location_entry = tk.Entry(window)
location_entry.pack()

tk.Label(window, text="Enter package weight (kg):").pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Enter number of packages:").pack(pady=5)
quantity_entry = tk.Entry(window)
quantity_entry.pack()

tk.Button(window, text="Calculate Total Cost", command=calculate_total).pack(pady=20)

window.mainloop()
    

