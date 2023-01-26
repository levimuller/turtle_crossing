import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=400, height=400)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.rt, "Right")
screen.onkey(player.lt, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect turtle reaching the top
    if player.ycor() > 175:
        player.reset_position()
        scoreboard.level_up()
        car_manager.speed_up()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
