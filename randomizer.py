# Modules
from random import randint as rnd # here we are importing random function, that working with integer only
from tkinter import * # windows create module

# Variables
ir = False # is resizable?
isRandom2 = False

def random(*sausage): # randomizer function
	global	isRandom2
	isRandom2 = False
	fefg = fef.get() # fef.get
	sefg = sef.get() # sef.get
	try:
		try:
			nmbr = rnd(int(fefg), int(sefg)) # random number
		except:
			try:
				nmbr = rnd(int(sefg), int(fefg)) # reversing our random number
			except:
				fef.delete(0, END) # deleting all from first field
				sef.delete(0, END) # deleting all from second field
				fef.insert(END, "Fill the fields!")
				sef.insert(END, "Fill the fields!")
	except:
		fef.delete(0, END) # deleting all from first field
		sef.delete(0, END) # deleting all from second field
		fef.insert(END, "Fill the fields!")
		sef.insert(END, "Fill the fields!")
	res = Label(root, text="Your number is: " + str(nmbr)) # result
	res.place(relwidth=0.5, relheight=0.1, rely=0.5, relx=0.25)
	print(nmbr) # writing random number in console

def random2(*pizza): # second randomizer function
	global isRandom2
	isRandom2 = True
	for i in range(100):
		fefg = fef.get() # fef.get
		sefg = sef.get() # sef.get

		try:
			try:
				nmbr = rnd(int(fefg), int(sefg)) # random number
			except:
				try:
					nmbr = rnd(int(sefg), int(fefg)) # reversing our random number
				except:
					fef.delete(0, END) # deleting all from first field
					sef.delete(0, END) # deleting all from second field
					fef.insert(END, "Fill the fields!")
					sef.insert(END, "Fill the fields!")
		except:
			fef.delete(0, END) # deleting all from first field
			sef.delete(0, END) # deleting all from second field
			fef.insert(END, "Fill the fields!")
			sef.insert(END, "Fill the fields!")

		res = Label(root, text="Your number is: " + str(nmbr)) # result
		res.place(relwidth=0.5, relheight=0.1, rely=0.5, relx=0.25)
		print(nmbr) # writing random number in console

def irchange(*ketchup):
	global ir
	if ir == False:
		root.resizable(True, True)
		ir = True
	elif ir == True:
		root.resizable(False, False)
		ir = False

def func_change(*cheese):
	global isRandom2
	if isRandom2 == True:
		isRandom2 = False
	elif isRandom2 == False:
		isRandom2 = True
	print(isRandom2)


def changer(*carbonara):
	global isRandom2
	if isRandom2 == False:
		random()
	elif isRandom2 == True:
		random2()
	print("isRandom2 = " + str(isRandom2))

# Window's setup
root = Tk() # our window
root.geometry("200x200") # window's size
root.resizable(False, False) # can we resize it? 1) vertical = False, 2) horizontal = False.
root.title("PupokRandom++")  # window's title

# Menus
menu = Menu(root) # main menu
root.config(menu=menu)

# Commands adding
menu.add_command(label="Change mode", command=func_change) # adding command
menu.add_command(label="Quit", command=quit)
menu.add_command(label="Resize", command=irchange)

# Object initializating
fefl = Label(root, text="From") # first entry field's label
fef = Entry(root, bg="#555", fg="#FFF", font="{Arial} 11") # first entry field
sefl = Label(root, text="To") # second entry field's label
sef = Entry(root, bg="#555", fg="#FFF", font="{Arial} 11") # second entry field
fb = Button(root, text="Get the number", command=changer) # randomizer button

# Placing
fefl.place(relwidth=0.5, relheight=0.1, rely=0.005, relx=0.25)
fef.place(relwidth=0.5, relheight=0.1, rely=0.1, relx=0.25)
sefl.place(relwidth=0.5, relheight=0.1, rely=0.2, relx=0.25)
sef.place(relwidth=0.5, relheight=0.1, rely=0.3, relx=0.25)
fb.place(relwidth=0.6, relheight=0.2, rely=0.7, relx=0.20)

# Binds
root.bind("<Return>", changer)
root.bind("<Control-Shift-Left>", func_change)
root.bind("<Control-Shift-Right>", func_change)

# Loop
root.mainloop() # window's loop
