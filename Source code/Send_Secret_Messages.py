from tkinter import *
from tkinter.messagebox import showerror
import pybase64



def Encrypt_data():
	massege = enter1.get(1.0,END)
	Password = str(password.get())
	if Password == "##@m@n@t##":
		data = massege.encode("ascii")
		data_row = pybase64.b64encode(data)
		final_data = data_row.decode("ascii")
		win1 = Toplevel()
		win1.geometry("500x300")
		win1.resizable(False,False)
		win1.config(bg = "Blue")
		win1.title("Encrypt data")
 
		t = Text(win1,font=("Time New Roman",20))
		t.insert(1.0,final_data)
		t.place(x = 20,y = 20,height = 260,width = 460)

		win1.mainloop()

	else:
		showerror(title = "Password",message ="Worng Password")


def Decrypt_data():
	massege = enter1.get(1.0,END)
	Password = str(password.get())
	if Password == "##@m@n@t##":
		data = massege.encode("ascii")
		data_row = pybase64.b64decode(data)
		final_data = data_row.decode("ascii")
		win1 = Toplevel()
		win1.geometry("500x300")
		win1.resizable(False,False)
		win1.config(bg = "Blue")
		win1.title("Decrypt data")
 
		t = Text(win1,font=("Time New Roman",20))
		t.insert(1.0,final_data)
		t.place(x = 20,y = 20,height = 260,width = 460)

		win1.mainloop()

	else:
		showerror(title = "Password",message ="Worng Password")


def Reset_data():
	enter1.delete(1.0,END)
	password.delete(0,END)



def main_win():
	global enter1,password

	win = Tk()
	win.title("Pass Encrypten")
	win.config(bg = "Blue")
	win.geometry("500x550")
	win.resizable(False,False)

	label1 = Label(win,text = "Enter your Message",font=("Time New Roman",20,"bold"),bg = "Blue",fg="white")
	label1.place(x=20,y=20,height=40,width=270)

	enter1 = Text(win,font=("Time New Roman",20))
	enter1.place(x = 20,y = 70,height = 200,width = 460)

	label2 = Label(win,text = "Enter your Password",font=("Time New Roman",20,"bold"),bg = "Blue",fg="white")
	label2.place(x=20,y=280,height=40,width=280)

	password = Entry(win,font=("Time New Roman",20),show="*")
	password.place(x = 20,y = 330,height = 50,width = 460)

	en = Button(win, text = "Encrypt",font=("Time New Roman",20),bg = "Red",fg = "white",command = Encrypt_data)
	en.place(x = 20,y = 390,height = 50,width = 220)


	dn = Button(win, text = "Decrypt",font=("Time New Roman",20),bg = "Green",fg = "white",command = Decrypt_data)
	dn.place(x = 260,y = 390,height = 50,width = 220)

	rn = Button(win, text = "Reset",font=("Time New Roman",20),bg = "yellow",command = Reset_data)
	rn.place(x = 140,y = 450,height = 50,width = 220)


	win.mainloop()



main_win()