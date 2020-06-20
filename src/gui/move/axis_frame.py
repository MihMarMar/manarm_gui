import tkinter as tk


class AxisFrame(tk.Frame):
    _angle = 0

    def __init__(self, parent, **kwargs):
        self._min_angle = kwargs.pop("min_angle", -360)
        self._max_angle = kwargs.pop("max_angle", 360)
        _axis_name = kwargs.pop("axis_name", "Axis")
        super().__init__(parent, **kwargs)
        # todo add callbacks to button presses as kwargs

        self._label = tk.Label(self, text=_axis_name)
        self._label.pack(side=tk.LEFT, padx=(8, 8))

        self._left_button = tk.Button(self, command=self._left_btn_action)
        _left_btn_img = tk.PhotoImage(file="move/img/left-arrow-icon.png")
        self._left_button.config(image=_left_btn_img)
        self._left_button.image = _left_btn_img
        self._left_button.pack(side=tk.LEFT)

        self._angle_slider_indicator = tk.Scale(self, from_=self._min_angle, to=self._max_angle, orient=tk.HORIZONTAL)
        self._angle_slider_indicator.config(state=tk.DISABLED, takefocus=0)
        self._angle_slider_indicator.pack(side=tk.LEFT)

        self._right_button = tk.Button(self, command=self._right_btn_action)
        _right_btn_img = tk.PhotoImage(file="move/img/right-arrow-icon.png")
        self._right_button.config(image=_right_btn_img)
        self._right_button.image = _right_btn_img
        self._right_button.pack(side=tk.LEFT)

    # todo add hold functionality to the buttons
    def _left_btn_action(self):
        self.set_angle(self._angle - 10)
        print("Left btn clicked")
        # todo

    def _right_btn_action(self):
        self.set_angle(self._angle + 10)
        print("Right btn clicked")
        # todo

    def set_angle(self, angle):
        if not self._min_angle <= angle <= self._max_angle:
            raise ValueError(f"Given angle {angle}"
                             f" is not between {self._min_angle} and {self._max_angle}!")

        self._angle = angle
        self._angle_slider_indicator.config(state=tk.NORMAL)
        self._angle_slider_indicator.set(angle)
        self._angle_slider_indicator.config(state=tk.DISABLED)

        #  handle buttons enabled/disabled
        if self._angle == self._max_angle:
            self._right_button.config(state=tk.DISABLED)
        else:
            self._right_button.config(state=tk.NORMAL)

        if self._angle == self._min_angle:
            self._left_button.config(state=tk.DISABLED)
        else:
            self._left_button.config(state=tk.NORMAL)

    def get_angle(self):
        return self._angle_slider_indicator.get()
