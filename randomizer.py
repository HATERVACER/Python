from random import randint as rnd # here we are importing random function, that working with integer only
from tkinter import * # windows create module

root = Tk() # our window
root.geometry("200x200") # window's size
root.resizable(False, False) # can we resize it? 1) vertical = False, 2) horizontal = False.
root.title("PupokRandom++")  # window's title
root.option_add("Background", "#ffffff") # White background for all objects in our window

def random(): # randomizer function
	fefg = fef.get() # fef.get
	sefg = sef.get() # sef.get 
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
	res = Label(root, text="Your number is: " + str(nmbr)) # result
	res.place(relwidth=0.5, relheight=0.1, rely=0.5, relx=0.25)
	print(nmbr) # writing random number in console

fefl = Label(root, text="From") # first entry field's label
fef = Entry(root) # first entry field
sefl = Label(root, text="To") # second entry field's label
sef = Entry(root) # second entry field 
fb = Button(root, text="Get the number", command=random) # randomizer button

# Placing
fefl.place(relwidth=0.5, relheight=0.1, rely=0.005, relx=0.25)
fef.place(relwidth=0.5, relheight=0.1, rely=0.1, relx=0.25)
sefl.place(relwidth=0.5, relheight=0.1, rely=0.2, relx=0.25)
sef.place(relwidth=0.5, relheight=0.1, rely=0.3, relx=0.25)
fb.place(relwidth=0.6, relheight=0.2, rely=0.7, relx=0.20)

root.mainloop() # window's loop