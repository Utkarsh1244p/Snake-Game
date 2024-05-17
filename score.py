from turtle import Turtle, Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.up()
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.update_score()
        # self.show_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font= ("Arial", 24, "normal"), align= "center")

    def game_over(self):
        Screen().clear()
        Screen().bgcolor("black")
        self.goto(0,0)
        self.write("Game Over", font= ("Arial", 24, "normal"), align= "center")
        self.goto(0, -40)
        self.write(f"Score: {self.score}", font= ("Arial", 20, "normal"), align= "center")
        

    # def show_score(self):
    #     self.write(f"Score: {self.score}", font= ("Arial", 20, "bold"), align= "center")
