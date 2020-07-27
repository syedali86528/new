from tkinter import *

def main():
	root=Tk()
	root.title("MY FIRST TKINTER APP")
	root.minsize(width=300,height=300)
	root.maxsize(width=400,height=350)

	button=Button(root,text='click me!',width=40,height=3)
	button.pack()

	root.mainloop()

if __name__ == '__main__':
		main()	