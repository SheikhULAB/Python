
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_left():
    print("Turn left")
def move():
    print("Move")   
     
move()
turn_left()
move()
turn_right()
move()    
move()
turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()    
    move()
    turn_left()

jump()
jump()
jump()
jump()
jump()
jump()


for step in range(6):
    jump()
    