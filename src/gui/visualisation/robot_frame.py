import Tkinter as Tk

from PIL import Image, ImageTk

from src.ros_bridge.topic_subscribers import TopicSubscribers


class RobotFrame(Tk.Frame):
    _last_img_seq = 0

    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, kwargs)
        self._img_sub = TopicSubscribers().instance.image_subscriber
        h, w, n_chan = self._img_sub.cv_image.shape()
        self._img_container = Tk.Canvas(parent, width=w, height=h)
        self._img_container.pack()
        self.after(100, self.update_img)

    def update_img(self):
        if self._last_img_seq == self._img_sub.last_msg_seq:
            return
        self._last_img_seq = self._img_sub.last_msg_seq
        img = ImageTk.PhotoImage(image=Image.fromarray(self._img_sub.cv_image))
        self._img_container.create_image(0, 0, image=img, anchor=Tk.NW)
        self.after(100, self.update_img())
