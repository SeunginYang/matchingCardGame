import turtle as t
import random
import time

def find_card(x,y):
    min_idx = 0
    min_dis = 100

    for i in range(16):
        distance = turtles[i].distance(x,y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i

def play(x,y):
    global click_num
    global first_pick
    global second_pick
    global attempt
    global score

    if attempt == 12:
        t.goto(0, -60)       # 해당 좌표 위치에 
        t.write("Game Over", False, "center", ("",30, "bold")) # Game Over가 나타날 수 있게 작성
    else: 
        click_num += 1

t.bgcolor("pink")
t.setup(700,700)
t.up()
t.ht()
t.goto(0,280)
t.write("카드매칭게임", False, "center", ("", 30, "bold")) 

#터틀 객체 생성
turtles = []
pos_x = [-210, -70, 70, 210]
pos_y = [-250, -110, 30, 170]

for x in range(4):
    for y in range(4):
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.color("pink")
        new_turtle.speed(0)
        new_turtle.goto(pos_x[x], pos_y[y])
        turtles.append(new_turtle)


default_img = "images/default_img.gif"
t.addshape(default_img)

img_list = []
for i in range(8):
    img = f"images/img{i}.gif"
    t.addshape(img)
    img_list.append(img)
    img_list.append(img)
 
random.shuffle(img_list)
for i in range(16):
    turtles[i].shape(img_list[i])

time.sleep(5)             #5초간 보여주기 위한 시간 설정 

for i in range(16):
    turtles[i].shape(default_img)

click_num =0 # 클릭 횟수를 체크하는 함수 (매 2회 클릭마다 정답체크)
score = 0  # 점수 
attempt = 0  # 시도한 횟수
first_pick =""       # 첫 번째 클릭한 이미지
second_pick =""      # 두 번째 클릭한 이미지

t.onscreenclick(play)



t.done()
turtle.exitonclick()
input("Press any key to exit ...")