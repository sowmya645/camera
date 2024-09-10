import tkinter as tk
from datetime import datetime

def calculate_age():
    birthdate_str = entry_birth_date.get()

    try:
        birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")

        current_date = datetime.now()

        x = current_date - birthdate
        years = x.days // 365
        months = (x.days % 365) // 30
        days = (x.days % 365) % 30
        hours, remainder = divmod(x.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        result_str = f"You are {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds old."
        label_result.config(text=result_str, fg="green")
        
    except ValueError:
        label_result.config(text="Invalid date format. Please use the format dd-mm-yyyy.", fg="red")  

main = tk.Tk()
main.title("Age Calculator")
main.configure(bg="Light Blue")  

label_instructions = tk.Label(main, font=('OCR A Extended', 25),text="AGE CALCULATOR \n Enter your birthdate (dd-mm-yyyy):", bg="Light Blue")
label_instructions.pack(pady=10)

entry_birth_date = tk.Entry(main, font='arial 12 bold', bg="Light Blue",fg="white")
entry_birth_date.pack(pady=10)

button_calculate = tk.Button(main, text="Calculate Age", command=calculate_age, bg="blue", fg="white") 
button_calculate.pack(pady=10)

label_result = tk.Label(main, font='arial 12 bold', text="", bg="Light Blue")
label_result.pack(pady=10)

main.mainloop()
