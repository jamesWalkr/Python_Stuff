from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("data.txt", mode='r')as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    # def get_high_score(self):
    #     with open("data.txt", mode='r')as file:
    #         content = file.read()
    #         self.high_score = int(content)
    #         return self.high_score

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
