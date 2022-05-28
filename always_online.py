import mouse
import time

def run_mouse():
    while(True):
        time.sleep(10)
        print("moved")
        mouse.move(1,2)
        mouse.right_click()
        time.sleep(10)
        mouse.drag(1,2,1010,1012)

if __name__ == '__main__':
    run_mouse()