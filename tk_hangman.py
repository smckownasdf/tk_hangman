import tkinter as tk
from random import choice

# TO-DO
# fill out Draw_Hangman method with visual cues
# create Free_Hangman method to draw happy, saved hangman on win
# convert test button to reset button
# add try / except and error testing
# Organize sections of code based on functionality for clarity & maybe add better comments

# DONE (this commit)
# added wrong_count variable & display within tk.Message window
# created (largely empty) Draw_Hangman method
# gave letter buttons full functionality


class Game(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)  # initialize Tkinter while you're at it
		self.main_container = tk.Frame(self)
		self.canvas_container = tk.Frame(self)
		self.button_container = tk.Frame(self, bg="pale goldenrod")
		self.letter_list = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
		self.word_list = ["pencil", "basket", "syzygy"]
		self.word = choice(self.word_list)
		self.word_display = " ".join(self.word)
		self.obscured_display = str("_ "*len(self.word))[:-1]
		self.wrong_count = 1
	def Create_Canvas(self, *args, **kwargs): # Canvas for drawing hangman
		canvas = tk.Canvas(self.canvas_container, width=500, height=500, bg="skyblue1")
		canvas.grid(column=1, row=1, columnspan=10)
		canvas.create_polygon(0, 375, 500, 375, 500, 500, 0, 500, fill="forest green", tags="setting")
		canvas.create_line(300, 410, 500, 410, tags="setting", width=5)
		canvas.create_line(400, 410, 400, 25, tags="setting", width=5)
		canvas.create_line(400, 25, 250, 25, tags="setting", width=5)
		canvas.create_line(250, 25, 250, 75, tags="setting", width=5)
	def Create_Main_Container(self, *args, **kwargs): # primary field / container for whole game display
		self.main_container.grid(rowspan=10, columnspan=10)
		self.main_container.grid_rowconfigure(0, weight=1) 
		self.main_container.grid_columnconfigure(0, weight=1)
	def Create_Canvas_Container(self, *args, **kwargs):
		self.canvas_container.grid(column=1, row=1, rowspan=6, columnspan=10)
	def Create_Button_Container(self, *args, **kwargs):
		self.button_container.grid(row=7, column=1, rowspan=3, columnspan=10)
		self.button_container.grid_rowconfigure(0, weight=1)
		self.button_container.grid_columnconfigure(0, weight=1)
	def Create_Letter_Buttons(self, *args, **kwargs):
		current_row = 8
		current_column = 1
		count = 0
		for letter in self.letter_list:
			letter_button = tk.Button(self.button_container, text=letter, command = lambda letter=letter : self.Check_Letter(letter)) # THIS TOOK ME FOREVER TO FIGURE OUT - without specifying "letter=letter" WITHIN lambda, it would always call last assignment after loop completion
			letter_button.grid(row = current_row, column = current_column, padx=2, pady=2, ipadx=5, sticky="NESW")

			if current_column < 10:
				current_column += 1
			else:
				current_column = 1
				current_row += 1
	def Create_Solution_Display(self, *args, **kwargs):
		self.display_message = tk.StringVar()

		solution_display = tk.Message(self.button_container, aspect=1000, textvariable=self.display_message)
		solution_display.grid(row=7, column=1, columnspan=10)
		solution_display.config(bg="lightblue", font=('helvetica', 20), pady=20, padx=50, relief="ridge")
		
		self.display_message.set(self.obscured_display)

	def Check_Letter(self, letter, *args, **kwargs):
		if letter in self.word:
			i = 0
			while i < len(self.word):
				if self.word[i] == letter:
					obscured_list = self.obscured_display.split(" ")
					obscured_list[i] = letter
					self.obscured_display = " ".join(obscured_list)
				i+=1
			self.Update_Solution_Display()
			self.Check_For_Win()
		elif self.wrong_count < 5:
			self.Wrong_Answer(self.wrong_count)
			self.Draw_Hangman(self.wrong_count)
			self.wrong_count += 1
		else:
			self.Draw_Hangman(self.wrong_count)
			self.display_message.set("YOU LOSE!\nCorrect Answer:\n"+self.word_display)
	def Wrong_Answer(self, wrong_count, *args, **kwargs):
		self.display_message.set(str(self.wrong_count)+" WRONG.")
		self.after(1000, self.Update_Solution_Display)
	def Draw_Hangman(self, wrong_count, *args, **kwargs):
		if self.wrong_count == 1:
			pass
		elif self.wrong_count == 2:
			pass
		elif self.wrong_count == 3:
			pass
		elif self.wrong_count == 4:
			pass
		elif self.wrong_count == 5:
			pass
		else:
			self.display_message.set("wrong_count variable error in Display_Hangman")
	def Update_Solution_Display(self, *args, **kwargs):
		self.display_message.set(self.obscured_display)
	def Check_For_Win(self, *args, **kwargs):
		if "_" not in self.obscured_display:
			self.display_message.set("You won!")
		else:
			pass
	def Update_Test_Display(self, btn_text, *args, **kwargs): # DELETE ME, for testing code in GUI
		lorem_ipsum = "Your button worked!"
		btn_text.set(self.word_display+self.obscured_display)
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