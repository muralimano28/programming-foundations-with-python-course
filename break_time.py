import time
import webbrowser

count = 0;
while count < 3:
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=-qlJiGGvPUI")
    count = count + 1
