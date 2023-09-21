# Import the required libraries
import math
import sys
from tkinter import *

sys.setrecursionlimit(1073741824)
prev_depth = 0
max_depth = 4

theta_pivot = 90

theta_left = 60
theta_right = 60

length = 350
length_ratio = 0.7
x0 = 960
y0 = 0
x1 = 960
y1 = y0 + length
colour = "#8BE9FD"
width = 10
width_ratio = 0.8


# Pan and Zoom ######################################
# Initialize canvas settings
canvas_scale = 1.0
canvas_scale_step = 0.1

canvas_x, canvas_y = 0, 0
step = 30

# Variable to track if key input is allowed
key_input_allowed = True


def allow_key_input():
    global key_input_allowed
    key_input_allowed = True


def zoom(event):
    global canvas_scale, key_input_allowed
    if not key_input_allowed:
        return

    key_input_allowed = False
    win.after(300, allow_key_input)  # Allow key input after 100ms delay

    if event.keysym == "equal":
        canvas_scale += canvas_scale_step
    elif event.keysym == "minus":
        canvas_scale -= canvas_scale_step
        if canvas_scale < canvas_scale_step:
            canvas_scale = canvas_scale_step

    canvas.scale(
        "all",
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        canvas_scale,
        canvas_scale,
    )


def move_canvas(event):
    global canvas_x, canvas_y, key_input_allowed
    if not key_input_allowed:
        return

    key_input_allowed = False
    win.after(300, allow_key_input)  # Allow key input after 100ms delay

    if event.keysym == "w":
        canvas_y += step
    elif event.keysym == "s":
        canvas_y -= step
    elif event.keysym == "a":
        canvas_x += step
    elif event.keysym == "d":
        canvas_x -= step

    canvas.scan_dragto(canvas_x, canvas_y, gain=1)


def init_win():
    global win
    win = Tk()
    win.title("Fractal Tree")
    win.attributes("-fullscreen", True)


def init_canvas():
    global canvas
    canvas = Canvas(win, background="#181818")
    canvas.pack(fill=BOTH, expand=True)

    canvas.bind("<KeyPress-minus>", zoom)
    canvas.bind("<KeyPress-equal>", zoom)  # 'equal' key for zooming in
    canvas.bind("<KeyPress>", move_canvas)
    canvas.focus_set()

    config_button = Button(
        canvas, text="config", command=open_slider_window, bg="#181818", fg="#FFF", bd=0
    )
    config_button.pack(anchor=NW, padx=15, pady=20)


###################################### Sliders ######################################
def update_theta_left(val):
    global theta_left
    theta_left = float(val)
    left_angle_label.config(text=f"Left Angle: {theta_left:.2f} degrees")
    update_tree()


def update_theta_right(val):
    global theta_right
    theta_right = float(val)
    right_angle_label.config(text=f"Right Angle: {theta_right:.2f} degrees")
    update_tree()


def update_theta_pivot(val):
    global theta_pivot
    theta_pivot = float(val)
    pivot_angle_label.config(text=f"pivot Angle: {theta_pivot:.2f} degrees")
    update_tree()


def delete_branches():
    new_num_branches = int(math.pow(2, max_depth) - 1)
    old_num_branches = int(math.pow(2, prev_depth) - 1)
    diff = old_num_branches - new_num_branches

    i = 0
    for i in range(diff):
        index = old_num_branches - i - 1
        tree[(index - 1) // 2].left = None
        tree[(index - 1) // 2].right = None

        canvas.delete(tree[index].line)
        tree.remove(tree[index])


def update_max_depth(val):
    global max_depth
    global prev_depth

    prev_depth = max_depth
    max_depth = int(val)
    max_depth_label.config(text=f"max branch depth: {max_depth}")
    if prev_depth > max_depth:
        delete_branches()
    else:
        add_tree()


###################################### Slider Window ######################################


def open_slider_window():
    global open_win
    slider_win = Toplevel()
    slider_win.title("Settings")
    slider_win.config(background="#535353")

    # Create the sliders and labels
    global left_angle_label
    left_angle_label = Label(
        slider_win,
        text=f"Left Angle: {theta_left:.2f}  degrees",
        background="#535353",
        fg="#fff",
    )
    left_angle_label.pack(padx=20, pady=5)
    slider_left = Scale(
        slider_win,
        from_=0,
        to=180,
        orient="horizontal",
        length=300,
        resolution=0.01,
        command=update_theta_left,
        sliderrelief=FLAT,
        showvalue=0,
        background="#535353",
        troughcolor="#dc143c",
        highlightbackground="#535353",
        highlightcolor="#535353",
        fg="#fff",
    )
    slider_left.set(theta_left)
    slider_left.pack(padx=20, pady=5)

    global right_angle_label
    right_angle_label = Label(
        slider_win,
        text=f"Right Angle: {theta_right:.2f} degrees",
        background="#535353",
        fg="#fff",
    )
    right_angle_label.pack(padx=20, pady=5)

    slider_right = Scale(
        slider_win,
        from_=0,
        to=180,
        orient="horizontal",
        length=300,
        resolution=0.01,
        command=update_theta_right,
        sliderrelief=FLAT,
        showvalue=0,
        background="#535353",
        troughcolor="#dc143c",
        highlightbackground="#535353",
        highlightcolor="#535353",
        fg="#fff",
    )
    slider_right.set(theta_right)
    slider_right.pack(padx=20, pady=5)

    global pivot_angle_label
    pivot_angle_label = Label(
        slider_win,
        text=f"pivot Angle: {theta_pivot:.2f} degrees",
        background="#535353",
        fg="#fff",
    )
    pivot_angle_label.pack(padx=20, pady=5)
    slider_pivot = Scale(
        slider_win,
        from_=0,
        to=180,
        orient="horizontal",
        length=300,
        resolution=0.01,
        command=update_theta_pivot,
        sliderrelief=FLAT,
        showvalue=0,
        background="#535353",
        troughcolor="#dc143c",
        highlightbackground="#535353",
        highlightcolor="#535353",
        fg="#fff",
    )
    slider_pivot.set(theta_pivot)
    slider_pivot.pack(padx=20, pady=5)

    global max_depth_label
    max_depth_label = Label(
        slider_win,
        text=f"max branch depth: {max_depth:.2f}",
        background="#535353",
        fg="#fff",
    )
    max_depth_label.pack(padx=20, pady=5)
    slider_max_depth = Scale(
        slider_win,
        from_=0,
        to=20,
        orient="horizontal",
        length=300,
        resolution=1,
        command=update_max_depth,
        sliderrelief=FLAT,
        showvalue=0,
        background="#535353",
        troughcolor="#dc143c",
        highlightbackground="#535353",
        highlightcolor="#535353",
        fg="#fff",
    )
    slider_max_depth.set(max_depth)
    slider_max_depth.pack(padx=20, pady=5)

    slider_win.mainloop()


###################################### Fractal Tree ######################################
class Branch:
    def __init__(self, parent, isLeft):
        self.parent = parent

        self.length = parent.length * length_ratio

        self.x0 = parent.x1
        self.y0 = parent.y1
        self.isLeft = isLeft
        if isLeft:
            self.theta = parent.theta + theta_left
            self.colour = "#8BE9FD"

        else:
            self.theta = parent.theta - theta_right
            self.colour = "#F99170"

        self.x1 = self.get_x1_l()
        self.y1 = self.get_y1_l()

        self.width = parent.width * width_ratio
        self.left = None
        self.right = None

    def get_x1_l(self):
        x1 = self.parent.x1 + self.length * math.cos(math.radians(self.theta))
        return x1

    def get_x1_r(self):
        x1 = self.parent.x1 - self.length * math.cos(math.radians(self.theta))
        return x1

    def get_y1_l(self):
        y1 = self.parent.y1 + self.length * math.sin(math.radians(self.theta))
        return y1

    def get_y1_r(self):
        y1 = self.parent.y1 + self.length * math.sin(math.radians(self.theta))
        return y1

    def draw_line(self):
        self.line = canvas.create_line(
            self.x0, self.y0, self.x1, self.y1, fill=self.colour, width=self.width
        )

    def update_branch(self):
        if self.isLeft:
            self.theta = self.parent.theta + theta_left
        else:
            self.theta = self.parent.theta - theta_right

        self.x0 = self.parent.x1
        self.y0 = self.parent.y1
        self.x1 = self.get_x1_l()
        self.y1 = self.get_y1_l()

        canvas.coords(self.line, self.x0, self.y0, self.x1, self.y1)


class Root:
    def __init__(self, x0, y0, x1, y1, theta, length, colour, width):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        self.theta = theta
        self.colour = colour
        self.width = width

        self.left = None
        self.right = None
        self.length = length

    def update_root(self, x0, y0, x1, y1, theta, length, colour, width):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        self.theta = theta
        self.colour = colour
        self.width = width

        self.length = length

    def draw_line(self):
        self.line = canvas.create_line(
            self.x0, self.y0, self.x1, self.y1, fill=self.colour, width=self.width
        )


def update_tree():
    global root
    for branch in tree:
        if branch == root:
            root.update_root(x0, y0, x1, y1, theta_pivot, length, colour, width)
        else:
            branch.update_branch()


def new_branch(i, isLeft):
    child = Branch(tree[int((i - 1) // 2)], isLeft)
    tree.append(child)
    child.draw_line()


def add_tree():
    len_tree = len(tree)
    num_branches = int(math.pow(2, max_depth) - 1)
    win.update()
    for i in range(len_tree, num_branches):
        if i % 2 == 0 and i != 0:  # Append left child
            new_branch(i, True)
        elif i % 2 != 0:  # Append right child
            new_branch(i, False)


def build_tree():
    global root
    num_branches = int(math.pow(2, max_depth) - 1)
    win.update()
    for i in range(num_branches):
        if not tree:
            root = Root(x0, y0, x1, y1, theta_pivot, length, colour, width)
            root.draw_line()
            tree.append(root)
            pass
        if i % 2 == 0 and i != 0:  # Append left child
            new_branch(i, True)
        elif i % 2 != 0:  # Append right child
            new_branch(i, False)


tree = []


def main():
    init_win()
    init_canvas()

    global win
    global root
    global tree

    build_tree()

    win.mainloop()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        # Catch ^C so it doesn't print traceback.
        sys.exit(0)
