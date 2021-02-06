import xbox
joy = xbox.Joystick()

print("Xbox controller sample: Press Back button to exit")
while not joy.Back():
    if joy.connected():
        #print(joy.dpadUp())
        #joy.dpadDown()
        #joy.dpadLeft()
        #joy.dpadRight(
        print(joy.leftX())
        #joy.leftY()
        #joy.rightTrigger()
        #print(joy.A())
        #joy.B()
        #joy.X()
        #joy.Y()
        #joy.dpadUp()
        #joy.dpadDown()
        #joy.dpadLeft()
        #joy.dpadRight()
print("disconnected")

joy.close()
