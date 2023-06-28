# RaspiCam3RobotDolly

This project consists of a robotic device that is controlled via ssh and allows a user to nicely move a raspberry pi 3 camera, recover and take pictures on command. 

Currently, the main.py file runs forever while receiving input from the user. If the user inputs 'f', the program takes and saves the picture, and if the user inputs 'e', the program exits.

## Up and Running

Simply clone this repository in your raspberry pi with the raspicam3 module connected. and run the following script:

`python main.py`

note: currently using python 3
