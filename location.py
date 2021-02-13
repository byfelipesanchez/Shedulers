import os
import time

path ="C:/Users/2018f/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39"
path = os.path.realpath(path)

question = input("Would you like to open Python (location)? y/n ")

if question == "y":
    os.startfile(path)
else:
    if question == "n":
        print("Then why did you open this program???")
        time.sleep(0.5)
        quit()
    else:
        quit



