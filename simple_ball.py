import khanhnguyen9872
import time
import random
import threading

is_resize_portrait = False
is_resize_landscape = False

color = ["\033[94m", "\033[96m", "\033[35m", "\033[36m", "\033[92m", "\033[93m", "\033[91m", "\033[95m", "\033[0m"]

stdout = khanhnguyen9872.stdout()
stdout_2 = khanhnguyen9872.stdout()

string_ball = "●"
string_bar = "▀▀▀▀▀"

wall_portrait = random.randint(len(string_bar)+1, 31)
wall_landscape = random.randint(3, 13)

landscape = wall_landscape
timeout = 0.05
boolvar = False
string_wall_portrait = "☰"
string_wall_landsp = "║"

#### Ball
point = 0
combo = 0
portrait = 1
bool_ball_portrait = True
is_run_ball = 1

def kill_process():
    if hasattr(__import__('signal'), 'SIGKILL'):
        __import__('os').kill(__import__('os').getpid(), __import__('signal').SIGKILL)
    else:
        __import__('os').kill(__import__('os').getpid(), __import__('signal').SIGABRT)
    exit()

### AUTO RESIZE
def __auto_resize__():
    threading.Thread(target=__wall_portrait__).start()
    threading.Thread(target=__wall_landscape__).start()

def __wall_portrait__():
    global wall_portrait, timeout, is_resize_portrait
    orig = wall_portrait
    time.sleep(3)
    while 1:
        if random.randint(0, 1):
            orig = random.randint(4, 35)
            is_resize_portrait = True
            while orig != wall_portrait:
                if orig > wall_portrait:
                    wall_portrait += 1
                elif orig < wall_portrait:
                    wall_portrait -= 1
                time.sleep(timeout + 0.05)
            is_resize_portrait = False
        time.sleep(3)

def __wall_landscape__():
    global wall_landscape, timeout, is_resize_landscape
    orig = wall_landscape
    time.sleep(3)
    while 1:
        if random.randint(0, 1):
            orig = random.randint(2, 15)
            is_resize_landscape = True
            while orig != wall_landscape:
                if orig > wall_landscape:
                    wall_landscape += 1
                elif orig < wall_landscape:
                    wall_landscape -= 1
                time.sleep(timeout + 0.05)
            is_resize_landscape = False
        time.sleep(3)

def __random_place_bar__():
    global tmp_place
    while 1:
        tmp_place = random.randint(2, len(string_bar))
        time.sleep(1)

def __random_speed_ball__():
    global is_run_ball
    while 1:
        is_run_ball = random.randint(0, 1)
        time.sleep(1)

def __load_portrait_wall_up__():
    global portrait_wall, __string_wall_portrait_below__, string_wall_landspace_left, string_wall_landspace_right, string_wall_landsp
    timeout = globals()["timeout"] - int(globals()["timeout"] / 3)
    while 1:
        tmp = (wall_portrait + len(string_ball) + 2)
        if len(portrait_wall) < tmp:
            portrait_wall.extend([string_wall_portrait] * int(tmp-len(portrait_wall)))
            __string_wall_portrait_below__ = str(" " + string_wall_landspace_left + string_wall_portrait * (wall_portrait + len(string_ball) + 2)) + string_wall_landspace_right
        elif len(portrait_wall) > tmp:
            portrait_wall = portrait_wall[:tmp]
            __string_wall_portrait_below__ = str(" " + string_wall_landspace_left + string_wall_portrait * (wall_portrait + len(string_ball) + 2)) + string_wall_landspace_right

        time.sleep(timeout)

#### MAIN
stdout_2.hide_cursor()
stdout_2.write(color[-1])
stdout_2.write("\n>> Hello World!\n>> Hey! What are you doing?\n\n[Ctrl + C] -> EXIT\n\n")

try:
    __string_bar__ = color[-1] + string_bar
    string_wall_landspace_left = string_wall_landsp
    string_wall_landspace_right = string_wall_landsp
    __string_wall_portrait_below__ = str(" " + string_wall_landspace_left + string_wall_portrait * (wall_portrait + len(string_ball) + 2)) + string_wall_landspace_right
    portrait_wall = [string_wall_portrait] * (wall_portrait + len(string_ball) + 2)
    tmp_place = 2
    tmp_color = None
    threading.Thread(target=__auto_resize__).start()
    threading.Thread(target=__load_portrait_wall_up__).start()
    threading.Thread(target=__random_speed_ball__).start()
    threading.Thread(target=__random_place_bar__).start()

    while 1:
        __string_wall_portrait__ = " " + string_wall_landspace_left + "".join(portrait_wall) + string_wall_landspace_right
        __string_wall_landscape__ = " " + string_wall_landspace_left + string_wall_landspace_left + " " * (wall_portrait+len(string_ball)) + string_wall_landspace_right + string_wall_landspace_right + "\n"

        tmp_color = random.choice(color[:-1])

        ball_output = str(
            __string_wall_landscape__ * landscape
            + ( 
                " " 
                + string_wall_landspace_left
                + string_wall_landspace_left
                + " " * portrait
                + tmp_color 
                + string_ball
                + color[-1]
                + " " * (wall_portrait - portrait)
                + (f"{string_wall_landspace_right}{string_wall_landspace_right}" if wall_portrait + 1 > portrait else f"{string_wall_landspace_right}{string_wall_landspace_right}<<==") 
                + "\n"
            ) 
            + __string_wall_landscape__ * (wall_landscape - landscape)
        )

        tmp_p = (wall_portrait+len(string_ball))
        point_output = str(
            "| SCORE: {} | Combo: {} |".format(point, combo)
        )

        if len(point_output) >= tmp_p:
            tmp_p = ""
        else:
            tmp_p = " " * int(tmp_p/5)

        point_output = "\n\n" + tmp_p + point_output

        tmp_value_bar = int(len(string_bar) / tmp_place)
        tmp_place_var = int(portrait - tmp_value_bar)

        bar_output = str(
            " "
            + " " * tmp_place_var
            + __string_bar__
            + color[-1]
            + " " * (wall_portrait - portrait - tmp_value_bar)
            + "\n"
        )

        final_output = str(__string_wall_portrait__ + "\n" + ball_output + bar_output + __string_wall_portrait_below__ + point_output)

        time.sleep(timeout)
        stdout.clear()
        stdout.write(final_output)

        if wall_landscape + 1 <= landscape:
            landscape -= 2
            if not boolvar:
                boolvar = not boolvar
        elif landscape > wall_landscape:
            landscape -= 1
        elif landscape < 0:
            landscape += 1
        else:
            if ((landscape == wall_landscape) and (not is_resize_landscape)) or (landscape == 0):
                if boolvar:
                    try:
                        portrait_wall[portrait:portrait+len(string_ball)] = [tmp_color + string_wall_portrait + color[-1]] * len(string_ball)
                    except IndexError:
                        portrait_wall[portrait] = tmp_color + string_wall_portrait + color[-1]
                else:
                    combo += 1
                    point += 3 + int(combo / 2)
                    __string_bar__ = tmp_color + string_bar

                boolvar = not boolvar
            if boolvar:
                landscape -= 1
            else:
                landscape += 1

        # Ball
        if wall_portrait + 1 <= portrait:
            portrait -= 2
            if bool_ball_portrait:
                bool_ball_portrait = not bool_ball_portrait
        elif portrait > wall_portrait:
            portrait -= 1
        elif portrait < 0:
            portrait += 1
        else:
            if ((portrait == wall_portrait) and (not is_resize_portrait)) or (portrait == 0):
                if not bool_ball_portrait:
                    string_wall_landspace_left = tmp_color + string_wall_landsp + color[-1]
                else:
                    string_wall_landspace_right = tmp_color + string_wall_landsp + color[-1]
                bool_ball_portrait = not bool_ball_portrait

            if is_run_ball:
                if bool_ball_portrait:
                    portrait += 1
                else:
                    portrait -= 1
            else:
                is_run_ball = 1

except KeyboardInterrupt:
    stdout.clear()
    stdout_2.clear()
    stdout_2.show_cursor()
    print("Created by KhanhNguyen9872!")
kill_process()
exit()