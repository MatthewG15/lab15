#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4
didWeHit = False


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=1)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
		
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "red")
		self.down.grid(row=1,column=1)
					
		# "Bind" an action to the first button												
		self.down.bind("<Button-1>", self.moveDown)
		
		self.Left = Button(self.myContainer1)
		self.Left.configure(text="Left", background= "purple")
		self.Left.grid(row=1,column=0)
		
		# "Bind" an action to the first button												
		self.Left.bind("<Button-1>", self.moveLeft)
		
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "blue")
		self.right.grid(row=1,column=2)
					
		# "Bind" an action to the first button												
		self.right.bind("<Button-1>", self.moveright)
					
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
		global player
		global drawpad
                drawpad.move(player,0,-10)
    
    	
	def moveDown(self, event):   
		global player
		global drawpad
                drawpad.move(player,0,10)
                
        	
	def moveLeft(self, event):   
		global player
		global drawpad
                drawpad.move(player,-10,0)    
                
        def moveright(self, event):   
		global player
		global drawpad
                drawpad.move(player,10,0)                   
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    
	    # Insert the code here to make the target move, bouncing on the edges    

            global direction
            x1, y1, x2, y2 = drawpad.coords(target)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(target,-480,0)
            elif x1 < 0:
                direction = 5
            drawpad.move(target,direction,0)
            drawpad.after(4, self.animate)    
	        
            
            
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            if didWeHit == True:
                direction = 0
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
	        global drawpad
                global player
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)
                x1, y1, x2, y2 = drawpad.coords(target)
                Px1, Py1, Px2, Py2 = drawpad.coords(player)
                # Do your if statement - remember to return True if successful!                
           	if (Px1 > x1 and Px2 < x2)and(Py1 > y1 and Py2 < y2):
           	        self.target.configure(fill = "red")
           	        return True
myapp = MyApp(root)
root.mainloop()