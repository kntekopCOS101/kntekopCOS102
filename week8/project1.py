import tkinter as tk
from tkinter import messagebox
import random

class Employee():
    employee_name = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones" , "Nicole Anide", "Kosi Korso",
                   "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]

    employee_tasks = ["Loading", "Transporting", "Reviewing orders", "Customer service", "Delievering items"]    
    def __init__(self, name):
        self.name = name
        self.attendance = False
        self.task = None

    def check_employee(self):
        if self.name in Employee.employee_name:
            return True
        else:
            self.refuse_access() 
        
    def take_attendance(self):
        if self.attendance == True:
            print(f"{self.name} has marked attendance for today")
        else:
            self.attendance = True
            print(f"Attendance for {self.name} as been marked as present")


    def assign_task(self):
        if self.attendance == True:
            task = random.choice(Employee.employee_tasks)
            print(f"The task assigned to you, {self.name} is {task}")
        else:
            print("Cannot assign task")  

    def refuse_access(self):
        print("Access denied ")



def show_name():
    name = name_entry.get()
    emp = Employee(name)
    if emp.check_employee():
        emp.take_attendance()
        emp.assign_task()        
        
window = tk.Tk()
window.title("Attendance loop")

tk.Label(window, text="Enter your full name:").pack(pady=10)
name_entry = tk.Entry(window, width=40)
name_entry.pack()

tk.Button(window, text="Submit", command=submit_name).pack(pady=20)

window.mainloop()

