from tkinter import *
import time
import _thread

def WindowColorChangeFunction(ColorChangeObject, rgbColors = False, CycleTimeInSec = 10, bytesPerColor = 2):

    maxColorValue = ( 16**bytesPerColor ) - 1
    waitTime = ( 1 / (maxColorValue*6) ) * CycleTimeInSec
    if not rgbColors:
        rgbColors = [maxColorValue, 0, 0] #Starting at full red screen
    
    while True:
        changingRate = [0, 0] #[changing color, step]
        step = 1
        fullColorAmount = 0

        for colorIndex in range(len(rgbColors)):
            if rgbColors[colorIndex] == maxColorValue:
                fullColorAmount += 1
                if fullColorAmount == 2:
                    if rgbColors[colorIndex-1] == maxColorValue:
                        changingRate[0] = colorIndex-1
                        changingRate[1] = -step
                    else:
                        changingRate[0] = colorIndex
                        changingRate[1] = -step
                    break
        else:
            for colorIndex in range(len(rgbColors)):
                if rgbColors[colorIndex] == maxColorValue:
                    try:
                        test = rgbColors[colorIndex+1]
                        changingRate[0] = colorIndex+1
                        changingRate[1] = step
                    except:
                        changingRate[0] = 0
                        changingRate[1] = step
                    break

        while True:
            time.sleep(waitTime)
            changingColor = changingRate[0]

            formattedColor = "#"
            for color in rgbColors:
                hexColor = hex(color)[2:]
                if len(hexColor) < bytesPerColor:
                    hexColor = "0" * (bytesPerColor - len(hexColor)) + hexColor
                formattedColor += hexColor

            ColorChangeObject.config(bg=formattedColor)

            change = changingRate[1]
            rgbColors[changingColor] += change
            if rgbColors[changingColor] == 0 or rgbColors[changingColor] == maxColorValue:
                break


def WindowColorChangeApp(rgbColors = False, CycleTimeInSec = 10, bytesPerColor = 2):

    frame = Tk()
    frame.geometry("2000x1100")

    coloredBackground = Label(frame,bg="#000000")
    coloredBackground.place(x=0,y=0,width=1920,height=1080)

    _thread.start_new_thread(WindowColorChangeFunction,(coloredBackground, rgbColors, CycleTimeInSec, bytesPerColor))

    frame.mainloop()

if __name__ == "__main__":
    WindowColorChangeApp()
