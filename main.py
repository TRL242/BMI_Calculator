from tkinter import *

bmi=0

window = Tk()
window.title("BMI Calculator")
window.config(padx=40, pady=40)

# height_input=float(input("Enter your height in centimeters:\n"))
# weight_input=float(input("Enter your Weight in Kg:  \n"))

def bmi_calculator():
    global bmi
    height_m = float(height_input_cm.get())/100
    bmi=round(float(weight_input_kg.get())/(height_m*height_m), 2)
    bmi_result_label.config(text=f"{bmi}")
    print(f"your Body Mass Index is {bmi} ")


def bmi_critique(bmi):
    #bmi = float(bmi.get())
    if(bmi>0):
        if(bmi<=16):
            bmi_critique_statement=("you are severely underweight")
        elif(bmi<=18.5):
            bmi_critique_statement=("you are underweight")
        elif(bmi<=25):
            bmi_critique_statement=("you are Healthy")
        elif(bmi<=30):
            bmi_critique_statement=("you are overweight")
        else: bmi_critique_statement=("you are severely overweight")
    else:bmi_critique_statement=("enter valid details")
    bmi_critique_result.config(text=f"{bmi_critique_statement}")

def print_critique():
    bmi_critique(bmi.get())
    
#bmi_critique(bmi)

height_input_cm = Entry(width=7)
height_input_cm.grid(column=1, row=0)

height_label_cm = Label(text="height(cm)")
height_label_cm.grid(column=2, row=0)

weight_input_kg = Entry(width=7)
weight_input_kg.grid(column=3, row=0)

weight_label_kg = Label(text="weight(kg)")
weight_label_kg.grid(column=4, row=0)

is_equal_label = Label(text="Is equal to a")
is_equal_label.grid(column=0, row=1)

bmi_result_label = Label(text="0")
bmi_result_label.grid(column=1, row=1)

bmi_label = Label(text="BMI")
bmi_label.grid(column=2, row=1)

bmi_critique_result = Label(text="None")
bmi_critique_result.grid(column=1, row=2)

bmi_critique_label = Label(text="BMI Citique")
bmi_critique_label.grid(column=2, row=2)

calculate_button = Button(text="Calculate",
                          command=lambda: [bmi_calculator(),bmi_critique(bmi)])
calculate_button.grid(column=1, row=4)


window.mainloop()