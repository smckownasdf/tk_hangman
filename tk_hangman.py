import tkinter as tk
from random import choice

class Game(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)  # initialize Tkinter while you're at it
		self.main_container = tk.Frame(self)
		self.canvas_container = tk.Frame(self)
		self.button_container = tk.Frame(self, bg="yellow")
		self.letter_list = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
		self.word_list = ["pencil", "basket", "syzygy"]
		self.word = choice(self.word_list)
	def Create_Canvas(self, *args, **kwargs): # Canvas for drawing hangman
		canvas = tk.Canvas(self.canvas_container, width=500, height=500, bg="blue")
		canvas.grid(column=1, row=1, columnspan=10)
		canvas.create_polygon(0, 375, 500, 375, 500, 500, 0, 500, fill="green", tags="setting")
		canvas.create_line(300, 410, 500, 410, tags="setting")
		canvas.create_line(400, 410, 400, 25, tags="setting")
		canvas.create_line(400, 25, 250, 25, tags="setting")
		canvas.create_line(250, 25, 250, 75, tags="setting")
	def Create_Main_Container(self, *args, **kwargs): # primary field / container for whole game display
		self.main_container.grid(rowspan=10, columnspan=10)  # maybe switch to grid later? fill set limits and expand into whitespace beyond that
		self.main_container.grid_rowconfigure(0, weight=1) 
		self.main_container.grid_columnconfigure(0, weight=1)
	def Create_Canvas_Container(self, *args, **kwargs):
		self.canvas_container.grid(column=1, row=1, rowspan=6, columnspan=10)
	def Create_Separator(self, num, *args, **kwargs): # Create a visual separation between the canvas and the word display / buttons
		canvas_separator = tk.Frame(self, height=2, bd=1, relief="sunken")
		canvas_separator.grid(row=num, columnspan=10, padx=5, pady=5)
	def Create_Button_Container(self, *args, **kwargs):
		self.button_container.grid(row=8, column=1, rowspan=3, columnspan=10)
		self.button_container.grid_rowconfigure(0, weight=1)
		self.button_container.grid_columnconfigure(0, weight=1)
	def Create_Buttons(self, *args, **kwargs):  # should probably create button class and give buttons names, attributes
		current_row = 8
		current_column = 1
		for letter in self.letter_list:
			letter_button = tk.Button(self.button_container, text=letter)
			letter_button.grid(row = current_row, column = current_column, padx=2, pady=2, ipadx=5, sticky="NESW")
			if current_column < 10:
				current_column += 1
			else:
				current_column = 1
				current_row += 1
	def Create_Solution_Display(self, *args, **kwargs):
		current_column = 1
		for letter in self.word:
			tk.Label(text=letter).grid(row = 7, column = current_column)
			current_column += 1
	def Make_Game(self, *args, **kwargs):
		self.Create_Main_Container()
		self.Create_Canvas_Container()
		self.Create_Canvas()
		self.Create_Separator(2)
		self.Create_Solution_Display()
		self.Create_Separator(6)
		# Separator between word display and buttons
		self.Create_Button_Container()
		self.Create_Buttons()
		# Create clickable buttons, ideally mapped to the keyboard keys (Should probably be a method in itself, like all of these)


app = Game()
app.Make_Game()
app.mainloop()