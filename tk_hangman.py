import tkinter as tk
from random import choice
from sys import exit

# TO-DO
# prevent rapid input so that everything can execute properly, although this seems to be a pipe dream as far as I can tell
# create Free_Hangman method to draw happy, saved hangman on win
# add try / except and error testing
# maybe add better comments so I don't hate myself when I look at this next

# DONE (this commit)
# Created section headers to help organize code better
# Unb[ou]nd keyboard letter keys in both Disable_Buttons and Check_Letter methods
# Refactored Create_Letter_Buttons into self and Bind_Buttons
# Added "hangman" tags to all hangman animations
# Created Remove_Hangman, Start_Displays, Enable_Buttons, Reset_Variables, and Reset_Game methods
# Refactored __init__ word creation assignments into Choose_Word method
# Converted test button to reset button and finished game loop
# Created Enable_Reset_Button, Disable_Reset_Button methods and made reset button only available upon game win / loss
# Grabs larger (235970) word list from external file (https://svnweb.freebsd.org/base/head/share/dict/web2)
# Connected sys.exit and used bind to close app with escape key
# added sun, clouds, lines to indicate slipknot, and mountains
# Created second display for messages rather than single display
# Created Draw_Free_Hangman method to show free, happy hangman



class Game(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)  # initialize Tkinter while you're at it
		self.main_container = tk.Frame(self)
		self.canvas_container = tk.Frame(self)
		self.button_container = tk.Frame(self, bg="pale goldenrod")
		self.canvas = None
		self.letter_list = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
		self.word_list = ["pencil", "basket", "syzygy"]
		self.word = None
		self.word_display = None
		self.obscured_display = None
		self.wrong_count = 1
		self.buttons = []
		self.reset_button = None
		self.display_message = tk.StringVar()
		self.solution_display_message = tk.StringVar()
		self.bind('<Escape>', self.Close)
# -------------------------------------------------------------------------------------------
# Creation Methods
# -------------------------------------------------------------------------------------------
	def Create_Canvas(self, *args, **kwargs): # Canvas for drawing hangman
		self.canvas = tk.Canvas(self.canvas_container, width=500, height=500, bg="skyblue1")
		self.canvas.grid(column=1, row=1, columnspan=10)
		self.Draw_Ground()
		self.Draw_Sun()
		self.Draw_Clouds()
		self.Draw_Gallows()
		self.Draw_Rope()

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
		a_button.grid(row=9, column=1, padx=2, pady=2, ipadx=5, sticky="NESW")
		b_button = tk.Button(self.button_container, text="b", command=lambda : self.Check_Letter(b_button))
		b_button.grid(row=9, column=2, padx=2, pady=2, ipadx=5, sticky="NESW")
		c_button = tk.Button(self.button_container, text="c", command=lambda : self.Check_Letter(c_button))
		c_button.grid(row=9, column=3, padx=2, pady=2, ipadx=5, sticky="NESW")
		d_button = tk.Button(self.button_container, text="d", command=lambda : self.Check_Letter(d_button))
		d_button.grid(row=9, column=4, padx=2, pady=2, ipadx=5, sticky="NESW")
		e_button = tk.Button(self.button_container, text="e", command=lambda : self.Check_Letter(e_button))
		e_button.grid(row=9, column=5, padx=2, pady=2, ipadx=5, sticky="NESW")
		f_button = tk.Button(self.button_container, text="f", command=lambda : self.Check_Letter(f_button))
		f_button.grid(row=9, column=6, padx=2, pady=2, ipadx=5, sticky="NESW")
		g_button = tk.Button(self.button_container, text="g", command=lambda : self.Check_Letter(g_button))
		g_button.grid(row=9, column=7, padx=2, pady=2, ipadx=5, sticky="NESW")
		h_button = tk.Button(self.button_container, text="h", command=lambda : self.Check_Letter(h_button))
		h_button.grid(row=9, column=8, padx=2, pady=2, ipadx=5, sticky="NESW")
		i_button = tk.Button(self.button_container, text="i", command=lambda : self.Check_Letter(i_button))
		i_button.grid(row=9, column=9, padx=2, pady=2, ipadx=5, sticky="NESW")
		j_button = tk.Button(self.button_container, text="j", command=lambda : self.Check_Letter(j_button))
		j_button.grid(row=9, column=10, padx=2, pady=2, ipadx=5, sticky="NESW")
		k_button = tk.Button(self.button_container, text="k", command=lambda : self.Check_Letter(k_button))
		k_button.grid(row=10, column=1, padx=2, pady=2, ipadx=5, sticky="NESW")
		l_button = tk.Button(self.button_container, text="l", command=lambda : self.Check_Letter(l_button))
		l_button.grid(row=10, column=2, padx=2, pady=2, ipadx=5, sticky="NESW")
		m_button = tk.Button(self.button_container, text="m", command=lambda : self.Check_Letter(m_button))
		m_button.grid(row=10, column=3, padx=2, pady=2, ipadx=5, sticky="NESW")
		n_button = tk.Button(self.button_container, text="n", command=lambda : self.Check_Letter(n_button))
		n_button.grid(row=10, column=4, padx=2, pady=2, ipadx=5, sticky="NESW")
		o_button = tk.Button(self.button_container, text="o", command=lambda : self.Check_Letter(o_button))
		o_button.grid(row=10, column=5, padx=2, pady=2, ipadx=5, sticky="NESW")
		p_button = tk.Button(self.button_container, text="p", command=lambda : self.Check_Letter(p_button))
		p_button.grid(row=10, column=6, padx=2, pady=2, ipadx=5, sticky="NESW")
		q_button = tk.Button(self.button_container, text="q", command=lambda : self.Check_Letter(q_button))
		q_button.grid(row=10, column=7, padx=2, pady=2, ipadx=5, sticky="NESW")
		r_button = tk.Button(self.button_container, text="r", command=lambda : self.Check_Letter(r_button))
		r_button.grid(row=10, column=8, padx=2, pady=2, ipadx=5, sticky="NESW")
		s_button = tk.Button(self.button_container, text="s", command=lambda : self.Check_Letter(s_button))
		s_button.grid(row=10, column=9, padx=2, pady=2, ipadx=5, sticky="NESW")
		t_button = tk.Button(self.button_container, text="t", command=lambda : self.Check_Letter(t_button))
		t_button.grid(row=10, column=10, padx=2, pady=2, ipadx=5, sticky="NESW")
		u_button = tk.Button(self.button_container, text="u", command=lambda : self.Check_Letter(u_button))
		u_button.grid(row=11, column=1, padx=2, pady=2, ipadx=5, sticky="NESW")
		v_button = tk.Button(self.button_container, text="v", command=lambda : self.Check_Letter(v_button))
		v_button.grid(row=11, column=2, padx=2, pady=2, ipadx=5, sticky="NESW")
		w_button = tk.Button(self.button_container, text="w", command=lambda : self.Check_Letter(w_button))
		w_button.grid(row=11, column=3, padx=2, pady=2, ipadx=5, sticky="NESW")
		x_button = tk.Button(self.button_container, text="x", command=lambda : self.Check_Letter(x_button))
		x_button.grid(row=11, column=4, padx=2, pady=2, ipadx=5, sticky="NESW")
		y_button = tk.Button(self.button_container, text="y", command=lambda  : self.Check_Letter(y_button))
		y_button.grid(row=11, column=5, padx=2, pady=2, ipadx=5, sticky="NESW")
		z_button = tk.Button(self.button_container, text="z", command=lambda  : self.Check_Letter(z_button))
		z_button.grid(row=11, column=6, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.buttons.extend((a_button, b_button, c_button, d_button, e_button, f_button, g_button, h_button, 
			i_button, j_button, k_button, l_button, m_button, n_button, o_button, p_button, q_button, r_button, 
			s_button, t_button, u_button, v_button, w_button, x_button, y_button, z_button))  # add all buttons to buttons list for easy access in resetting the game
		self.Bind_Buttons()

	def Create_Displays(self, *args, **kwargs):
		solution_display = tk.Message(self.button_container, aspect=1000, textvariable=self.solution_display_message)
		solution_display.grid(row=7, column=1, columnspan=10)
		solution_display.config(bg="lightblue", font=('helvetica', 20), pady=20, padx=50, relief="ridge")

		self.display_message = tk.StringVar()
		message_display = tk.Message(self.button_container, aspect=1000, textvariable=self.display_message)
		message_display.grid(row=8, column=1, columnspan=10)
		message_display.config(bg="lightblue", font=('helvetica', 20), pady=20, padx=50, relief="ridge")
		self.Start_Displays()

	def Bind_Buttons(self, *args, **kwargs):
		# I hate using index numbers instead of names, but why use a dictionary just to make this look nicer?
		self.bind("a", lambda event: self.Check_Letter(self.buttons[0])) 
		self.bind("b", lambda event: self.Check_Letter(self.buttons[1]))
		self.bind("c", lambda event: self.Check_Letter(self.buttons[2]))
		self.bind("d", lambda event: self.Check_Letter(self.buttons[3]))
		self.bind("e", lambda event: self.Check_Letter(self.buttons[4]))
		self.bind("f", lambda event: self.Check_Letter(self.buttons[5]))
		self.bind("g", lambda event: self.Check_Letter(self.buttons[6]))
		self.bind("h", lambda event: self.Check_Letter(self.buttons[7]))
		self.bind("i", lambda event: self.Check_Letter(self.buttons[8]))
		self.bind("j", lambda event: self.Check_Letter(self.buttons[9]))
		self.bind("k", lambda event: self.Check_Letter(self.buttons[10]))
		self.bind("l", lambda event: self.Check_Letter(self.buttons[11]))
		self.bind("m", lambda event: self.Check_Letter(self.buttons[12]))
		self.bind("n", lambda event: self.Check_Letter(self.buttons[13]))
		self.bind("o", lambda event: self.Check_Letter(self.buttons[14]))
		self.bind("p", lambda event: self.Check_Letter(self.buttons[15]))
		self.bind("q", lambda event: self.Check_Letter(self.buttons[16]))
		self.bind("r", lambda event: self.Check_Letter(self.buttons[17]))
		self.bind("s", lambda event: self.Check_Letter(self.buttons[18]))
		self.bind("t", lambda event: self.Check_Letter(self.buttons[19]))
		self.bind("u", lambda event: self.Check_Letter(self.buttons[20]))
		self.bind("v", lambda event: self.Check_Letter(self.buttons[21]))
		self.bind("w", lambda event: self.Check_Letter(self.buttons[22]))
		self.bind("x", lambda event: self.Check_Letter(self.buttons[23]))
		self.bind("y", lambda event: self.Check_Letter(self.buttons[24]))
		self.bind("z", lambda event: self.Check_Letter(self.buttons[25]))

	def Create_Word_List(self, *args, **kwargs):
		# Thank you, https://svnweb.freebsd.org/base/head/share/dict/web2 for this file
		with open('words') as file:
		    self.word_list = [word.lower() for line in file for word in line.split()]

	def Make_Game(self, *args, **kwargs):
		self.Create_Main_Container()
		self.Create_Canvas_Container()
		self.Create_Canvas()
		self.Create_Button_Container()
		self.Create_Word_List()
		self.Choose_Word()
		self.Create_Letter_Buttons()
		self.Create_Reset_Button()
		self.Create_Displays()

	def Start_Displays(self, *args, **kwargs):
		self.solution_display_message.set(self.obscured_display)
		self.display_message.set("Welcome to TK Hangman!")
# -------------------------------------------------------------------------------------------
# Gameplay Methods
# -------------------------------------------------------------------------------------------
	def Check_Letter(self, button, event=None, *args, **kwargs): # event=None is for key binding. Explanation: https://stackoverflow.com/questions/13326940/python-tkinter-how-to-bind-key-to-a-button
		button.config(state="disabled")
		letter = button.cget("text")
		self.unbind(letter)
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
			self.display_message.set("Correct Answer: "+self.word_display)
			self.Disable_Buttons()
			self.Enable_Reset_Button()
			self.bind("<Return>", self.Reset_Game)


	def Increase_Wrong_Count(self, *args, **kwargs):
		self.wrong_count += 1

	def Wrong_Answer(self, wrong_count, *args, **kwargs):
		self.display_message.set(str(self.wrong_count)+" WRONG.")
		self.after(1000, self.Update_Solution_Display) # more familiar time.sleep doesn't play nicely with tkinter; this is rough equivalent
		self.after(1000, self.Update_Message_Display)

	def Update_Solution_Display(self, *args, **kwargs):
		self.solution_display_message.set(self.obscured_display)

	def Update_Message_Display(self, *args, **kwargs):
		if self.wrong_count < 3:
			self.display_message.set(f"{str(5-self.wrong_count)} guesses remaining!")
		elif self.wrong_count < 4:
			self.display_message.set(f"Only {str(5-self.wrong_count)} guesses left!")
		else:
			self.display_message.set("One guess left! Make it count!")

	def Check_For_Win(self, *args, **kwargs):
		if "_" not in self.obscured_display:
			self.display_message.set("You won!")
			self.Remove_Hangman()
			self.Disable_Buttons()
			self.Enable_Reset_Button()
			self.Draw_Free_Hangman()
		else:
			pass

	def Create_Reset_Button(self, *args, **kwargs): # DELETE ME, for testing code in GUI
		btn_text = "RESET GAME"
		self.reset_button = tk.Button(self.button_container, text=btn_text, command=self.Reset_Game)
		self.reset_button.grid(row=11, column=8, columnspan=3, padx=2, pady=2, ipadx=5, sticky="NESW")
		self.Disable_Reset_Button()

	def Enable_Reset_Button(self, *args, **kwargs):
		self.bind("<Return>", self.Reset_Game)
		self.reset_button.config(state="normal")

	def Disable_Reset_Button(self, *args, **kwargs):
		self.unbind("<Return>")
		self.reset_button.config(state="disabled")

	def Disable_Buttons(self, *args, **kwargs):
		for button in self.buttons:
			button.config(state="disabled")
		for letter in self.letter_list:
			self.unbind(letter)

# -------------------------------------------------------------------------------------------
# Animation Methods
# -------------------------------------------------------------------------------------------
	def Draw_Ground(self, *args, **kwargs):
		self.canvas.create_polygon(500,500, 0,500, 0,229, 169,305, 169,250, 220,220, 340,303, 340,270, 390,240, 430,260, 430,290, 500,240, fill="slate blue")
		self.canvas.create_polygon(500,500, 0,500, 0,300, 54,278, 180,303, 287,235, 397,300, 450,240, 500,290, fill="saddle brown", tags="setting")
		self.canvas.create_polygon(500,500, 0,500, 0,287, 67,304, 169,243, 305,305, 370,264, 457,344, 500,300, fill="brown4", tags="setting")
		self.canvas.create_polygon(0,400, 20,390, 200,385, 500,395, 500, 500, 0, 500, fill="forest green", tags="setting") # Ground

	def Draw_Gallows(self, *args, **kwargs):
		self.canvas.create_line(300, 410, 500, 410, tags="setting", width=5) # gallows base
		self.canvas.create_line(400, 410, 400, 25, tags="setting", width=5) # gallows vertical support beam
		self.canvas.create_line(400, 25, 250, 25, tags="setting", width=5) # gallows horizontal overhead beam
		self.canvas.create_oval(245, 25, 255, 35, tags="setting", width=2) # gallows rope loop

	def Draw_Rope(self, *args, **kwargs):
		self.canvas.create_line(250, 35, 250, 76, fill="goldenrod", tags="setting", width=5) # noose line
		self.canvas.create_line(250, 76, 250, 125, fill="goldenrod", tags="setting", width=10) # noose knot
		self.canvas.create_oval(235, 125, 265, 165, outline="goldenrod", tags="setting", width=5) # noose loop
		self.canvas.create_line(245,123,255,122, tags="setting") # rope detail
		self.canvas.create_line(245,119,255,118, tags="setting") # rope detail
		self.canvas.create_line(245,115,255,114, tags="setting") # rope detail
		self.canvas.create_line(245,111,255,110, tags="setting") # rope detail
		self.canvas.create_line(245,107,255,106, tags="setting") # rope detail
		self.canvas.create_line(245,103,255,102, tags="setting") # rope detail
		self.canvas.create_line(245,99,255,98, tags="setting") # rope detail
		self.canvas.create_line(245,95,255,94, tags="setting") # rope detail
		self.canvas.create_line(245,91,255,90, tags="setting") # rope detail
		self.canvas.create_line(245,87,255,86, tags="setting") # rope detail
		self.canvas.create_line(245,83,255,82, tags="setting") # rope detail
		self.canvas.create_line(245,79,255,78, tags="setting") # rope detail
		self.canvas.create_line(245,75,255,74, tags="setting") # rope detail

	def Draw_Sun(self, *args, **kwargs):
		self.canvas.create_oval(50, 50, 125, 125, fill="goldenrod", tags="setting") # Mr. Sun

	def Draw_Clouds(self, *args, **kwargs):
		self.canvas.create_oval(330, 38, 380, 54, fill="white", outline="white", tags="setting") # cloud (left)
		self.canvas.create_oval(360, 23, 420, 60, fill="white", outline="white", tags="setting") # cloud (left)
		self.canvas.create_oval(320, 30, 380, 50, fill="white", outline="white", tags="setting") # cloud (left)
		self.canvas.create_oval(380, 30, 460, 50, fill="white", outline="white", tags="setting") # cloud (left)
		self.canvas.create_oval(30, 138, 80, 154, fill="white", outline="white", tags="setting") # cloud (right)
		self.canvas.create_oval(60, 123, 120, 160, fill="white", outline="white", tags="setting") # cloud (right)
		self.canvas.create_oval(20, 140, 80, 150, fill="white", outline="white", tags="setting") # cloud (right)
		self.canvas.create_oval(80, 130, 160, 150, fill="white", outline="white", tags="setting") # cloud (right)

	def Draw_Mountains(self, *args, **kwargs):
		self.canvas.create_polygon()

	def Draw_Hangman(self, wrong_count, *args, **kwargs):
		if self.wrong_count == 1:
			self.canvas.create_oval(220,102, 280, 162, fill="blanched almond", tags="hangman")
		elif self.wrong_count == 2:
			self.canvas.create_polygon(220,250, 220,200, 210,210, 190,200, 215,168, 285,168, 310,200, 290,210, 280,200, 280,250, fill="red4", tags="hangman") # Shirt (torso) - center numbers are top of shirt
		elif self.wrong_count == 3:
			self.canvas.create_polygon(235,352, 210,350, 220,250, 280,250, 290,350, 265,352, 250,290, fill="navy", tags="hangman") # pants (legs) - center numbers are top of pants
		elif self.wrong_count == 4:
			self.canvas.create_line(200,205, 195,215, width=7, tags="hangman") # (our) left arm upper
			self.canvas.create_line(193,213, 220,220, width=7, tags="hangman") # left arm lower
			self.canvas.create_line(300,205, 305,215, width=7, tags="hangman") # right arm upper
			self.canvas.create_line(307,213, 279,220, width=7, tags="hangman") # right arm lower
			self.canvas.create_polygon(265,352, 290,350, 310,352, 312,368, 267,368, tags="hangman") # right shoe, drawn from top-left of shoe
			self.canvas.create_polygon(235,352, 210,350, 190,352, 188,368, 232,368, tags="hangman") # left shoe, drawn from top-right of shoe
		elif self.wrong_count == 5: # face / game over
			self.canvas.create_line(235,130, 240,135, width=2, tags="hangman") # (our) right eye pt1
			self.canvas.create_line(235,135, 240,130, width=2, tags="hangman") # right eye pt2
			self.canvas.create_line(265,130, 260,135, width=2, tags="hangman") # left eye pt1
			self.canvas.create_line(265,135, 260,130, width=2, tags="hangman") # left eye pt2
			self.canvas.create_arc(235,145, 265,155, extent=180, style="arc", width=2, tags="hangman") # frown
			self.canvas.create_arc(250,140, 255,155, extent=-180, style="arc", fill="tomato2", outline="tomato3", tags="hangman") # tongue
		else:
			self.display_message.set("wrong_count variable error in Display_Hangman")

	def Draw_Free_Hangman(self, *args, **kwargs):
		self.canvas.create_polygon(155,220, 145,220, 145,210, 155,210, fill="blanched almond") # neck
		self.canvas.create_oval(120,152, 180,212, fill="blanched almond", tags="hangman") # head
		self.canvas.create_oval(135,175, 143,180, tags="hangman") # (our) left eye
		self.canvas.create_oval(138,177, 140,179, fill="black", tags="hangman") # left pupil
		self.canvas.create_oval(157,175, 165,180, tags="hangman") # right eye
		self.canvas.create_oval(160,177, 162,179, fill="black", tags="hangman") # right pupil
		self.canvas.create_line(150,180, 147,187, tags="hangman") # nose
		self.canvas.create_line(147,187, 151,187, tags="hangman") # nose
		self.canvas.create_arc(165,185, 135,200, style="arc", extent=-160, width=2, tags="hangman") # smile
		self.canvas.create_polygon(120,300, 120,250, 110,260, 90,250, 115,218, 185,218, 210,250, 190,260, 180,250, 180,300, fill="red4", tags="hangman") # torso
		self.canvas.create_polygon(135,402, 110,400, 120,300, 180,300, 190,400, 165,402, 150,340, fill="navy", tags="hangman") # pants
		self.canvas.create_line(100,255, 95,265, width=7, tags="hangman") # (our) left arm upper
		self.canvas.create_line(93,263, 65,240, width=7, tags="hangman") # left arm lower
		self.canvas.create_line(200,255, 205,265, width=7, tags="hangman") # right arm upper
		self.canvas.create_line(207,263, 179,270, width=7, tags="hangman") # right arm lower
		self.canvas.create_polygon(165,402, 190,400, 210,402, 212,418, 167,418, tags="hangman") # right shoe, drawn from top-left of shoe
		self.canvas.create_polygon(135,402, 110,400, 90,402, 88,418, 132,418, tags="hangman") # left shoe, drawn from top-right of shoe
# -------------------------------------------------------------------------------------------
# Reset Methods
# -------------------------------------------------------------------------------------------
	def Choose_Word(self, *args, **kwargs):
		self.word = choice(self.word_list)
		self.word_display = " ".join(self.word)
		self.obscured_display = str("_ "*len(self.word))[:-1]

	def Remove_Hangman(self, *args, **kwargs):
		self.canvas.delete("hangman")

	def Restart_Displays(self, *args, **kwargs):
		self.solution_display_message.set(self.obscured_display)
		self.display_message.set("Guess the word!")

	def Enable_Buttons(self, *args, **kwargs):
		for button in self.buttons:
			button.config(state="normal")
		self.Bind_Buttons()

	def Reset_Variables(self, *args, **kwargs):
		self.obscured_display = str("_ "*len(self.word))[:-1]
		self.wrong_count = 1

	def Reset_Game(self, *args, **kwargs):
		self.Remove_Hangman()
		self.Reset_Variables()
		self.Choose_Word()
		self.Restart_Displays()
		self.Enable_Buttons()
		self.Disable_Reset_Button()

	def Close(self, *args, **kwargs):
		exit()

# -------------------------------------------------------------------------------------------
# Testing Methods
# -------------------------------------------------------------------------------------------
	def How_Many_Words(self, *args, **kwargs):
		self.display_message.set(str(len(self.word_list)))

# -------------------------------------------------------------------------------------------
# Actual Execution of App
# -------------------------------------------------------------------------------------------



app = Game()
app.Make_Game()
app.mainloop()