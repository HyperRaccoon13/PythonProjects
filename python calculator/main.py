import customtkinter
import math

OUTPUT_HIGHT = 100

xOfset = 5
yOfset = 5

app = customtkinter.CTk()
app.title("Math Thing")

#Output Lable
label = customtkinter.CTkLabel(app, text="Enter number", fg_color="transparent")
label.place(x=xOfset, y=OUTPUT_HIGHT/5)

numberOuput = customtkinter.CTkLabel(app, text="Output", fg_color="transparent")
numberOuput.place(x=xOfset, y=OUTPUT_HIGHT/2.5)

#Button Vars 
buttonSizeX = 100
buttonSizeY = 100

buttonPosX = 0
buttonPosY = 0

buttonInRow = 3
buttonInColumn = 3

buttonDisc = {}

numberIndex = 0
outputList = []

#operators

operatorsDisc = {}

operatorsIndex = 0
operatorsList = ["+", "-", "*", "/", "0", "="]

def CleanOutput(output):
   result = ""
   for item in output:
      if item != "=":
        result += str(item)

   return result

def FinalCalculate(expression):
    expression = CleanOutput(outputList)
    try:
        result = eval(expression)
        numberOuput.configure(text=result)

    except Exception as error:
        numberOuput.configure(text=error)


for x in range(buttonInColumn):
    for y in range(buttonInRow):

         numberIndex = numberIndex + 1

         def NumberCallBack(number=numberIndex):
            outputList.append(number)
            label.configure(text=outputList)

         buttonDisc[numberIndex] = customtkinter.CTkButton(app, text=numberIndex, command=NumberCallBack, width=buttonSizeX, height=buttonSizeY)
         buttonDisc[numberIndex].place(x=xOfset + buttonPosX, y=OUTPUT_HIGHT + yOfset + buttonPosY)
         buttonPosX = buttonPosX + buttonSizeX + xOfset 

         #Start Of Operators Buttons
         if numberIndex >= 9:
           buttonPosY = 0

           #Operator Button Loop
           for operators in operatorsList:
               operatorsIndex = operatorsIndex + 1 

               #Operators Call Back Function
               def OperatorsCallBack(operators=operatorsList[operatorsIndex-1]):
                if outputList and all(item != outputList[-1] for item in operatorsList if item != "0"):
                    outputList.append(operators)

                    if outputList[-1] == "=":
                       FinalCalculate(outputList)

                    label.configure(text=outputList)

               #Zero Button
               if operatorsIndex == 5:
                  buttonPosX = 0 + buttonSizeX + xOfset
                  buttonPosY = buttonPosY - buttonSizeY - yOfset

               #Equals Buttons
               if operatorsIndex == 6:
                  buttonPosX = 0 + buttonSizeX + xOfset + buttonPosX
                  buttonPosY = buttonPosY - buttonSizeY - yOfset
                  
               #Operators Button
               operatorsDisc[operatorsIndex] = customtkinter.CTkButton(app, text=operators, command=OperatorsCallBack, width=buttonSizeX, height=buttonSizeY)
               operatorsDisc[operatorsIndex].place(x=xOfset + buttonPosX, y=OUTPUT_HIGHT + yOfset + buttonPosY)
               buttonPosY = buttonPosY + buttonSizeY + yOfset

    buttonPosY = buttonPosY + buttonSizeY + yOfset
    buttonPosX = 0

#Finds the size for the GUI
SCREEN_WIDTH = (xOfset * 3) + (buttonSizeX + xOfset + buttonSizeX) * 2
SCREEN_HIGHT = OUTPUT_HIGHT + yOfset + (yOfset + buttonSizeY) * 4

app.geometry(f"{SCREEN_WIDTH}x{SCREEN_HIGHT}")
app.minsize(SCREEN_WIDTH, SCREEN_HIGHT)
app.maxsize(SCREEN_WIDTH, SCREEN_HIGHT)
app.mainloop()