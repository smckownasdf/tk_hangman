import tkinter as tk
from random import choice

# Deleted "Separators" which no longer served a purpose
# Created button for testing to see if behind-the-scenes code functions as expected
# Created future methods to implement

class Game(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)  # initialize Tkinter while you're at it
		self.main_container = tk.Frame(self)
		self.canvas_container = tk.Frame(self)
		self.button_container = tk.Frame(self, bg="yellow")
		self.letter_list = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
		self.word_list = ["pencil", "basket", "syzygy"]
		self.word = choice(self.word_list)
		self.answer_key = {}
	def Create_Canvas(self, *args, **kwargs): # Canvas for drawing hangman
		canvas = tk.Canvas(self.canvas_container, width=500, height=500, bg="blue")
		canvas.grid(column=1, row=1, columnspan=10)
		canvas.create_polygon(0, 375, 500, 375, 500, 500, 0, 500, fill="green", tags="setting")
		canvas.create_line(300, 410, 500, 410, tags="setting")
		canvas.create_line(400, 410, 400, 25, tags="setting")
		canvas.create_line(400, 25, 250, 25, tags="setting")
		canvas.create_line(250, 25, 250, 75, tags="setting")
	def Create_Main_Container(self, *args, **kwargs): # primary field / container for whole game display
		self.main_container.grid(rowspan=10, columnspan=10)
		self.main_container.grid_rowconfigure(0, weight=1) 
		self.main_container.grid_columnconfigure(0, weight=1)
	def Create_Canvas_Container(self, *args, **kwargs):
		self.canvas_container.grid(column=1, row=1, rowspan=6, columnspan=10)
	def Create_Button_Container(self, *args, **kwargs):
		self.button_container.grid(row=8, column=1, rowspan=3, columnspan=10)
		self.button_container.grid_rowconfigure(0, weight=1)
		self.button_container.grid_columnconfigure(0, weight=1)
	def Create_Letter_Buttons(self, *args, **kwargs):  # should probably create button class and give buttons names, attributes
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
			tk.Label(text=" __ ").grid(row = 7, column = current_column)
			self.answer_key.update({current_column : letter})
			current_column += 1
	def Check_Letter(self, letter, *args, **kwargs):
		pass
	def Update_Solution_Display(self, *args, **kwargs):
		pass
	def Update_Test_Display(self, btn_text, *args, **kwargs): # DELETE ME, for testing code in GUI
		lorem_ipsum = "Your button worked!"
		btn_text.set(lorem_ipsum)
	def Create_Test_Display_Button(self, *args, **kwargs): # DELETE ME, for testing code in GUI
		btn_text = tk.StringVar()
		test_display_text = "TEST RESULTS HERE"
		test_display_button = tk.Button(self.button_container, command=lambda: self.Update_Test_Display(btn_text), textvariable=btn_text)
		test_display_button.grid(row=10, column=8, columnspan=3, padx=2, pady=2, ipadx=5, sticky="NESW")
		btn_text.set(test_display_text)
	def Make_Game(self, *args, **kwargs):
		self.Create_Main_Container()
		self.Create_Canvas_Container()
		self.Create_Canvas()
		self.Create_Solution_Display()
		self.Create_Button_Container()
		self.Create_Letter_Buttons()
		self.Create_Test_Display_Button()


app = Game()
app.Make_Game()
app.mainloop()