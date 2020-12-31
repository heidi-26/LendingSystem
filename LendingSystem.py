from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


# Author: Alexander Caones

def hi():
    print("Helooooooooooooooooooo")


def calculation():
    new_win = Toplevel(root)
    new_win.geometry("400x100")
    new_win.title("Calculation")

    mybutton = Button(new_win, text="HI", font=(
        "Arial", 10), command=hi).pack()


def Button_monthly():
    n = ent1.get()
    a = ent2.get()
    l = ent3.get()
    cb = combo_Box.get()

    if n == "" and l == "":
        messagebox.showerror("Error", "Please fill both name and loan amount")
    elif (int(l) > 1000000):
        messagebox.showerror(
            "Error", "Please enter amount, P1 - P1,000,000 only")
    else:
        try:
            l = int(l)
            my_name = Label(root, text="Name: ", font=("Arial", 10, "bold"))
            my_name.grid(row=16, sticky=W)
            my_name_result = Label(root, text=n, font=("Arial", 10))
            my_name_result.grid(row=16, column=1, sticky=W)

            my_address = Label(root, text="Address: ",
                               font=("Arial", 10, "bold"))
            my_address.grid(row=17, sticky=W)
            my_address_r = Label(root, text=a, font=("Arial", 10))
            my_address_r.grid(row=17, column=1, sticky=W)

            my_loan_amount = Label(
                root, text="Loan Amount: ", font=("Arial", 10, "bold"))
            my_loan_amount.grid(row=18, sticky=W)
            my_loan_amount_result = Label(root, text=l, font=("Arial", 10))
            my_loan_amount_result.grid(row=18, column=1, sticky=W)

            my_combo_Box = Label(root, text="Terms: ",
                                 font=("Arial", 10, "bold"))
            my_combo_Box.grid(row=19, sticky=W)
            my_combo_box_result = Label(root, text=cb, font=("Arial", 10))
            my_combo_box_result.grid(row=19, column=1, sticky=W)

            my_top = Label(root, text="TOP: ", font=("Arial", 10, "bold"))
            my_top.grid(row=20, sticky=W)

            my_t = Label(root, text="Monthly Interest", font=("Arial", 10))
            my_t.grid(row=20, column=1, sticky=W)

            my_interest = Label(root, text="Interest",
                                font=("Arial", 10, "bold"))
            my_interest.grid(row=21, sticky=W)

            process_button = Button(
                root, text="Calculation", font="Arial, 10", fg="white", bg="Green", command=calculation)
            process_button.grid(row=22, column=1, sticky=W)

            l = int(ent3.get())
            if l <= 50000:
                my_button_submit1 = Label(root, text="5%", font=("Arial", 10))
                my_button_submit1.grid(row=21, column=1, sticky=W)
            elif l >= 50001 and l <= 500000:
                my_button_submit1 = Label(root, text="6%", font=("Arial", 10))
                my_button_submit1.grid(row=21, column=1, sticky=W)
            elif l >= 500001 and l <= 1000000:
                my_button_submit1 = Label(root, text="7%", font=("Arial", 10))
                my_button_submit1.grid(row=21, column=1, sticky=W)

        except ValueError:
            messagebox.showerror(
                "Error", "Only digits are allowed in loan amount field")


def Button_quarterly():
    n = ent1.get()
    a = ent2.get()
    l = ent3.get()
    cb = combo_Box.get()

    if n == "" and l == "":
        messagebox.showerror("Error", "Please fill both name and loan amount")
    else:
        try:
            l = int(l)
            my_name = Label(root, text="Name: ", font=("Arial", 10, "bold"))
            my_name.grid(row=16, sticky=W)
            my_name_result = Label(root, text=n, font=("Arial", 10))
            my_name_result.grid(row=16, column=1, sticky=W)

            my_address = Label(root, text="Address: ",
                               font=("Arial", 10, "bold"))
            my_address.grid(row=17, sticky=W)
            my_address_r = Label(root, text=a, font=("Arial", 10))
            my_address_r.grid(row=17, column=1, sticky=W)

            my_loan_amount = Label(
                root, text="Loan Amount: ", font=("Arial", 10, "bold"))
            my_loan_amount.grid(row=18, sticky=W)
            my_loan_amount_result = Label(root, text=l, font=("Arial", 10))
            my_loan_amount_result.grid(row=18, column=1, sticky=W)

            my_combo_Box = Label(root, text="Terms: ",
                                 font=("Arial", 10, "bold"))
            my_combo_Box.grid(row=19, sticky=W)
            my_combo_box_result = Label(root, text=cb, font=("Arial", 10))
            my_combo_box_result.grid(row=19, column=1, sticky=W)

            my_top = Label(root, text="TOP: ", font=("Arial", 10, "bold"))
            my_top.grid(row=20, sticky=W)

            my_t = Label(root, text="Quarterly Interest", font=("Arial", 10))
            my_t.grid(row=20, column=1, sticky=W)

            my_interest = Label(root, text="Interest",
                                font=("Arial", 10, "bold"))
            my_interest.grid(row=21, sticky=W)

            process_button = Button(
                root, text="Calculation", font="Arial, 10", fg="white", bg="Green", command=calculation)
            process_button.grid(row=22, column=1, sticky=W)

            l = int(ent3.get())
            if l <= 1000:
                my_button_submit2 = Label(
                    root, text="No interest", font=("Arial", 10))
                my_button_submit2.grid(row=21, column=1, sticky=W)
            elif l >= 1001 and l <= 50000:
                my_button_submit2 = Label(root, text="16%", font=("Arial", 10))
                my_button_submit2.grid(row=21, column=1, sticky=W)
            elif l >= 50001 and l <= 500000:
                my_button_submit2 = Label(root, text="17%", font=("Arial", 10))
                my_button_submit2.grid(row=21, column=1, sticky=W)
            elif l >= 500001 and l <= 1000000:
                my_button_submit2 = Label(root, text="18%", font=("Arial", 10))
                my_button_submit2.grid(row=21, column=1, sticky=W)

        except ValueError:
            messagebox.showerror(
                "Error", "Only digits are allowed in loan amount field")


def Button_semi():
    n = ent1.get()
    a = ent2.get()
    l = ent3.get()
    cb = combo_Box.get()

    if n == "" and l == "":
        messagebox.showerror("Error", "Please fill both name and loan amount")
    else:
        try:
            l = int(l)
            my_name = Label(root, text="Name: ", font=("Arial", 10, "bold"))
            my_name.grid(row=16, sticky=W)
            my_name_result = Label(root, text=n, font=("Arial", 10))
            my_name_result.grid(row=16, column=1, sticky=W)

            my_address = Label(root, text="Address: ",
                               font=("Arial", 10, "bold"))
            my_address.grid(row=17, sticky=W)
            my_address_r = Label(root, text=a, font=("Arial", 10))
            my_address_r.grid(row=17, column=1, sticky=W)

            my_loan_amount = Label(
                root, text="Loan Amount: ", font=("Arial", 10, "bold"))
            my_loan_amount.grid(row=18, sticky=W)
            my_loan_amount_result = Label(root, text=l, font=("Arial", 10))
            my_loan_amount_result.grid(row=18, column=1, sticky=W)

            my_combo_Box = Label(root, text="Terms: ",
                                 font=("Arial", 10, "bold"))
            my_combo_Box.grid(row=19, sticky=W)
            my_combo_box_result = Label(root, text=cb, font=("Arial", 10))
            my_combo_box_result.grid(row=19, column=1, sticky=W)

            my_top = Label(root, text="TOP: ", font=("Arial", 10, "bold"))
            my_top.grid(row=20, sticky=W)

            my_t = Label(root, text="Semi-Annual Interest", font=("Arial", 10))
            my_t.grid(row=20, column=1, sticky=W)

            my_interest = Label(root, text="Interest",
                                font=("Arial", 10, "bold"))
            my_interest.grid(row=21, sticky=W)

            l = int(ent3.get())
            if l <= 1000:
                my_button_submit3 = Label(
                    root, text="No interest", font=("Arial", 10))
                my_button_submit3.grid(row=21, column=1, sticky=W)
            elif l >= 1001 and l <= 10000:
                my_button_submit3 = Label(
                    root, text="No interest", font=("Arial", 10))
                my_button_submit3.grid(row=21, column=1, sticky=W)
            elif l >= 10001 and l <= 100000:
                my_button_submit3 = Label(root, text="19%", font=("Arial", 10))
                my_button_submit3.grid(row=21, column=1, sticky=W)
            elif l >= 100001 and l <= 500000:
                my_button_submit3 = Label(root, text="20%", font=("Arial", 10))
                my_button_submit3.grid(row=21, column=1, sticky=W)
            elif l >= 500001 and l <= 1000000:
                my_button_submit3 = Label(root, text="21%", font=("Arial", 10))
                my_button_submit3.grid(row=21, column=1, sticky=W)

            process_button = Button(
                root, text="Calculation", font="Arial, 10", fg="white", bg="Green", command=calculation)
            process_button.grid(row=22, column=1, sticky=W)

        except ValueError:
            messagebox.showerror(
                "Error", "Only digits are allowed in loan amount field")


def Button_annual():
    n = ent1.get()
    a = ent2.get()
    l = ent3.get()
    cb = combo_Box.get()

    if n == "" and l == "":
        messagebox.showerror("Error", "Please fill both name and loan amount")
    else:
        try:
            l = int(l)
            my_name = Label(root, text="Name: ", font=("Arial", 10, "bold"))
            my_name.grid(row=16, sticky=W)
            my_name_result = Label(root, text=n, font=("Arial", 10))
            my_name_result.grid(row=16, column=1, sticky=W)

            my_address = Label(root, text="Address: ",
                               font=("Arial", 10, "bold"))
            my_address.grid(row=17, sticky=W)
            my_address_r = Label(root, text=a, font=("Arial", 10))
            my_address_r.grid(row=17, column=1, sticky=W)

            my_loan_amount = Label(
                root, text="Loan Amount: ", font=("Arial", 10, "bold"))
            my_loan_amount.grid(row=18, sticky=W)
            my_loan_amount_result = Label(root, text=l, font=("Arial", 10))
            my_loan_amount_result.grid(row=18, column=1, sticky=W)

            my_combo_Box = Label(root, text="Terms: ",
                                 font=("Arial", 10, "bold"))
            my_combo_Box.grid(row=19, sticky=W)
            my_combo_box_result = Label(root, text=cb, font=("Arial", 10))
            my_combo_box_result.grid(row=19, column=1, sticky=W)

            my_top = Label(root, text="TOP: ", font=("Arial", 10, "bold"))
            my_top.grid(row=20, sticky=W)

            my_t = Label(root, text="Annually Interest", font=("Arial", 10))
            my_t.grid(row=20, column=1, sticky=W)

            my_interest = Label(root, text="Interest",
                                font=("Arial", 10, "bold"))
            my_interest.grid(row=21, sticky=W)

            process_button = Button(
                root, text="Calculation", font="Arial, 10", fg="white", bg="Green", command=calculation)
            process_button.grid(row=22, column=1, sticky=W)

            l = int(ent3.get())
            if l <= 1000:
                my_button_submit4 = Label(
                    root, text="No interest", font=("Arial", 10))
                my_button_submit4.grid(row=21, column=1, sticky=W)
            elif l >= 1001 and l <= 10000:
                my_button_submit4 = Label(
                    root, text="No interest", font=("Arial", 10))
                my_button_submit4.grid(row=21, column=1, sticky=W)
            elif l >= 10001 and l <= 50000:
                my_button_submit4 = Label(
                    root, text="No interest", font=("Arial", 10))
                my_button_submit4.grid(row=21, column=1, sticky=W)
            elif l >= 50001 and l <= 100000:
                my_button_submit4 = Label(root, text="27%", font=("Arial", 10))
                my_button_submit4.grid(row=21, column=1, sticky=W)
            elif l >= 100001 and l <= 500000:
                my_button_submit4 = Label(root, text="29%", font=("Arial", 10))
                my_button_submit4.grid(row=21, column=1, sticky=W)
            elif l >= 500001 and l <= 1000000:
                my_button_submit4 = Label(root, text="30%", font=("Arial", 10))
                my_button_submit4.grid(row=21, column=1, sticky=W)

        except ValueError:
            messagebox.showerror(
                "Error", "Only digits are allowed in loan amount field")


"""  
   if t == "MONTHLY" and z <= 50000:
        my_button_submit1 = Label(root, text="5%", font=("Arial", 10))
        my_button_submit1.grid(row=19, column=1, sticky=W)
    elif z >= 50001 and z <= 500000:
        my_button_submit1 = Label(root, text="6%", font=("Arial", 10))
        my_button_submit1.grid(row=19, column=1, sticky=W)
    elif z >= 500001 and z <= 1000000:
        my_button_submit1 = Label(root, text="7%", font=("Arial", 10))
        my_button_submit1.grid(row=19, column=1, sticky=W)
"""

"""

def calculation():
    pass


def button():
    n = name.get()
    l = loan_Ammount.get()
    t = s.get()
    ct = combobox_terms.get()

    if n == "" or l == "":
        messagebox.showerror("Error", "Please fill both name and loan amount")

    elif ct == "":
        messagebox.showerror("Error", "Please enter how many months you want to pay your borrowed money")
    else:
        try:
            l = int(l)
        except ValueError:
            messagebox.showerror("Error", "Only digits are allowed in loan amount field")

    x = loan_Amount.get()
    if (int(x) > 1000000):
        messagebox.showerror("Error", "Please enter amount, P1 - P1,000,000 only")
    else:
        l1 = Label(root, text="Name: ", font=("Arial", 10, "bold"))
        l2 = Label(root, text="Address: ", font=("Arial", 10, "bold"))
        l3= Label(root, text="Loan Amount: ", font=("Arial", 10, "bold"))
        my_value = Label(root, text="TOP: ", font=("Arial", 10, "bold"))
        l4 = Label(root, text="Terms: ", font=("Arial", 10, "bold"))
        my_interest = Label(root, text="Interest: ", font=("Arial", 10, "bold"))

        l1.grid(row=14, column=0, sticky=W)
        l2.grid(row=15, column=0, sticky=W)
        l3.grid(row=16, column=0, sticky=W)
        my_value.grid(row=17, column=0, sticky=W)
        l4.grid(row=18, column=0, sticky=W)
        my_interest.grid(row=19, column=0, sticky=W)

        r_l1 = Label(root, text=n, font=("Arial", 10))
        r_l2 = Label(root, text=address_ent2.get(), font=("Arial", 10))
        r_l3 = Label(root, text=l, font=("Arial", 10))
        r_my_value = Label(root, text=t, font=("Arial", 10))
        r_l4 = Label(root, text=ct, font=("Arial", 10))

        r_l1.grid(row=14, column=1, sticky=W)
        r_l2.grid(row=15, column=1, sticky=W)
        r_l3.grid(row=16, column=1, sticky=W)
        r_my_value.grid(row=17, column=1, sticky=W)
        r_l4.grid(row=18, column=1, sticky=W)

    z = int(loan_Amount.get())
    if t == "MONTHLY" and z <= 50000:
        my_button_submit1 = Label(root, text="5%", font=("Arial", 10))
        my_button_submit1.grid(row=19, column=1, sticky=W)
    elif z >= 50001 and z <= 500000:
        my_button_submit1 = Label(root, text="6%", font=("Arial", 10))
        my_button_submit1.grid(row=19, column=1, sticky=W)
    elif z >= 500001 and z <= 1000000:
        my_button_submit1 = Label(root, text="7%", font=("Arial", 10))
        my_button_submit1.grid(row=19, column=1, sticky=W)

    if t == "QUARTERLY" and z <= 1000:
        my_button_submit2 = Label(root, text="No interest", font=("Arial", 10))
        my_button_submit2.grid(row=19, column=1, sticky=W)
    elif z >= 1001 and z <= 50000:
        my_button_submit2 = Label(root, text="16%", font=("Arial", 10))
        my_button_submit2.grid(row=19, column=1, sticky=W)
    elif z >= 50001 and z <= 500000:
        my_button_submit2 = Label(root, text="17%", font=("Arial", 10))
        my_button_submit2.grid(row=19, column=1, sticky=W)
    elif z >= 500001 and z <= 1000000:
        my_button_submit2 = Label(root, text="18%", font=("Arial", 10))
        my_button_submit2.grid(row=19, column=1, sticky=W)

    if t == "Semi-Annual" and z <= 1000:
        my_button_submit3 = Label(root, text="No interest", font=("Arial", 10))
        my_button_submit3.grid(row=19, column=1, sticky=W)
    elif z >= 1001 and z <= 10000:
        my_button_submit3 = Label(root, text="No interest", font=("Arial", 10))
        my_button_submit3.grid(row=19, column=1, sticky=W)
    elif z >= 10001 and z <= 100000:
        my_button_submit3 = Label(root, text="19%", font=("Arial", 10))
        my_button_submit3.grid(row=19, column=1, sticky=W)
    elif z >= 100001 and z <= 500000:
        my_button_submit3 = Label(root, text="20%", font=("Arial", 10))
        my_button_submit3.grid(row=19, column=1, sticky=W)
    elif z >= 500001 and z <= 1000000:
        my_button_submit3 = Label(root, text="21%", font=("Arial", 10))
        my_button_submit3.grid(row=19, column=1, sticky=W)

    if t == "ANNUALLY" and z <= 1000:
        my_button_submit4 = Label(root, text="No interest", font=("Arial", 10))
        my_button_submit4.grid(row=19, column=1, sticky=W)
    elif z >= 1001 and z <= 10000:
        my_button_submit4 = Label(root, text="No interest", font=("Arial", 10))
        my_button_submit4.grid(row=19, column=1, sticky=W)
    elif z >= 10001 and z <= 50000:
        my_button_submit4 = Label(root, text="No interest", font=("Arial", 10))
        my_button_submit4.grid(row=19, column=1, sticky=W)
    elif z >= 50001 and z <= 100000:
        my_button_submit4 = Label(root, text="27%", font=("Arial", 10))
        my_button_submit4.grid(row=19, column=1, sticky=W)
    elif z >= 100001 and z <= 500000:
        my_button_submit4 = Label(root, text="29%", font=("Arial", 10))
        my_button_submit4.grid(row=19, column=1, sticky=W)
    elif z >= 500001 and z <= 1000000:
        my_button_submit4 = Label(root, text="30%", font=("Arial", 10))
        my_button_submit4.grid(row=19, column=1, sticky=W)

    process_button = Button(root, text="Calculation", font="Arial, 10", fg="white", bg="Green", command=calculation)
    process_button.grid(row=20, column=1, sticky=W)"""


root = Tk()
root.title("XYZ Lending System")
root.geometry("1000x1000")

level1 = Label(root, text="AMOUNT MATRIX", font=("Broadway", 14, "bold"))
level2 = Label(root, text="""AMOUNT TO BORROW
\n
P 1000 below
P 1,001 - P 10,000
P 10,001 - P 50,000
P 50,500 - P 100,000
P 100,001 - P 500,000
P 500,001 - P 1,000,000

""", font=("Arial", 10, "bold"))

level3 = Label(root, text="""MONTHLY \n INTEREST

5%
5%
5%
6%
6%
7%

""", font=("Arial", 10, "bold"))

level4 = Label(root, text="""QUARTERLY \n INTEREST

.....
16%
16%
17%
17%
18%

""", font=("Arial", 10, "bold"))

level5 = Label(root, text="""SEMI-ANNUAL \n INTEREST

.....
.....
19%
19%
20%
21%

""", font=("Arial", 10, "bold"))

level6 = Label(root, text="""ANNUAL \n INTEREST

.....
.....
.....
27%
29%
30%

""", font=("Arial", 10, "bold"))

level1.grid(row=0, column=1, pady=30)
level2.grid(row=1, column=0, pady=30)
level3.grid(row=1, column=1, pady=30)
level4.grid(row=1, column=2, pady=30)
level5.grid(row=1, column=3, pady=30)
level6.grid(row=1, column=4, pady=30)


l1 = Label(root, text="NAME: ", font=("Arial", 10, "bold"))
l2 = Label(root, text="ADDRESS: ", font=("Arial", 10, "bold"))
l3 = Label(root, text="LOAN AMOUNT: ", font=("Arial", 10, "bold"))
l4 = Label(root, text="TERMS: ", font=("Arial", 10, "bold"))

ent1 = Entry(root, width=50)
ent2 = Entry(root, width=50)
ent3 = Entry(root, width=50)
combo_Box = Combobox(root, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                                   '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'], width=30)

l1.grid(row=5, sticky=W)
l2.grid(row=6, sticky=W)
l3.grid(row=7, sticky=W)
l4.grid(row=8, sticky=W)


ent1.grid(row=5, column=1, sticky=W)
ent2.grid(row=6, column=1, sticky=W)
ent3.grid(row=7, column=1, sticky=W)
combo_Box.grid(row=8, column=1, sticky=W)

my_value = Label(root, text="TERMS OF PAYMENT: ", font=("Arial", 10, "bold"))
my_value.grid(row=9, column=1, sticky=W)

my_button_submit1 = Button(root, text="MONTHLY", font="Arial, 10",
                           bd=3, width=20, background="BLUE", fg="white",
                           command=Button_monthly)
my_button_submit1.grid(row=10, column=0)

my_button_submit2 = Button(root, text="QUARTERLY", font="Arial, 10",
                           bd=3, width=20, background="BLUE", fg="white",
                           command=Button_quarterly)
my_button_submit2.grid(row=10, column=2)

my_button_submit3 = Button(root, text="SEMI-ANNUAL", font="Arial, 10",
                           bd=3, width=20, background="BLUE", fg="white",
                           command=Button_semi)
my_button_submit3.grid(row=11, column=0)

my_button_submit4 = Button(root, text="ANNUALLY", font="Arial, 10",
                           bd=3, width=20, background="BLUE", fg="white",
                           command=Button_annual)
my_button_submit4.grid(row=11, column=2)


root.mainloop()
