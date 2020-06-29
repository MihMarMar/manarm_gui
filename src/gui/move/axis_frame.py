import Tkinter as Tk


class AxisFrame(Tk.Frame):

    def __init__(self, parent, **kwargs):
        self._angle = 0
        self._min_angle = kwargs.pop("min_angle", -360)
        self._max_angle = kwargs.pop("max_angle", 360)
        _axis_name = kwargs.pop("axis_name", "Axis")
        Tk.Frame.__init__(self, parent, **kwargs)
        # todo add callbacks to button presses as kwargs

        self._label = Tk.Label(self, text=_axis_name)
        self._label.pack(side=Tk.LEFT, padx=(8, 8))

        self._left_button = Tk.Button(self, command=self._left_btn_action)
        _left_btn_img = Tk.PhotoImage(file="move/img/left-arrow-icon.png")
        self._left_button.config(image=_left_btn_img)
        self._left_button.image = _left_btn_img
        self._left_button.pack(side=Tk.LEFT)

        self._angle_slider_indicator = Tk.Scale(self, from_=self._min_angle, to=self._max_angle, orient=Tk.HORIZONTAL)
        self._angle_slider_indicator.config(state=Tk.DISABLED, takefocus=0)
        self._angle_slider_indicator.pack(side=Tk.LEFT)

        self._right_button = Tk.Button(self, command=self._right_btn_action)
        _right_btn_img = Tk.PhotoImage(file="move/img/right-arrow-icon.png")
        self._right_button.config(image=_right_btn_img)
        self._right_button.image = _right_btn_img
        self._right_button.pack(side=Tk.LEFT)

    # todo add hold functionality to the buttons
    def _left_btn_action(self):
        print("Left btn clicked")
        # todo

    def _right_btn_action(self):
        print("Right btn clicked")
        # todo

    def set_angle(self, angle):
        if not self._min_angle <= angle <= self._max_angle:
            raise ValueError("Given angle {}".format(angle) +
                             " is not between {} and {}!".format(self._min_angle, self._max_angle))

        self._angle = angle
        self._angle_slider_indicator.config(state=Tk.NORMAL)
        self._angle_slider_indicator.set(angle)
        self._angle_slider_indicator.config(state=Tk.DISABLED)

        #  handle buttons enabled/disabled
        if self._angle == self._max_angle:
            self._right_button.config(state=Tk.DISABLED)
        else:
            self._right_button.config(state=Tk.NORMAL)

        if self._angle == self._min_angle:
            self._left_button.config(state=Tk.DISABLED)
        else:
            self._left_button.config(state=Tk.NORMAL)

    def get_angle(self):
        return self._angle_slider_indicator.get()
