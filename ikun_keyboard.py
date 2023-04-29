from pynput import keyboard#首先导入模块
import playsound

def press(key):
    try:
        #print(key.char)#调试输出

        if key.char=="j":
            playsound.playsound("J.mp3")
        elif key.char=="n":
            playsound.playsound("N.mp3")
        elif key.char=="t":
            playsound.playsound("T.mp3")
        elif key.char=="m":
            playsound.playsound("M.mp3")

    except AttributeError:
        if key==keyboard.Key.ctrl or key==keyboard.Key.ctrl_l or key==keyboard.Key.ctrl_r:
            #print("只因你太美")
            playsound.playsound("ctrl.mp3")

with keyboard.Listener(on_press=press) as listener:
    listener.join()