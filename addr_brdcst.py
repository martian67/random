from Text_to_MorseLED import *

txt = 'github dot com fslash martian67 fslash encrypted dash data dash stream'
spd = 60

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    try:
        while True:
            txt2morse(txt,spd)
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()