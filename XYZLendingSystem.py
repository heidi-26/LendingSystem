from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


def hi():
    print("Helooooooooooooooooooo")


def calculation(term_of_payment="Monthly"):
    new_win = Toplevel(root)
    new_win.geometry("400x300")
    new_win.title("Calculation")

    mybutton = Button(new_win, text="HI", font=(
        "Arial", 10), command=hi).pack()


MONTHLY = "Monthly"
QUARTERLY = "Quarterly"
SEMI_ANNUAL = "Semi-annual"
ANNUAL = 'Annual'


def terms_of_payment(term_of_payment=MONTHLY):
    name_value_field = name_field.get()
    address_value_field = address_field.get()
    loan_amount_value_field = int(loan_amount_field.get())
    term_value_combo = term_combo_box.get()
    if name_value_field == "" and loan_amount_value_field == "":
        messagebox.showerror(
            "Error", "Please fill both name and loan amount")
    elif (int(loan_amount_value_field) > 1000000):
        messagebox.showerror(
            "Error", "Please enter amount, P1 - P1,000,000 only")

    for grid_num in range(16, 22):
        for col_num in range(2):
            output_label = ""
            fontSettings = ("Arial", 10, "bold")
            stickyPos = W
            if grid_num == 16 and col_num == 0:
                output_label = "Name: "
            elif grid_num == 16 and col_num == 1:
                output_label = name_value_field
                fontSettings = ("Arial", 10)
                # output_label_component = Label(
                #     root, text=output_label, font=fontSettings)
                # output_label_component.grid(
                #     row=grid_num, column=col_num, sticky=stickyPos)
            elif grid_num == 17 and col_num == 0:
                output_label = "Address: "
            elif grid_num == 17 and col_num == 1:
                output_label = address_value_field
                fontSettings = ("Arial", 10)
            elif grid_num == 18 and col_num == 0:
                output_label = "Loan Amount: "
            elif grid_num == 18 and col_num == 1:
                output_label = loan_amount_value_field
                fontSettings = ("Arial", 10)
            elif grid_num == 19 and col_num == 0:
                output_label = "Terms: "
            elif grid_num == 19 and col_num == 1:
                output_label = term_value_combo
                fontSettings = ("Arial", 10)
            elif grid_num == 20 and col_num == 0:
                output_label = "TOP: "
            elif grid_num == 20 and col_num == 1:
                output_label = f"{term_of_payment} Interest"
                fontSettings = ("Arial", 10)
            elif grid_num == 21 and col_num == 0:
                output_label = "Interest: "
            elif grid_num == 21 and col_num == 1:
                if term_of_payment == MONTHLY:
                    if loan_amount_value_field <= 50000:
                        output_label = "5%"
                    elif loan_amount_value_field >= 50001 and loan_amount_value_field <= 500000:
                        output_label = "6%"
                    elif loan_amount_value_field >= 500001 and loan_amount_value_field <= 1000000:
                        output_label = "7%"
                if term_of_payment == QUARTERLY:
                    if loan_amount_value_field <= 1000:
                        output_label = "No interest"
                    elif loan_amount_value_field >= 1001 and loan_amount_value_field <= 50000:
                        output_label = "16%"
                    elif loan_amount_value_field >= 50001 and loan_amount_value_field <= 500000:
                        output_label = "17%"
                    elif loan_amount_value_field >= 500001 and loan_amount_value_field <= 1000000:
                        output_label = "18%"
                if term_of_payment == SEMI_ANNUAL:
                    if loan_amount_value_field <= 1000 or (loan_amount_value_field >= 1001 and loan_amount_value_field <= 10000):
                        output_label = "No Interest"
                    elif loan_amount_value_field >= 10001 and loan_amount_value_field <= 100000:
                        output_label = "19%"
                    elif loan_amount_value_field >= 100001 and loan_amount_value_field <= 500000:
                        output_label = "20%"
                    elif loan_amount_value_field >= 500001 and loan_amount_value_field <= 1000000:
                        output_label = "21%"
                if term_of_payment == ANNUAL:
                    if loan_amount_value_field <= 1000 or (loan_amount_value_field >= 1001 and loan_amount_value_field <= 10000) or (loan_amount_value_field >= 10001 and loan_amount_value_field <= 50000):
                        output_label = "No Interest"
                    elif loan_amount_value_field >= 50001 and loan_amount_value_field <= 100000:
                        output_label = "27%"
                    elif loan_amount_value_field >= 100001 and loan_amount_value_field <= 500000:
                        output_label = "29%"
                    elif loan_amount_value_field >= 500001 and loan_amount_value_field <= 1000000:
                        output_label = "30%"

                fontSettings = ("Arial", 10)

            output_label_component = Label(
                root, text=output_label, font=fontSettings)
            output_label_component.grid(
                row=grid_num, column=col_num, sticky=stickyPos)

    calculation_button = Button(
        root, text="Calculation", font="Arial, 10", fg="white", bg="Green", command=lambda: calculation(term_of_payment))
    calculation_button.grid(row=22, column=1, sticky=W)


root = Tk()
root.title("XYZ Lending System")
root.geometry("1000x1000")

amount_matrix_label = Label(
    root, text="AMOUNT MATRIX", font=("Broadway", 14, "bold"))
amount_to_borrow_col = Label(root, text="""AMOUNT TO BORROW
\n
P 1000 below
P 1,001 - P 10,000
P 10,001 - P 50,000
P 50,500 - P 100,000
P 100,001 - P 500,000
P 500,001 - P 1,000,000

""", font=("Arial", 10, "bold"))

monthly_interest_col = Label(root, text="""MONTHLY \n INTEREST

5%
5%
5%
6%
6%
7%

""", font=("Arial", 10, "bold"))

quarterly_interest_col = Label(root, text="""QUARTERLY \n INTEREST

.....
16%
16%
17%
17%
18%

""", font=("Arial", 10, "bold"))

semi_annual_interest_col = Label(root, text="""SEMI-ANNUAL \n INTEREST

.....
.....
19%
19%
20%
21%

""", font=("Arial", 10, "bold"))

annual_interest_col = Label(root, text="""ANNUAL \n INTEREST

.....
.....
.....
27%
29%
30%

""", font=("Arial", 10, "bold"))

amount_matrix_label.grid(row=0, column=1, pady=30)
amount_to_borrow_col.grid(row=1, column=0, pady=30)
monthly_interest_col.grid(row=1, column=1, pady=30)
quarterly_interest_col.grid(row=1, column=2, pady=30)
semi_annual_interest_col.grid(row=1, column=3, pady=30)
annual_interest_col.grid(row=1, column=4, pady=30)


name_label = Label(root, text="NAME: ", font=("Arial", 10, "bold"))
address_label = Label(root, text="ADDRESS: ", font=("Arial", 10, "bold"))
loan_amount_label = Label(root, text="LOAN AMOUNT: ",
                          font=("Arial", 10, "bold"))
terms_label = Label(root, text="TERMS: ", font=("Arial", 10, "bold"))

name_field = Entry(root, width=50)
address_field = Entry(root, width=50)
loan_amount_field = Entry(root, width=50)
term_combo_box = Combobox(root, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                                        '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'], width=30)

name_label.grid(row=5, sticky=W)
address_label.grid(row=6, sticky=W)
loan_amount_label.grid(row=7, sticky=W)
terms_label.grid(row=8, sticky=W)


name_field.grid(row=5, column=1, sticky=W)
address_field.grid(row=6, column=1, sticky=W)
loan_amount_field.grid(row=7, column=1, sticky=W)
term_combo_box.grid(row=8, column=1, sticky=W)

terms_of_payment_label = Label(
    root, text="TERMS OF PAYMENT: ", font=("Arial", 10, "bold"))
terms_of_payment_label.grid(row=9, column=1, sticky=W)

monthly_button = Button(root, text="MONTHLY", font="Arial, 10",
                        bd=3, width=20, background="BLUE", fg="white",
                        command=lambda: terms_of_payment(MONTHLY))

monthly_button.grid(row=10, column=0)

quarterly_button = Button(root, text="QUARTERLY", font="Arial, 10",
                          bd=3, width=20, background="BLUE", fg="white",
                          command=lambda: terms_of_payment(QUARTERLY))
quarterly_button.grid(row=10, column=2)

semi_annual_button = Button(root, text="SEMI-ANNUAL", font="Arial, 10",
                            bd=3, width=20, background="BLUE", fg="white",
                            command=lambda: terms_of_payment(SEMI_ANNUAL))
semi_annual_button.grid(row=11, column=0)

annual_button = Button(root, text="ANNUALLY", font="Arial, 10",
                       bd=3, width=20, background="BLUE", fg="white",
                       command=lambda: terms_of_payment(ANNUAL))
annual_button.grid(row=11, column=2)


root.mainloop()
