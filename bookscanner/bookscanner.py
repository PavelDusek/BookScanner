from rich import print
import time
import glob
import os
import subprocess
#import matplotlib.pyplot as plt
import cv2
import screeninfo

monitors = screeninfo.get_monitors()
print("[bold yellow]Monitors:[/bold yellow]", monitors)
monitor = monitors[0]
screen_width, screen_height = monitor.width, monitor.height

def showImg(filename, zoom = False):
    img = cv2.imread(filename)
    img_height, img_width, img_channels = img.shape
    if zoom:
        aspect_ratio = 1.5 * screen_height / img_height
        img = cv2.resize(img, (0,0), fx= aspect_ratio, fy= aspect_ratio)
        cv2.namedWindow(filename)
        cv2.moveWindow(filename, 10, 10)
    else:
        aspect_ratio = 0.75 * screen_height / img_height
        img = cv2.resize(img, (0,0), fx= aspect_ratio, fy= aspect_ratio)
        #img = cv2.resize(img, (100, 50) )
        cv2.namedWindow(filename)
        cv2.moveWindow(filename, round(screen_width/2), 0)
    cv2.imshow(filename, img)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if chr(key) == 'z':
        showImg(filename, zoom = True)

oldfilename = "capt0000.jpg"
newfilename = "page_0000.jpg"
pause = 0
command = ""

while (not command.strip() in ["q", "Q"]):
    print(f"[red]{command}[/red]")
    print("[bright_cyan]Getting a photo[/bright_cyan]")
    subprocess.call(["gphoto2", "--capture-image-and-download"])
    time.sleep(pause)
    images = glob.glob("*.jpg")
    pages  = glob.glob("page_*.jpg")

    if oldfilename in images:
        #photo has been succesfully taken
        if command.strip() in ["r", "R"]:
            #replace previous image
            length = len( pages )
        else:
            #make a new image
            length = len( pages ) + 1
        newfilename = f"page_{length:04d}.jpg"
    print(f"Moving [bold green]{oldfilename}[/bold green] to [bold magenta]{newfilename}[/bold magenta]")
    os.rename( oldfilename, newfilename)
    showImg(newfilename)
    #subprocess.Popen(["display", newfilename])
    print("[bold cyan]Commands:[/bold cyan] [red]Q = Quit[/red] | [green]R = Replace last[/green]")
    command = input("Command? ")

