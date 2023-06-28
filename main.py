import os

def takePic(id):
    print("taking photo....")
    os.system("libcamera-jpeg --rotation 180 -o "+ id + '.jpg')
    print("foto taken succesfuly")
    

while True:
    id = 1
    action = input("f = photo, e = exit: \n")
    if action == 'f':
        takePic(id)
    if action == 'e':
        break
    id += 1