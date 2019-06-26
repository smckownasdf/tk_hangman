import tkinter as tk
from threading import Thread
from random import choice


# TO-DO
# prevent rapid input so that everything can execute properly, although this seems to be a pipe dream as far as I can tell
# create Free_Hangman method to draw happy, saved hangman on win
# add game reset functionality
# convert test button to reset button
# add try / except and error testing
# Organize sections of code based on functionality for clarity & maybe add better comments

# DONE (this commit)
# Converted dynamically produced letter buttons to static buttons so they'd be easier to work with
# Deleted (or tried?) Thread execution of Draw_Hangman because it failed to solve the issue with interrupted drawing
# Disabled GUI buttons in Check_Letter method to prevent multiple key presses of same letter
# Binded keyboard to button functionality

class Game(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)  # initialize Tkinter while you're at it
		self.main_container = tk.Frame(self)
		self.canvas_container = tk.Frame(self)
		self.button_container = tk.Frame(self, bg="pale goldenrod")
		self.canvas = None
		self.letter_list = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
		self.word_list = ["pencil", "basket", "syzygy"]
		self.word = choice(self.word_list)
		self.word_display = " ".join(self.word)
		self.obscured_display = str("_ "*len(self.word))[:-1]
		self.wrong_count = 1
		self.main_container.bind("<Key>", self.Test_Key_Press)
		self.buttons = []
	def Create_Canvas(self, *args, **kwargs): # Canvas for drawing hangman
		self.canvas = tk.Canvas(self.canvas_container, width=500, height=500, bg="skyblue1")
		self.canvas.grid(column=1, row=1, columnspan=10)
		self.canvas.create_polygon(0, 375, 500, 375, 500, 500, 0, 500, fill="forest green", tags="setting")
		self.canvas.create_line(300, 410, 500, 410, tags="setting", width=5) # gallows base
		self.canvas.create_line(400, 410, 400, 25, tags="setting", width=5) # gallows vertical support beam
		self.canvas.create_line(400, 25, 250, 25, tags="setting", width=5) # gallows horizontal overhead beam
		self.canvas.create_oval(245, 25, 255, 35, tags="setting", width=2) # gallows rope loop
		self.canvas.create_line(250, 35, 250, 75, fill="goldenrod", tags="setting", width=5) # gallows noose line
		self.canvas.create_line(250, 75, 250, 125, fill="goldenrod", tags="setting", width=10) # gallows noose knot
		self.canvas.create_oval(235, 125, 265, 165, outline="goldenrod", tags="setting", width=5) # gallows noose loop
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
		a_button = tk.Button(self.button_container, text="a", command=lambda : self.Check_Letter(a_button))
		a_button.grid(row=8, column=1, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("a", lambda event: self.Check_Letter(a_button))
		self.buttons.append(a_button)
		b_button = tk.Button(self.button_container, text="b", command=lambda : self.Check_Letter(b_button))
		b_button.grid(row=8, column=2, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("b", lambda event: self.Check_Letter(b_button))
		self.buttons.append(b_button)
		c_button = tk.Button(self.button_container, text="c", command=lambda : self.Check_Letter(c_button))
		c_button.grid(row=8, column=3, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("c", lambda event: self.Check_Letter(c_button))
		self.buttons.append(c_button)
		d_button = tk.Button(self.button_container, text="d", command=lambda : self.Check_Letter(d_button))
		d_button.grid(row=8, column=4, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("d", lambda event: self.Check_Letter(d_button))
		e_button = tk.Button(self.button_container, text="e", command=lambda : self.Check_Letter(e_button))
		e_button.grid(row=8, column=5, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("e", lambda event: self.Check_Letter(e_button))
		f_button = tk.Button(self.button_container, text="f", command=lambda : self.Check_Letter(f_button))
		f_button.grid(row=8, column=6, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("f", lambda event: self.Check_Letter(f_button))
		g_button = tk.Button(self.button_container, text="g", command=lambda : self.Check_Letter(g_button))
		g_button.grid(row=8, column=7, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("g", lambda event: self.Check_Letter(g_button))
		h_button = tk.Button(self.button_container, text="h", command=lambda : self.Check_Letter(h_button))
		h_button.grid(row=8, column=8, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("h", lambda event: self.Check_Letter(h_button))
		i_button = tk.Button(self.button_container, text="i", command=lambda : self.Check_Letter(i_button))
		i_button.grid(row=8, column=9, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("i", lambda event: self.Check_Letter(i_button))
		j_button = tk.Button(self.button_container, text="j", command=lambda : self.Check_Letter(j_button))
		j_button.grid(row=8, column=10, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("j", lambda event: self.Check_Letter(j_button))
		k_button = tk.Button(self.button_container, text="k", command=lambda : self.Check_Letter(k_button))
		k_button.grid(row=9, column=1, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("k", lambda event: self.Check_Letter(k_button))
		l_button = tk.Button(self.button_container, text="l", command=lambda : self.Check_Letter(l_button))
		l_button.grid(row=9, column=2, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("l", lambda event: self.Check_Letter(l_button))
		m_button = tk.Button(self.button_container, text="m", command=lambda : self.Check_Letter(m_button))
		m_button.grid(row=9, column=3, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("m", lambda event: self.Check_Letter(m_button))
		n_button = tk.Button(self.button_container, text="n", command=lambda : self.Check_Letter(n_button))
		n_button.grid(row=9, column=4, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("n", lambda event: self.Check_Letter(n_button))
		o_button = tk.Button(self.button_container, text="o", command=lambda : self.Check_Letter(o_button))
		o_button.grid(row=9, column=5, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("o", lambda event: self.Check_Letter(o_button))
		p_button = tk.Button(self.button_container, text="p", command=lambda : self.Check_Letter(p_button))
		p_button.grid(row=9, column=6, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("p", lambda event: self.Check_Letter(p_button))
		q_button = tk.Button(self.button_container, text="q", command=lambda : self.Check_Letter(q_button))
		q_button.grid(row=9, column=7, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("q", lambda event: self.Check_Letter(q_button))
		r_button = tk.Button(self.button_container, text="r", command=lambda : self.Check_Letter(r_button))
		r_button.grid(row=9, column=8, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("r", lambda event: self.Check_Letter(r_button))
		s_button = tk.Button(self.button_container, text="s", command=lambda : self.Check_Letter(s_button))
		s_button.grid(row=9, column=9, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("s", lambda event: self.Check_Letter(s_button))
		t_button = tk.Button(self.button_container, text="t", command=lambda : self.Check_Letter(t_button))
		t_button.grid(row=9, column=10, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("t", lambda event: self.Check_Letter(t_button))
		u_button = tk.Button(self.button_container, text="u", command=lambda : self.Check_Letter(u_button))
		u_button.grid(row=10, column=1, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("u", lambda event: self.Check_Letter(u_button))
		v_button = tk.Button(self.button_container, text="v", command=lambda : self.Check_Letter(v_button))
		v_button.grid(row=10, column=2, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("v", lambda event: self.Check_Letter(v_button))
		w_button = tk.Button(self.button_container, text="w", command=lambda : self.Check_Letter(w_button))
		w_button.grid(row=10, column=3, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("w", lambda event: self.Check_Letter(w_button))
		x_button = tk.Button(self.button_container, text="x", command=lambda : self.Check_Letter(x_button))
		x_button.grid(row=10, column=4, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("x", lambda event: self.Check_Letter(x_button))
		y_button = tk.Button(self.button_container, text="y", command=lambda  : self.Check_Letter(y_button))
		y_button.grid(row=10, column=5, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("y", lambda event: self.Check_Letter(y_button))
		z_button = tk.Button(self.button_container, text="z", command=lambda  : self.Check_Letter(z_button))
		z_button.grid(row=10, column=6, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.bind("z", lambda event: self.Check_Letter(z_button))
		self.buttons.extend((a_button, b_button, c_button, d_button, e_button, f_button, g_button, h_button, 
			i_button, j_button, k_button, l_button, m_button, n_button, o_button, p_button, q_button, r_button, 
			s_button, t_button, u_button, v_button, w_button, x_button, y_button, z_button))  # add all buttons to buttons list for easy access in resetting the game
	def Create_Solution_Display(self, *args, **kwargs):
		self.display_message = tk.StringVar()

		solution_display = tk.Message(self.button_container, aspect=1000, textvariable=self.display_message)
		solution_display.grid(row=7, column=1, columnspan=10)
		solution_display.config(bg="lightblue", font=('helvetica', 20), pady=20, padx=50, relief="ridge")
		
		self.display_message.set(self.obscured_display)

	def Check_Letter(self, button, event=None, *args, **kwargs): # event=None is for key binding. Explanation: https://stackoverflow.com/questions/13326940/python-tkinter-how-to-bind-key-to-a-button
		button.config(state="disabled")
		letter = button.cget("text")
		if button.cget("text") in self.word:
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
			self.Draw_Hangman(self.wrong_count)
			self.Wrong_Answer(self.wrong_count)
			self.after(1000, self.Increase_Wrong_Count)
		else:
			self.Draw_Hangman(self.wrong_count)
			self.display_message.set("YOU LOSE!\nCorrect Answer:\n"+self.word_display)
			self.Disable_Buttons()

	def Increase_Wrong_Count(self, *args, **kwargs):
		self.wrong_count += 1
	def Wrong_Answer(self, wrong_count, *args, **kwargs):
		self.display_message.set(str(self.wrong_count)+" WRONG.")
		self.after(1000, self.Update_Solution_Display) # more familiar time.sleep doesn't play nicely with tkinter; this is rough equivalent
	def Draw_Hangman(self, wrong_count, *args, **kwargs):
		if self.wrong_count == 1:
			self.canvas.create_oval(220,102, 280, 162, fill="blanched almond", tags="hangman")
		elif self.wrong_count == 2:
			self.canvas.create_polygon(220,250, 220,200, 210,210, 190,200, 215,168, 285,168, 310,200, 290,210, 280,200, 280,250, fill="red4") # Shirt (torso) - center numbers are top of shirt
		elif self.wrong_count == 3:
			self.canvas.create_polygon(235,352, 210,350, 220,250, 280,250, 290,350, 265,352, 250,290, fill="navy") # pants (legs) - center numbers are top of pants
		elif self.wrong_count == 4:
			self.canvas.create_line(200,205, 195,215, width=7) # (our) left arm upper
			self.canvas.create_line(193,213, 220,220, width=7) # left arm lower
			self.canvas.create_line(300,205, 305,215, width=7) # right arm upper
			self.canvas.create_line(307,213, 279,220, width=7) # right arm lower
			self.canvas.create_polygon(265,352, 290,350, 310,352, 312,368, 267,368) # right shoe, drawn from top-left of shoe
			self.canvas.create_polygon(235,352, 210,350, 190,352, 188,368, 232,368) # left shoe, drawn from top-right of shoe
		elif self.wrong_count == 5: # face / game over
			self.canvas.create_line(235,130, 240,135, width=2) # (our) right eye pt1
			self.canvas.create_line(235,135, 240,130, width=2) # right eye pt2
			self.canvas.create_line(265,130, 260,135, width=2) # left eye pt1
			self.canvas.create_line(265,135, 260,130, width=2) # left eye pt2
			self.canvas.create_arc(235,145, 265,155, extent=180, style="arc", width=2) # frown
			self.canvas.create_arc(250,140, 255,155, extent=-180, style="arc", fill="tomato2", outline="tomato3")
		else:
			self.display_message.set("wrong_count variable error in Display_Hangman")
	def Update_Solution_Display(self, *args, **kwargs):
		self.display_message.set(self.obscured_display)
	def Check_For_Win(self, *args, **kwargs):
		if "_" not in self.obscured_display:
			self.display_message.set("You won!")
			self.Disable_Buttons()
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
		self.bind("<Return>", lambda event : self.Update_Test_Display(btn_text))
	def Disable_Buttons(self, *args, **kwargs):
		for button in self.buttons:
			button.config(state="disabled")
	def Make_Game(self, *args, **kwargs):
		self.Create_Main_Container()
		self.Create_Canvas_Container()
		self.Create_Canvas()
		self.Create_Solution_Display()
		self.Create_Button_Container()
		self.Create_Letter_Buttons()
		self.Create_Test_Display_Button()
	def Test_Key_Press(self, event, *args, **kwargs):
		self.display_message.set(event.char)



app = Game()
app.Make_Game()
app.mainloop()