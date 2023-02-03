import keyboard
import pyautogui
import time


if __name__=="__main__":
    inp = "j;6qo4mp6"
    # inp = "vu,41u/3p "
    while True:  
        orgx,orgy = pyautogui.position()
        # 1670 ,1055
        # x,y =pyautogui.position()
        # r, g, b = pyautogui.pixel(x, y)
        # print(r,g,b)
        # print("The cursor is currently at: " + str(x) + ", " + str(y))
        # time.sleep(1)
        try: 
            if keyboard.is_pressed('f9'): 
                print(list(pyautogui.pixel(1670,1055)))
                for i in list(pyautogui.pixel(1670,1055)):
                    if i<200:
                # if sum(list(pyautogui.pixel(1670,1055)))<200:
                        pyautogui.click((1670,1055))
                        print("its now English")
                        break
                print('test')
                pyautogui.typewrite("@"+inp)  
                pyautogui.press(["enter","space"])
                pyautogui.moveTo(orgx,orgy)

            if keyboard.is_pressed('ctrl+q'):
                print('ctrlq')
                break
        except:
            pass