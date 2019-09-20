import tkinter as tk
from tkinter import messagebox


class Calculator:

    def action(self, arg):
        self.entry.insert(tk.END, arg)

    def replace_symbol(self):
        expression = self.entry.get()
        new_exp = expression.replace('÷', '/') # replacing ÷ by / and x by * 
        new_exp = new_exp.replace('X', '*')
        return new_exp

    def equal(self):
        new_exp = self.replace_symbol()
        try:
            value = eval(new_exp)
        except SyntaxError or NameError:
            self.entry.delete(0, tk.END)
            # self.entry.insert(0, 'Invalid Input!')
            messagebox.showerror("Error", "Invalid Input!")
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, value)

    def enter_key(self, e):
        new_exp = self.replace_symbol()
        try:
            value = eval(new_exp)
        except SyntaxError or NameError:
            self.entry.delete(0, tk.END)
            # self.entry.insert(0, 'Invalid Input!')
            messagebox.showerror("Error", "Invalid Input!")
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, value)

    def sq_root(self):
        new_exp = self.replace_symbol()
        try:
            value = eval(new_exp)
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(0))
        except SyntaxError or NameError:
            self.entry.delete(0, tk.END)
            # self.entry.insert(0, 'Invalid Input!')
            messagebox.showerror("Error", "Invalid Input!")
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, value ** 0.5)

    def square(self):
        new_exp = self.replace_symbol()
        try:
            value = eval(new_exp)
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(0))
        except SyntaxError or NameError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, 'Invalid Input!')
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, value * value)

    def clear_one(self):
        s1 = self.entry.get()
        self.entry.delete(len(s1) - 1, tk.END)

    def clear(self):
        self.entry.delete(0, tk.END)

    def __init__(self):
        # Creating Root Window
        self.root = tk.Tk()

        # Setting Title of Root Window
        self.root.title("Calculator")

        # Setting Image/Icon on Root Window
        img = tk.PhotoImage(file="download.png")
        self.root.iconphoto(self.root, img)

        # Setting Width,height of root window and making it un resizeable
        self.root.geometry("445x250+520+275")
        self.root.resizable(width=False, height=False)

        # Creating Entry(Display of Calculator)
        self.entry = tk.Entry(self.root, width=30, font=("Calibri", 20), bd=5)

        # Creating Numeric Buttons(0,1,2,3,4,5,6,7,8,9)
        self.zero = tk.Button(self.root, text="0", width=8, height=2, command=lambda: self.action("0"))
        self.one = tk.Button(self.root, text="1", width=8, height=2, command=lambda: self.action("1"))
        self.two = tk.Button(self.root, text="2", width=8, height=2, command=lambda: self.action("2"))
        self.three = tk.Button(self.root, text="3", width=8, height=2, command=lambda: self.action("3"))
        self.four = tk.Button(self.root, text="4", width=8, height=2, command=lambda: self.action("4"))
        self.five = tk.Button(self.root, text="5", width=8, height=2, command=lambda: self.action("5"))
        self.six = tk.Button(self.root, text="6", width=8, height=2, command=lambda: self.action("6"))
        self.seven = tk.Button(self.root, text="7", width=8, height=2, command=lambda: self.action("7"))
        self.eight = tk.Button(self.root, text="8", width=8, height=2, command=lambda: self.action("8"))
        self.nine = tk.Button(self.root, text="9", width=8, height=2, command=lambda: self.action("9"))
        self.decimal = tk.Button(self.root, text=".", width=8, height=2, command=lambda: self.action("."))
        
        # Creating Operational buttons(.,-,*,/,+,%)
        self.subtract = tk.Button(self.root, text="-", width=8, height=2, command=lambda: self.action("-"))
        self.multiply = tk.Button(self.root, text="X", width=8, height=2, command=lambda: self.action("x"))
        self.divide = tk.Button(self.root, text="÷", width=8, height=2, command=lambda: self.action("÷"))
        self.plus = tk.Button(self.root, text="+", width=8, height=2, command=lambda: self.action("+"))
        self.percent = tk.Button(self.root, text="%", width=8, height=2, command=lambda: self.action("%"))
        
        # Creating brackets
        self.open_brace = tk.Button(self.root, text="(", width=8, height=2, command=lambda: self.action("("))
        self.close_brace = tk.Button(self.root, text=")", width=8, height=2, command=lambda: self.action(")"))
        
        # Creating buttons for square, square root, equal
        self.square = tk.Button(self.root, text="x²", width=8, height=2, command=self.square)
        self.sq_root = tk.Button(self.root, text="√", width=8, height=2, command=self.sq_root)
        self.equal = tk.Button(self.root, text="=", width=19, height=2, command=self.equal)
        
        # Creating buttons for clearing display
        self.clear = tk.Button(self.root, text="AC", width=8, height=2, command=self.clear)
        self.clear_one = tk.Button(self.root, text="C", width=8, height=2, command=self.clear_one)

        # Placing Buttons and Entry box
        # Row1 placing entry box(display of calculator)
        self.entry.grid(row=0, column=0, columnspan=6)
        self.entry.focus() # To set focus on display

        # Row2 placing buttons(7,8,9,/,%,C)
        self.seven.grid(row=2, column=0, padx=(10, 2), pady=5)
        self.eight.grid(row=2, column=1, padx=2, pady=5)
        self.nine.grid(row=2, column=2, padx=2, pady=5)
        self.divide.grid(row=2, column=3, padx=2, pady=5)
        self.percent.grid(row=2, column=4, padx=2, pady=5)
        self.clear_one.grid(row=2, column=5, padx=(2, 10), pady=5)

        # Row3 placing buttons(4,5,6,x,√,'(')
        self.four.grid(row=3, column=0, padx=(10, 2), pady=5)
        self.five.grid(row=3, column=1, padx=2, pady=5)
        self.six.grid(row=3, column=2, padx=2, pady=5)
        self.multiply.grid(row=3, column=3, padx=2, pady=5)
        self.sq_root.grid(row=3, column=4, padx=2, pady=5)
        self.open_brace.grid(row=3, column=5, padx=(2, 10), pady=5)

        # Row 4 placing buttons(1,2,3,-,x²,')')
        self.one.grid(row=4, column=0, padx=(10, 2), pady=5)
        self.two.grid(row=4, column=1, padx=2, pady=5)
        self.three.grid(row=4, column=2, padx=2, pady=5)
        self.subtract.grid(row=4, column=3, padx=2, pady=5)
        self.square.grid(row=4, column=4, padx=2, pady=5)
        self.close_brace.grid(row=4, column=5, padx=(2, 10), pady=5)

        # Row5 placing buttons(AC,0,.,+,=)
        self.clear.grid(row=5, column=0, padx=(10, 2), pady=5)
        self.zero.grid(row=5, column=1, padx=2, pady=5)
        self.decimal.grid(row=5, column=2, padx=2, pady=5)
        self.plus.grid(row=5, column=3, padx=2, pady=5)
        self.equal.grid(row=5, column=4, padx=(2, 10), pady=5, columnspan=2)

         # Action on pressing Enter key
        self.entry.bind("<Return>", self.enter_key)

        # Displaying Root Window
        self.root.mainloop()

# Driver code


if __name__ == '__main__':
    Calculator()
