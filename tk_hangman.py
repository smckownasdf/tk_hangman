import tkinter as tk

class Game(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)  # initialize Tkinter while you're at it
		self.main_container = main_container = tk.Frame(self)
		self.letter_list = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]

	def Create_Canvas(self, *args, **kwargs): # Canvas for drawing hangman
		canvas = tk.Canvas(self.main_container, width=400, height=400, bg="blue")
		canvas.pack()
	def Create_Main_Container(self, *args, **kwargs): # primary field / container for whole game display
		self.main_container.pack(side="top", fill="both", expand=True)  # maybe switch to grid later? fill set limits and expand into whitespace beyond that
		self.main_container.grid_rowconfigure(0, weight=1) 
		self.main_container.grid_columnconfigure(0, weight=1)
	def Create_Separator(self, *args, **kwargs): # Create a visual separation between the canvas and the word display / buttons
		canvas_separator = tk.Frame(self, height=2, bd=1, relief="sunken")
		canvas_separator.pack(fill="x", padx=5, pady=5)
	def Create_Buttons(self, *args, **kwargs):
		tk.Label(text=self.letter_list).pack()
	def Create_Solution_Display(self, *args, **kwargs):
		tk.Label(text="W _ O _ R _ D _ _ _ D _ I _ S _ P _ L _ A _ Y").pack()
	def Make_Game(self, *args, **kwargs):
		self.Create_Main_Container()
		self.Create_Canvas()
		self.Create_Separator()
		self.Create_Solution_Display()
		self.Create_Separator()
		# Separator between word display and buttons
		self.Create_Buttons()
		# Create clickable buttons, ideally mapped to the keyboard keys (Should probably be a method in itself, like all of these)


app = Game()
app.Make_Game()
app.mainloop()