import tkinter as tk
from random import choice
from sys import exit

class Game(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)    # initialize Tkinter while you're at it
        # TKinter Frames / Containers
        self.main_container = tk.Frame(self)
        self.canvas_container = tk.Frame(self)
        self.button_container = tk.Frame(self, bg="pale goldenrod")
        # UI variables for broad scope of accessibility
        self.canvas = None
        self.reset_button = None
        self.face_hidden_check = None
        self.left_cloud_hidden_check = None
        self.right_cloud_hidden_check = None
        self.cloud_button = None
        self.display_message = tk.StringVar()
        self.solution_display_message = tk.StringVar()
        self.buttons = []
        # Gameplay variable initialization
        self.letter_list = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
        self.word_list = None
        self.backup_word_list = ["pencil", "basket", "syzygy", "porcupine", "crawfish", "banana", "tumbleweed", "python", "gerrymander"]
        self.word = None
        self.word_display = None
        self.obscured_display = None
        self.wrong_count = 1
        self.bind('<Escape>', self.Close)
# -------------------------------------------------------------------------------------------
# Creation Methods
# -------------------------------------------------------------------------------------------
    def Create_Canvas(self, *args, **kwargs): 
        # Create canvas widget for drawing hangman
        self.canvas = tk.Canvas(self.canvas_container, width=500, height=500, bg="skyblue1")
        self.canvas.grid(column=1, row=1, columnspan=10)
        # Draw background elements
        self.Draw_Ground()
        self.Draw_Sun()
        self.Draw_Clouds()
        self.Draw_Gallows()
        self.Draw_Rope()
        self.Draw_Hidden_Hangman()
        self.Draw_Sun_Face()

    def Create_Main_Container(self, *args, **kwargs):
        """
        Build the whole gridspace, encompassing both Canvas and Button containers
        """
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
        """
        Create all letter buttons individually, add them to self.buttons, and place them in the grid
        """
        a_button = tk.Button(self.button_container, text="a", command=lambda : self.Check_Letter(a_button))
        b_button = tk.Button(self.button_container, text="b", command=lambda : self.Check_Letter(b_button))
        c_button = tk.Button(self.button_container, text="c", command=lambda : self.Check_Letter(c_button))
        d_button = tk.Button(self.button_container, text="d", command=lambda : self.Check_Letter(d_button))
        e_button = tk.Button(self.button_container, text="e", command=lambda : self.Check_Letter(e_button))
        f_button = tk.Button(self.button_container, text="f", command=lambda : self.Check_Letter(f_button))
        g_button = tk.Button(self.button_container, text="g", command=lambda : self.Check_Letter(g_button))
        h_button = tk.Button(self.button_container, text="h", command=lambda : self.Check_Letter(h_button))
        i_button = tk.Button(self.button_container, text="i", command=lambda : self.Check_Letter(i_button))
        j_button = tk.Button(self.button_container, text="j", command=lambda : self.Check_Letter(j_button))
        k_button = tk.Button(self.button_container, text="k", command=lambda : self.Check_Letter(k_button))
        l_button = tk.Button(self.button_container, text="l", command=lambda : self.Check_Letter(l_button))
        m_button = tk.Button(self.button_container, text="m", command=lambda : self.Check_Letter(m_button))
        n_button = tk.Button(self.button_container, text="n", command=lambda : self.Check_Letter(n_button))
        o_button = tk.Button(self.button_container, text="o", command=lambda : self.Check_Letter(o_button))
        p_button = tk.Button(self.button_container, text="p", command=lambda : self.Check_Letter(p_button))
        q_button = tk.Button(self.button_container, text="q", command=lambda : self.Check_Letter(q_button))
        r_button = tk.Button(self.button_container, text="r", command=lambda : self.Check_Letter(r_button))
        s_button = tk.Button(self.button_container, text="s", command=lambda : self.Check_Letter(s_button))
        t_button = tk.Button(self.button_container, text="t", command=lambda : self.Check_Letter(t_button))
        u_button = tk.Button(self.button_container, text="u", command=lambda : self.Check_Letter(u_button))
        v_button = tk.Button(self.button_container, text="v", command=lambda : self.Check_Letter(v_button))
        w_button = tk.Button(self.button_container, text="w", command=lambda : self.Check_Letter(w_button))
        x_button = tk.Button(self.button_container, text="x", command=lambda : self.Check_Letter(x_button))
        y_button = tk.Button(self.button_container, text="y", command=lambda : self.Check_Letter(y_button))
        z_button = tk.Button(self.button_container, text="z", command=lambda : self.Check_Letter(z_button))
        # Add all newly created buttons to list
        self.buttons.extend((a_button, b_button, c_button, d_button, e_button, f_button, g_button, h_button, 
            i_button, j_button, k_button, l_button, m_button, n_button, o_button, p_button, q_button, r_button, 
            s_button, t_button, u_button, v_button, w_button, x_button, y_button, z_button))
        self.Grid_Buttons()
        self.Bind_Buttons()

    def Grid_Buttons(self, *args, **kwargs):
        """
        Place each letter button in an appropriate spot in the grid
        """
        row = 9
        column = 1
        i = 0
        while i < len(self.buttons):
            while column <= 10:
                if i < len(self.buttons):
                    self.buttons[i].grid(row=row, column=column, padx=2, pady=2, ipadx=5, sticky="NESW")
                    column += 1
                else:
                    break
                i += 1                
            row += 1
            column = 1

    def Bind_Buttons(self, *args, **kwargs):
        """
        Connect buttons to keyboard input
        Note: Index numbers feel like a less pythonic way of doing this,
        but creating a dictionary for this function seems rather inefficient
        """
        try:
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
        except IndexError as err:
            print("Buttons list variable is missing an index, 0 to 25")
            print("Playing with no or limited keyboard input for letters")
            print("Error: ", err)

    def Create_Displays(self, *args, **kwargs):
        self.Setup_Solution_Display()
        self.Setup_Message_Display()
        self.Start_Displays()

    def Setup_Solution_Display(self, *args, **kwargs):
        solution_display = tk.Message(self.button_container, aspect=1000, textvariable=self.solution_display_message)
        solution_display.grid(row=7, column=1, columnspan=10)
        solution_display.config(bg="lightblue", font=('helvetica', 20), pady=20, padx=50, relief="ridge")

    def Setup_Message_Display(self, *args, **kwargs):
        self.display_message = tk.StringVar()
        message_display = tk.Message(self.button_container, aspect=1000, textvariable=self.display_message)
        message_display.grid(row=8, column=1, columnspan=10)
        message_display.config(bg="lightblue", font=('helvetica', 20), pady=20, padx=50, relief="ridge")

    def Create_Word_List(self, *args, **kwargs):
        """
        Extract strings from an external file to create a list of possible solutions
        File found at https://github.com/dolph/dictionary/find/master for this file
        """
        try:
            with open('ospd.txt') as file:
                self.word_list = [word.lower() for line in file for word in line.split()]
            file.close()
        except IOError as err:
            print("Word list file is missing or cannot be opened. Game > Create_Word_List")
            print("Error:", err)
            print("Instead we are using a pre-built, smaller word list.")
            self.word_list = self.backup_word_list

    def Make_Game(self, *args, **kwargs):
        self.Create_Main_Container()
        self.Create_Canvas_Container()
        self.Create_Canvas()
        self.Create_Button_Container()
        self.Create_Word_List()
        self.Choose_Word()
        self.Reset_Variables()
        self.Create_Letter_Buttons()
        self.Create_Reset_Button()
        self.Create_Displays()

    def Start_Displays(self, *args, **kwargs):
        self.solution_display_message.set(self.obscured_display)
        self.display_message.set("Welcome to TK Hangman!")

    def Create_Reset_Button(self, *args, **kwargs):
        btn_text = "RESET GAME"
        self.reset_button = tk.Button(self.button_container, text=btn_text, command=self.Reset_Game)
        self.reset_button.grid(row=11, column=8, columnspan=3, padx=2, pady=2, ipadx=5, sticky="NESW")
        self.Disable_Reset_Button()

# -------------------------------------------------------------------------------------------
# Gameplay Methods
# -------------------------------------------------------------------------------------------
    def Check_Letter(self, button, event=None, *args, **kwargs): # event=None is for key binding from Bind_Buttons.
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
            self.Draw_Hangman()
            self.Wrong_Answer()
            self.after(1000, self.Increase_Wrong_Count)
        else:
            self.Draw_Hangman()
            self.display_message.set("Correct Answer: "+self.word_display)
            self.Disable_Buttons()
            self.Enable_Reset_Button()

    def Increase_Wrong_Count(self, *args, **kwargs):
        self.wrong_count += 1

    def Wrong_Answer(self, *args, **kwargs):
        """
        Display the visual indicators that a wrong answer has been selected
        """
        self.display_message.set(str(self.wrong_count)+" WRONG.")
        self.after(1000, self.Update_Solution_Display) # more familiar time.sleep doesn't play nicely with tkinter; this is rough equivalent
        self.after(1000, self.Update_Message_Display)

    def Update_Solution_Display(self, *args, **kwargs):
        self.solution_display_message.set(self.obscured_display)

    def Update_Message_Display(self, *args, **kwargs):
        try:
            if self.wrong_count < 3:
                self.display_message.set(f"{str(5-self.wrong_count)} guesses remaining!")
            elif self.wrong_count < 4:
                self.display_message.set(f"Only {str(5-self.wrong_count)} guesses left!")
            else:
                self.display_message.set("One guess left! Make it count!")
        except:
            print("Display message update failed: Update_Message_Display")

    def Draw_Hangman(self, *args, **kwargs):
        try:
            if self.wrong_count == 1:
                self.canvas.itemconfig("head", state="normal")
            elif self.wrong_count == 2:
                self.canvas.itemconfig("torso", state="normal")
            elif self.wrong_count == 3:
                self.canvas.itemconfig("pants", state="normal")
            elif self.wrong_count == 4:
                self.canvas.itemconfig("limbs", state="normal")
            elif self.wrong_count >= 5: # face / game over
                self.canvas.itemconfig("face", state="normal")
            else:
                self.display_message.set("wrong_count variable outside of expected range")
                # This probably doesn't need a try/except given I've handled all valueerror issues in the if
        except (ValueError) as err:
            print("wrong_count variable outside of expected range")
            print("Error: ", err)
            raise err

    def Check_For_Win(self, *args, **kwargs):
        if "_" not in self.obscured_display:
            self.display_message.set("You won!")
            self.Remove_Hangman()
            self.Disable_Buttons()
            self.Enable_Reset_Button()
            self.Draw_Free_Hangman()
        else:
            pass

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

    def Toggle_Sun_Face(self, *args, **kwargs):
        if self.canvas.itemcget(self.face_hidden_check, "state") == "hidden":
            self.canvas.itemconfig("sunface", state="normal")
        elif self.canvas.itemcget(self.face_hidden_check, "state") == "normal":
            self.canvas.itemconfig("sunface", state="hidden")

    def Toggle_Right_Cloud(self, *args, **kwargs):
        if self.canvas.itemcget(self.right_cloud_hidden_check, "state") == "normal":
            self.canvas.itemconfig("rightcloud", state="hidden")
        self.Clouds_Button_Appearance()

    def Toggle_Left_Cloud(self, *args, **kwargs):
        if self.canvas.itemcget(self.left_cloud_hidden_check, "state") == "normal":
            self.canvas.itemconfig("leftcloud", state="hidden")
        self.Clouds_Button_Appearance()

    def Clouds_Button_Appearance(self, *args, **kwargs):
        if self.canvas.itemcget(self.left_cloud_hidden_check, "state") == "hidden" and self.canvas.itemcget(self.right_cloud_hidden_check, "state") == "hidden":
            if self.cloud_button == None:
                self.cloud_button = tk.Button(self.button_container, text="I <3 Clouds", command=self.Bring_Clouds_Back)
            self.cloud_button.grid(row=7, column=9, columnspan=2, padx=2, pady=2, ipadx=5, sticky="NESW")
        else:
            pass

    def Bring_Clouds_Back(self, *args, **kwargs):
        self.canvas.itemconfig("leftcloud", state="normal")
        self.canvas.itemconfig("rightcloud", state="normal")
        self.cloud_button.grid_forget()

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
        sun = self.canvas.create_oval(50, 50, 125, 125, fill="goldenrod", tags="setting") # Mr. Sun
        self.canvas.tag_bind(sun, '<Button-1>', self.Toggle_Sun_Face)

    def Draw_Sun_Face(self, *args, **kwargs):
        self.face_hidden_check = self.canvas.create_oval(70,75, 85,87, fill="black", tags="sunface", state="hidden") # left lens create_oval
        self.canvas.create_polygon(70,81, 70,75, 86,75, 86,81, fill="black", tags="sunface", state="hidden") # left lens rectangle
        self.canvas.create_oval(110,75, 95,87, fill="black", tags="sunface", state="hidden") # right lens oval
        self.canvas.create_polygon(111,81, 111,75, 95,75, 95,81, fill="black", tags="sunface", state="hidden") # right lens rectangle
        self.canvas.create_line(70,75, 110,75, tags="sunface", state="hidden") # upper bridge
        self.canvas.create_line(88,78, 93,78, tags="sunface", state="hidden") # lower bridge mid
        self.canvas.create_line(88,78, 86,80, tags="sunface", state="hidden") # lower bridge left
        self.canvas.create_line(93,78, 95,80, tags="sunface", state="hidden") # lower bridge right
        self.canvas.create_arc(70,90, 110,110, style="arc", extent=-180, width=2, tags="sunface", state="hidden")

    def Draw_Clouds(self, *args, **kwargs):
        self.left_cloud_hidden_check = self.canvas.create_oval(330, 38, 380, 54, fill="white", outline="white", tags="leftcloud", state="normal") # cloud (left)
        self.canvas.create_oval(360, 23, 420, 60, fill="white", outline="white", tags="leftcloud", state="normal") # cloud (left)
        self.canvas.create_oval(320, 30, 380, 50, fill="white", outline="white", tags="leftcloud", state="normal") # cloud (left)
        self.canvas.create_oval(380, 30, 460, 50, fill="white", outline="white", tags="leftcloud", state="normal") # cloud (left)
        self.right_cloud_hidden_check = self.canvas.create_oval(30, 138, 80, 154, fill="white", outline="white", tags="rightcloud", state="normal") # cloud (right)
        self.canvas.create_oval(60, 123, 120, 160, fill="white", outline="white", tags="rightcloud", state="normal") # cloud (right)
        self.canvas.create_oval(20, 140, 80, 150, fill="white", outline="white", tags="rightcloud", state="normal") # cloud (right)
        self.canvas.create_oval(80, 130, 160, 150, fill="white", outline="white", tags="rightcloud", state="normal") # cloud (right)
        self.canvas.tag_bind("rightcloud", '<Button-1>', self.Toggle_Right_Cloud)
        self.canvas.tag_bind("leftcloud", '<Button-1>', self.Toggle_Left_Cloud)

    def Draw_Hidden_Hangman(self, *args, **kwargs):
        self.canvas.create_oval(220,102, 280, 162, fill="blanched almond", tags="hangman, head", state="hidden") # Draw Head
        self.canvas.create_polygon(220,250, 220,200, 210,210, 190,200, 215,168, 285,168, 310,200, 290,210, 280,200, 280,250, fill="red4", tags="hangman, torso", state="hidden") # Shirt (torso) - top of shirt is center coords (215,168 to 285,168)
        self.canvas.create_polygon(235,352, 210,350, 220,250, 280,250, 290,350, 265,352, 250,290, fill="navy", tags="hangman, pants", state="hidden") # pants (legs) - center coords are top of pants
        self.canvas.create_line(200,205, 195,215, width=7, tags="hangman, limbs", state="hidden") # (our) left arm upper
        self.canvas.create_line(193,213, 220,220, width=7, tags="hangman, limbs", state="hidden") # left arm lower
        self.canvas.create_line(300,205, 305,215, width=7, tags="hangman, limbs", state="hidden") # right arm upper
        self.canvas.create_line(307,213, 279,220, width=7, tags="hangman, limbs", state="hidden") # right arm lower
        self.canvas.create_polygon(265,352, 290,350, 310,352, 312,368, 267,368, tags="hangman, limbs", state="hidden") # right shoe, drawn from top-left of shoe
        self.canvas.create_polygon(235,352, 210,350, 190,352, 188,368, 232,368, tags="hangman, limbs", state="hidden") # left shoe, drawn from top-right of shoe
        self.canvas.create_line(235,130, 240,135, width=2, tags="hangman, face", state="hidden") # (our) right eye pt1
        self.canvas.create_line(235,135, 240,130, width=2, tags="hangman, face", state="hidden") # right eye pt2
        self.canvas.create_line(265,130, 260,135, width=2, tags="hangman, face", state="hidden") # left eye pt1
        self.canvas.create_line(265,135, 260,130, width=2, tags="hangman, face", state="hidden") # left eye pt2
        self.canvas.create_arc(235,145, 265,155, extent=180, style="arc", width=2, tags="hangman, face", state="hidden") # frown
        self.canvas.create_arc(250,140, 255,155, extent=-180, style="arc", fill="tomato2", outline="tomato3", tags="hangman, face", state="hidden") # tongue

    def Draw_Free_Hangman(self, *args, **kwargs):
        self.canvas.create_polygon(155,220, 145,220, 145,210, 155,210, fill="blanched almond", tags="freehangman") # neck
        self.canvas.create_oval(120,152, 180,212, fill="blanched almond", tags="freehangman") # head
        self.canvas.create_oval(135,175, 143,180, tags="freehangman") # (our) left eye
        self.canvas.create_oval(138,177, 140,179, fill="black", tags="freehangman") # left pupil
        self.canvas.create_oval(157,175, 165,180, tags="freehangman") # right eye
        self.canvas.create_oval(160,177, 162,179, fill="black", tags="freehangman") # right pupil
        self.canvas.create_line(150,180, 147,187, tags="freehangman") # nose
        self.canvas.create_line(147,187, 151,187, tags="freehangman") # nose
        self.canvas.create_arc(165,185, 135,200, style="arc", extent=-160, width=2, tags="freehangman") # smile
        self.canvas.create_polygon(120,300, 120,250, 110,260, 90,250, 115,218, 185,218, 210,250, 190,260, 180,250, 180,300, fill="red4", tags="freehangman") # torso
        self.canvas.create_polygon(135,402, 110,400, 120,300, 180,300, 190,400, 165,402, 150,340, fill="navy", tags="freehangman") # pants
        self.canvas.create_line(100,255, 95,265, width=7, tags="freehangman") # (our) left arm upper
        self.canvas.create_line(93,263, 65,240, width=7, tags="freehangman") # left arm lower
        self.canvas.create_line(200,255, 205,265, width=7, tags="freehangman") # right arm upper
        self.canvas.create_line(207,263, 179,270, width=7, tags="freehangman") # right arm lower
        self.canvas.create_polygon(165,402, 190,400, 210,402, 212,418, 167,418, tags="freehangman") # right shoe, drawn from top-left of shoe
        self.canvas.create_polygon(135,402, 110,400, 90,402, 88,418, 132,418, tags="freehangman") # left shoe, drawn from top-right of shoe

# -------------------------------------------------------------------------------------------
# Reset Methods
# -------------------------------------------------------------------------------------------
    def Choose_Word(self, *args, **kwargs):
        self.word = choice(self.word_list)
        self.word_display = " ".join(self.word)
        self.obscured_display = str("_ "*len(self.word))[:-1]

    def Remove_Hangman(self, *args, **kwargs):
        # self.canvas.delete("hangman") # This no longer works and I can't find a clear answer as to why
        self.canvas.delete("freehangman")
        self.canvas.itemconfig("head", state="hidden")
        self.canvas.itemconfig("torso", state="hidden")
        self.canvas.itemconfig("pants", state="hidden")
        self.canvas.itemconfig("limbs", state="hidden")
        self.canvas.itemconfig("face", state="hidden")

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
        self.Choose_Word()
        self.Reset_Variables()
        self.Restart_Displays()
        self.Enable_Buttons()
        self.Disable_Reset_Button()

    def Close(self, *args, **kwargs):
        exit()

# -------------------------------------------------------------------------------------------
# Execution and Mainloop
# -------------------------------------------------------------------------------------------

app = Game()
app.Make_Game()
app.mainloop()