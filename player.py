from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def detect_collision(self, b):
        width_threshold = 24
        height_threshold = 22
        if abs(self.xcor() - b.xcor()) < width_threshold and abs(self.ycor() - b.ycor()) < height_threshold:
            print(f" X: {abs(self.xcor() - b.xcor())} Y:{abs(self.ycor() - b.ycor())}")
            return True
        return False


