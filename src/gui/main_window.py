from Tkinter import *

import rospy

from src.gui.move.move_frame import MoveFrame
from src.gui.visualisation.robot_frame import RobotFrame

form = Tk()
form.title("ManArm controller")
myLabel = Label(form, text="ManArm controller")
myLabel.pack()
move_frame = MoveFrame(form)
move_frame.pack(side=LEFT)
robot_frame = RobotFrame(form)
robot_frame.pack(side=LEFT)

# add notebook
try:
    form.mainloop()
except KeyboardInterrupt:
    rospy.signal_shutdown("Keyboard interrupt")
