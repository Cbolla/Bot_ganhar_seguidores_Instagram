import sys
from PySide2 import QtCore, QtGui, QtWidgets
from untitled import Ui_MainWindow
from untitled import*
import pyautogui
import time
import keyboard
import random


lista=[]
def main(ui):
    def a():
        lista.append(ui.lineEdit.text())
    ui.botaoa.clicked.connect(a)
    
    def tudo():
        while keyboard.is_pressed("c")==False:
            sort=random.choice(lista)
            def parar():
                for c in range(10):
                    if pyautogui.locateOnScreen("following.PNG"):
                        pyautogui.click("following.PNG")
                        time.sleep(1)
                        pyautogui.click("unfollow.PNG")
                    else:
                        if pyautogui.locateOnScreen("parar.PNG"):
                            pyautogui.scroll(-200)
            def continuar():
                for ce in range(15):
                    if pyautogui.locateOnScreen("follow.PNG"):
                        pyautogui.click("follow.PNG")
                        time.sleep(1)
                    else:
                        pyautogui.locateOnScreen("following.PNG")
                        pyautogui.scroll(-200)
            def fun1():
                time.sleep(1)
                pyautogui.click("x.PNG")
                time.sleep(1)
                pyautogui.click(1038,93)
                time.sleep(1)
                pyautogui.click("profile.PNG")
                time.sleep(1)
                pyautogui.click("cfollowing.PNG")
                time.sleep(1)
                pyautogui.click(728,330)
            def fun2():
                time.sleep(1)
                pyautogui.click("x.PNG")
                time.sleep(1)
                pyautogui.click("search.PNG")
                time.sleep(1)
                pyautogui.locateOnScreen("profile.PNG")
                pyautogui.write(sort)
                time.sleep(1)
                pyautogui.click(648,149)
                time.sleep(1)
                pyautogui.click("followers.PNG")
                time.sleep(1)
                pyautogui.click(728,330) 
            continuar()
            fun1()
            parar()
            fun2()
    
    ui.botaogo.clicked.connect(tudo)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow= QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
