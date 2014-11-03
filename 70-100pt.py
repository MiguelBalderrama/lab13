#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
circle = drawpad.create_oval(100, 100, 140, 140, fill='green')
circle2 = drawpad.create_oval(500, 200, 540, 240, fill='green')
circle3 = drawpad.create_oval(1000, 300, 1040, 340, fill='green')
direction = 1
direction2 = 1
direction3 = 1
def animate():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)
    if x2 > drawpad.winfo_width(): 
        direction = - 10
    elif x1 < 0:
        direction = 10
    #Move our oval object by the value of direction
    drawpad.move(circle,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(5, animate)
def animate2():
    global direction2
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle2)
    if x2 > drawpad.winfo_width(): 
        direction2 = - 10
    elif x1 < 0:
        direction2 = 10
    #Move our oval object by the value of direction
    drawpad.move(circle2,direction2,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(5, animate2)
def animate3():
    global direction3
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle3)
    if x2 > drawpad.winfo_width(): 
        direction3 = - 10
    elif x1 < 0:
        direction3 = 10
    #Move our oval object by the value of direction
    drawpad.move(circle3,direction3,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(5, animate3)

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="  up  ", background= "green")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.button2 = Button(self.myContainer1)
	    self.button2.configure(text="down", background= "green")
	    self.button2.grid(row=2,column=1)
	    self.button2.bind("<Button-1>", self.button2Click)
	    self.up.bind("<Button-1>", self.upClicked)
       	    self.button3 = Button(self.myContainer1)
	    self.button3.configure(text="left", background= "green")
	    self.button3.grid(row=1,column=0)
	    self.button3.bind("<Button-1>", self.button3Click)
       	    self.button4 = Button(self.myContainer1)
	    self.button4.configure(text="right", background= "green")
	    self.button4.grid(row=1,column=2)
	    self.button4.bind("<Button-1>", self.button4Click)
      	    self.button5 = Button(self.myContainer1)
	    self.button5.configure(text="          ", background= "green")
	    self.button5.grid(row=1,column=1)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)

        def button2Click(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   
	def button3Click(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   
	def button4Click(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
   
app = MyApp(root)
animate()
animate2()
animate3()	
root.mainloop()