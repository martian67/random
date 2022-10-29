from Text_to_MorseLED import *

txt = input("type text to convert to Morse Lights here: ")
spd = input("enter a number between 1 and 60 for LED speed: ")

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    try:
        while True:
            txt2morse(txt,spd)
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()