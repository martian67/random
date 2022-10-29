####### Text to Morse Code Tones or NATO phonetic language
# 1) import and establish the dictionary of symbols
# 2) ask for text (possibly voice in the future) input
# 3) convert to desired output using dictionary of symbols
    # a) Morse
        # - interpret dots and dashes into tones
    # b) NATO
# 4) output tones, text, or voice (phonetic)
# 5) ask for additional conversions
    # -exit if desired

import pandas as pd

# imports excel disctionary from file
df = pd.read_excel('Dictionary_data.xlsx', sheet_name = 'Morse')

morsedf = df[["Symbol","Morse"]]
sym = df["Symbol"]
morse_tone = df["Morse"]

### Define Dictionaries ###
morse_dict = {}
for i in range(len(df.index)):
    morse_dict[str(sym.iloc[i])] = str(morse_tone.iloc[i]).replace(" ","")
    
### Define Morse GPIO-LED
import RPi.GPIO as GPIO
import time

ledPin = 13    # define ledPin

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level 
    print ('using pin%d'%ledPin)

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
        print ('led turned on >>>')     # print information on terminal
        time.sleep(1)                   # Wait for 1 second
        GPIO.output(ledPin, GPIO.LOW)   # make ledPin output LOW level to turn off led
        print ('led turned off <<<')
        time.sleep(1)                   # Wait for 1 second

def Morse_LED_Out(x,y):
    setup()
    spd = int(y)  #LED scroll speed
    for i in x:
        if i == '.':
            GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
            time.sleep(1/spd)   #define 'on' dot
            GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level to turn off led
            time.sleep(.5/spd)   #gap morse characters
        elif i == '-':
            GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
            time.sleep(2/spd)     #define 'on' dash
            GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level to turn off led
            time.sleep(.5/spd)   #gap morse characters
        elif i == ' ':
            time.sleep(1/spd)
            continue

def destroy():
    GPIO.cleanup()                      # Release all GPIO

### Define what to pass to morse_out
    # convert input to morse_out input str
        # build morse_out input str

def txt2morse(x,spd):
    y = x.upper()
    morse_out = ""
    for i in range(len(y)):
        if y[i] == " ":
            morse_out = morse_out + "  "
        else:
            morse_out = morse_out + morse_dict[y[i]] + " "
    print(morse_out)
    return Morse_LED_Out(morse_out,spd)

#txt = input("type text to convert to Morse Lights here: ")
#txt2morse(txt)

#destroy()