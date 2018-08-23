# !/usr/bin/python3
import winsound
import _thread

isRun = True


def print_time(threadName, delay):
    print("播放铃声~")
    global isRun
    winsound.PlaySound("ring.wav", winsound.SND_FILENAME)

    isRun = False


def ring():
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2,))
    except:
        print("Error: 无法启动线程")

    while isRun:
        pass


if __name__ == '__main__':
    ring()
