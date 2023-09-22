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
timeout = 0.06
boolvar = False
string_wall_portrait = "☰"
string_wall_landspace = "║"

#### Ball
portrait = 1
bool_ball_portrait = True

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
    try:
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
    except KeyboardInterrupt:
        return

def __wall_landscape__():
    global wall_landscape, timeout, is_resize_landscape
    orig = wall_landscape
    try:
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
    except KeyboardInterrupt:
        return

def __random_place_bar__():
    global tmp_place
    try:
        while 1:
            tmp_place = random.randint(2, len(string_bar))
            time.sleep(1)
    except KeyboardInterrupt:
        return

def __load_portrait_wall_up__():
    global portrait_wall, __string_wall_portrait_below__
    timeout = globals()["timeout"] - int(globals()["timeout"] / 3)
    try:
        while 1:
            tmp = (wall_portrait + len(string_ball) + 2)
            if len(portrait_wall) < tmp:
                portrait_wall.extend([string_wall_portrait] * int(tmp-len(portrait_wall)))
                __string_wall_portrait_below__ = str(" " + string_wall_landspace + string_wall_portrait * (wall_portrait + len(string_ball) + 2)) + string_wall_landspace
            elif len(portrait_wall) > tmp:
                portrait_wall = portrait_wall[:tmp]
                __string_wall_portrait_below__ = str(" " + string_wall_landspace + string_wall_portrait * (wall_portrait + len(string_ball) + 2)) + string_wall_landspace

            time.sleep(timeout)
    except KeyboardInterrupt:
        return

# def __load_landscape_wall_left__():
#     global landscape_wall_left
#     timeout = globals()["timeout"] - int(globals()["timeout"] / 2)
#     try:
#         while 1:

#             time.sleep(timeout)
#     except KeyboardInterrupt:
#         return

# def __load_landscape_wall_right__():
#     pass

#### MAIN
stdout_2.hide_cursor()
stdout_2.write(color[-1])
stdout_2.write("\n>> Hello World!\n>> Hey! What are you doing?\n\n[Ctrl + C] -> EXIT\n\n")

try:
    __string_bar__ = color[-1] + string_bar
    __string_wall_portrait_below__ = str(" " + string_wall_landspace + string_wall_portrait * (wall_portrait + len(string_ball) + 2)) + string_wall_landspace
    portrait_wall = [string_wall_portrait] * (wall_portrait + len(string_ball) + 2)
    tmp_place = 2
    tmp_color = None
    threading.Thread(target=__auto_resize__).start()
    threading.Thread(target=__load_portrait_wall_up__).start()
    # threading.Thread(target=__load_landscape_wall_left__).start()
    # threading.Thread(target=__load_landscape_wall_right__).start()
    threading.Thread(target=__random_place_bar__).start()
    while 1:
        __string_wall_portrait__ = " " + string_wall_landspace + "".join(portrait_wall) + string_wall_landspace
        __string_wall_landscape__ = " " + string_wall_landspace + string_wall_landspace + " " * (wall_portrait+len(string_ball)) + string_wall_landspace + string_wall_landspace + "\n"

        stdout.write(__string_wall_portrait__ + "\n")
        tmp_color = random.choice(color[:-1])

        # Ball
        stdout.write(
            __string_wall_landscape__ * landscape
            + ( 
                " " 
                + string_wall_landspace
                + string_wall_landspace
                + " " * portrait
                + tmp_color 
                + string_ball
                + color[-1]
                + " " * (wall_portrait - portrait)
                + (f"{string_wall_landspace}{string_wall_landspace}" if wall_portrait + 1 > portrait else f"{string_wall_landspace}{string_wall_landspace}<<==") 
                + "\n"
            ) 
            + __string_wall_landscape__ * (wall_landscape - landscape)
        )

        # Bar
        tmp_value_bar = int(len(string_bar) / tmp_place)
        tmp_place_var = int(portrait - tmp_value_bar)
        stdout.write(
                " "
                + " " * tmp_place_var
                + __string_bar__
                + color[-1]
                + " " * (wall_portrait - portrait - tmp_value_bar)
                + "\n"
        )
        stdout.write(__string_wall_portrait_below__)

        if landscape > wall_landscape:
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
                    __string_bar__ = tmp_color + string_bar

                boolvar = not boolvar
            if boolvar:
                landscape -= 1
            else:
                landscape += 1

        # Ball
        if portrait > wall_portrait:
            portrait -= 1
        elif portrait < 0:
            portrait += 1
        else:
            if ((portrait == wall_portrait) and (not is_resize_portrait)) or (portrait == 0):
                # if bool_ball_portrait:
                #     # landscape_wall_left[landscape] = tmp_color + string_wall_landscape + color[-1]
                #     pass
                # else:
                #     # landscape_wall_right[landscape] = tmp_color + string_wall_landscape + color[-1]
                #     pass

                bool_ball_portrait = not bool_ball_portrait
            if bool_ball_portrait:
                portrait += 1
            else:
                portrait -= 1

        time.sleep(timeout)
        stdout.clear()
except KeyboardInterrupt:
    stdout.clear()
    stdout_2.clear()
    stdout_2.show_cursor()
    print("Created by KhanhNguyen9872!")
kill_process()
exit()