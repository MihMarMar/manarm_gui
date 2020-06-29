import Tkinter as Tk
from math import degrees

from axis_frame import AxisFrame
from src.ros_bridge.topic_subscribers import TopicSubscribers


class AxesPanel(Tk.Frame):
    _last_msg_seq = -1

    def __init__(self, parent, **kw):
        Tk.Frame.__init__(self, parent, **kw)
        self._axes_subscriber = TopicSubscribers().instance.axes_subscriber
        self._axes = []
        for i in range(6):
            self._axes.append(AxisFrame(self, axis_name=self.get_joint_name(i).replace('_', ' ')[:-5]))
            self._axes[i].pack()

        self.after(250, self.update_axis_values)

    def update_axis_values(self):
        if self._last_msg_seq == self._axes_subscriber.last_msg_seq:
            self.after(250, self.update_axis_values)
            return
        self._last_msg_seq = self._axes_subscriber.last_msg_seq

        for i in range(len(self._axes)):
            _, pos, vel, eff = self._axes_subscriber.return_joint_state(self.get_joint_name(i))
            self._axes[i].set_angle(degrees(pos))
        self.after(250, self.update_axis_values)

    @staticmethod
    def get_joint_name(index):
        joint_names = {
            0: 'elbow_joint',
            1: 'shoulder_pan_joint',
            2: 'shoulder_lift_joint',
            3: 'wrist_1_joint',
            4: 'wrist_2_joint',
            5: 'wrist_3_joint'
        }
        return joint_names.get(index, "Unrecognised index")
