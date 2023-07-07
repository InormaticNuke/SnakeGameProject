import turtle as t
import random as rd

t.bgcolor('#10c988')

snake = t.Turtle()
snake.shape('square')
snake.color('black')
snake.speed(0)
snake.penup() 
snake.hideturtle()

food = t.Turtle()
food_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('circle',food_shape)
food.color('red')
food.penup()
food.hideturtle()
food.speed()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('SPACE TO START',align='center',font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = snake.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

def game_over():
    snake.color('#10c988')
    food.color('#10c988')
    t.penup()
    t.hideturtle()
    t.write('GG',align='center' , font=('Aerial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score),align = 'center',font=('Arial',40,'bold'))

def place_food():
    food.hideturtle()
    food.setx(rd.randint(-200,200))
    food.sety(rd.randint(-200,200))
    food.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    snake_speed = 2
    snake_length = 3
    snake.shapesize(1,snake_length,1)
    snake.showturtle()
    display_score(score)
    place_food()

    while True:
        snake.forward(snake_speed)
        if snake.distance(food)<20:
            place_food()
            snake_length = snake_length + 1
            snake.shapesize(1,snake_length,1)
            snake_speed = snake_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def move_down():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def move_left():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def move_right():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()