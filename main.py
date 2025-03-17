from tkinter import *

import numpy as np

#inputs made by the user
tries = 999
dmi = int(input("how many dimensions do you want "))
while dmi%2==0 or tries<0 or ( dmi <= 2 or dmi > 5):
    dmi = int(input("Try again, how many dimensions do you want "))
    tries-=1
#UI
root = Tk()
root.title("magic square game")
root.config(bg="white")

label = Label(root, font=100)
label.grid(row=dmi, column=dmi-1)



#goal set to reach
M = int(dmi*(dmi**2+1)/2)
goal_label = Label(root,
                   text=f'This is your goal {M}',
                   font=0, fg='black',
                   activeforeground='black',
                   bg='white',
                   activebackground='white')
goal_label.grid(row= 0, column=dmi)

#Button function it checks if the the magic square is complete or not
#changes the screen to match what is written
def submit():
    inputs = []
    try:
        for entry in entries:
            for element in entry:
                inputs.append(int(element.get()))
        inputs2D = np.array(inputs)
        inputs2D = inputs2D.reshape(dmi, dmi)
        label.config(text="")
      #  print(inputs2D)

        #CHECK SUM
        sumd1 = 0
        sumd2 = 0

        for i in range(3):
            sumd1 += inputs2D[i][i]
            sumd2 += inputs2D[i][3 - i - 1]
            # if the two diagonal sums are not equal then it isn't a magic square
        if not (sumd1 == sumd2):
            print('diagonals do not match')

        for i in range(dmi):

            # row sum and column sum
            sumr = 0
            sumc = 0

            for j in range(dmi):
                sumr += inputs2D[i][j]
                sumc += inputs2D[j][i]

            if not (sumr == sumc == sumd1):
                break

        if sumr == sumc == sumd1:
            success = Label(root, text='Success, row and columns match', font=100)
            success.grid(row=dmi, column=dmi)
        else:
            failure = Label(root, text='failure, this is not a magic square', font=100)
            failure.grid(row=dmi, column=dmi)
        if len(set(inputs)) != len(inputs):
            label.config(text="No duplicate values are allowed")
    except ValueError:
        label.config(text="Error only integers are acceptable ")

#button ui/placement on the screen
buttonx = dmi - 1
buttony = dmi

button = Button(root,
                text='Submit',
                font=50,
                command=submit,
                bg='white',
                activebackground='white',
                fg='black',
                activeforeground='black',
                borderwidth=1,
                relief=FLAT,
                )
button.grid(row=buttonx, column=buttony)

entries = []
for i in range(dmi):
    row_entries = []
    for j in range(dmi):
        entry = Entry(root, justify='center', font=100, relief=GROOVE)
        entry.grid(row=i, column=j, ipadx=5, ipady=60, padx=10, pady=10)
        row_entries.append(entry)
    entries.append(row_entries)
root.eval('tk::PlaceWindow . center')
root.mainloop()

### Var: row_entries: collects/appends variable entry. Elements in entries are a punch of entry
### Var: entries, collects/appends row_entries.  Elements in entries are a punch of row_entries
