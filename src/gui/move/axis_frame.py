import tkinter as tk


class AxisFrame(tk.Frame):
    angle = 0

    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent)
        self.min_angle = kwargs.get("min_angle", -360)
        self.max_angle = kwargs.get("max_angle", 360)
        axis_name = kwargs.get("name", "Axis")
        # todo add callbacks to button presses as kwargs

        self.label = tk.Label(self, text=axis_name)
        self.label.pack(side=tk.LEFT, padx=(8, 8))

        self.left_button = tk.Button(self)
        left_btn_img = tk.PhotoImage(file="move/img/left-arrow-icon.png")
        self.left_button.config(image=left_btn_img)
        self.left_button.image = left_btn_img
        self.left_button.bind(sequence="<Button-1>", func=self.left_btn_action)
        self.left_button.pack(side=tk.LEFT)

        self.angle_slider_indicator = tk.Scale(self, from_=-720, to=720, orient=tk.HORIZONTAL)
        self.angle_slider_indicator.config(state=tk.DISABLED, takefocus=0)
        self.angle_slider_indicator.pack(side=tk.LEFT)

        self.right_button = tk.Button(self)
        right_btn_img = tk.PhotoImage(file="move/img/right-arrow-icon.png")
        self.right_button.config(image=right_btn_img)
        self.right_button.image = right_btn_img
        self.right_button.bind(sequence="<Button-1>", func=self.right_btn_action)
        self.right_button.pack(side=tk.LEFT)

    # todo add hold functionality to the buttons
    def left_btn_action(self, event):
        print("Left btn clicked")
        # todo

    def right_btn_action(self, event):
        print("Right btn clicked")
        # todo

    def set_angle(self, angle):
        if not self.min_angle <= angle <= self.max_angle:
            raise ValueError(f"Given angle {angle}"
                             f" is not between {self.min_angle} and {self.max_angle}!")
        self.angle_slider_indicator.config(state=tk.ACTIVE)
        self.angle_slider_indicator.set(angle)
        self.angle_slider_indicator.config(state=tk.DISABLED)

    def get_angle(self):
        return self.angle_slider_indicator.get()
