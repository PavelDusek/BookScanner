import time
import glob
import os
import subprocess


oldfilename = "capt0000.jpg"
command = ""
while command != "q":
    print(command)
    subprocess.call(["gphoto2", "--capture-image-and-download"])
    time.sleep(3)
    filenames = glob.glob("*.jpg")
    if oldfilename in filenames:
        length = len( filenames ) + 1
        newfilename = f"page_{length:04d}.jpg"
        print("Moving", oldfilename, "to", newfilename)
        os.rename( oldfilename, newfilename)
        #subprocess.Popen(["display", newfilename])
    command = input("Command?")

