from Tkinter import *
import Tkinter
import subprocess
import os
import sys

root = Tkinter.Tk()
root.title("SopiaSuite, 2014")
root.geometry('255x255+550+220') # (Geo: Height, Width, Horizontal, Vertical)
text = Text(root)
text.insert(INSERT, "Please select which tool\nyou wish to use...")

def kill_window():
	root.destroy()

# Asked question on SO about how to exit after a subprocess.
# http://stackoverflow.com/questions/21953256/python-script-not-exiting-when-using-tkinter/21953303?noredirect=1#21953303
# The suggestion was to give the subprocess a variable name
# Then use .wait() to wait because .wait() lets a child process finish before returning

def callDuff():
    proc = subprocess.Popen("python duffDir\duff.py")
    kill_window()
    proc.wait()
	# Following line is adapted from
	# http://sharats.me/the-ever-useful-and-neat-subprocess-module.html
	# Lets sub process finish before returning
	# End of borrowed code

def callFibs():
	proc = subprocess.Popen("python fibsDir\\fibs.py")
	kill_window()
	# Following line is adapted from
	# http://sharats.me/the-ever-useful-and-neat-subprocess-module.html
	# Lets sub process finish before returning
	proc.wait()
	# End of borrowed code


def callShift():
	proc = subprocess.Popen("python shiftDir\shift.py")
	kill_window()
	# Following line is adapted from
	# http://sharats.me/the-ever-useful-and-neat-subprocess-module.html
	# Lets sub process finish before returning
	proc.wait()
	# End of borrowed code

def callSpies():
	# os.chdir("spiesDir")
	# print os.getcwd()
	# print os.listdir(os.getcwd())
	proc = subprocess.Popen("python spiesDir\spies.py")
	kill_window()
	# Following line is adapted from
	# http://sharats.me/the-ever-useful-and-neat-subprocess-module.html
	# Lets sub process finish before returning
	proc.wait()
	# End of borrowed code

def callSiphon():
	print ("\nSIPHON is only compatible with Linux (Ubuntu)\nPlease run manually on Ubuntu.\n")

def callTrap():
	# os.chdir("spiesDir")
	# print os.getcwd()
	# print os.listdir(os.getcwd())
	proc = subprocess.Popen("python trapDir\\trap.py")
	kill_window()
	# Following line is adapted from
	# http://sharats.me/the-ever-useful-and-neat-subprocess-module.html
	# Lets sub process finish before returning
	proc.wait()
	# End of borrowed code

def callHelp():
	print "\nLaunching help files..."
	os.chdir("helpFiles")
	print os.getcwd()
	# Have to call hh.exe on Win 8.1 or error message because command line doesn't know what to do with chm ext
	proc = subprocess.Popen("hh.exe sopiaChm.chm")
	# The following simply lets you go back a directory so you can run another command from the menu
	os.getcwd()
	os.chdir("../")
	os.getcwd()

def callExit():
	print ("\nThank you for using SOPIA Suite\n\tGoodbye!\n")
	sys.exit(0)

buttonOne = Tkinter.Button(root, text ="DUFF", relief=FLAT, command=callDuff)
buttonTwo = Tkinter.Button(root, text ="FIBS", relief=FLAT, command=callFibs)
buttonThree = Tkinter.Button(root, text ="SHIFT", relief=FLAT, command=callShift)
buttonFour = Tkinter.Button(root, text ="SPIES", relief=FLAT, command=callSpies)
buttonFive = Tkinter.Button(root, text ="SIPHON", relief=FLAT, command=callSiphon)
buttonSix = Tkinter.Button(root, text ="HELP FILES", relief=FLAT, command=callHelp)
buttonSeven = Tkinter.Button(root, text ="EXIT", relief=FLAT, command=callExit)

buttonOne.pack()
buttonTwo.pack()
buttonThree.pack()
buttonFour.pack()
buttonFive.pack()
buttonSix.pack()
buttonSeven.pack()
text.pack()
root.mainloop()

# The following line with shell=True wont work...
# proc = subprocess.Popen("python spies.py", shell=True)

# Replaced the line WITHOUT shell and works. Weird....