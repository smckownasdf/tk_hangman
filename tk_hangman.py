import tkinter as tk

class Game(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)  # initialize Tkinter while you're at it
		
		# Create primary container for game to display
		main_container = tk.Frame(self)
		main_container.pack(side="top", fill="both", expand=True)  # maybe switch to grid later? fill set limits and expand into whitespace beyond that
		main_container.grid_rowconfigure(0, weight=1) 
		main_container.grid_columnconfigure(0, weight=1)

		# Create a Canvas on which to draw the hangman as the game progresses
		canvas = tk.Canvas(main_container, width=400, height=400)
		canvas.pack()

		# Create a visual separation between the canvas and the word display / buttons
		canvas_separator = tk.Frame(self, height=2, bd=1, relief="sunken")
		canvas_separator.pack(fill="x", padx=5, pady=5)

		# Create a text display as the word fills in
		tk.Label(text="W _ O _ R _ D _ _ _ D _ I _ S _ P _ L _ A _ Y").pack()

		# Separator between word display and buttons
		display_separator = tk.Frame(self, height=2, bd=1, relief="sunken")
		display_separator.pack(fill="x", padx=5, pady=5)

		# Create clickable buttons, ideally mapped to the keyboard keys (Should probably be a method in itself, like all of these)
		tk.Label(text="Buttons, oh yeah").pack()

app = Game()
app.mainloop()