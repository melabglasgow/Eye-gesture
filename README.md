# Eye-gesture
Source code and file of eye gesture project in meLAB, University of Glasgow

Author: Xiangpeng Liang

The GFS and WirelessDAQ with Tetris gama can work indepently. The GFS maps human eye movement onto a eye model (designed by Asfand Tanwear, the source file is attached) for the experimental sitation that the human test of contact lens have not been approval. More details of TMR sensor and magnetic contact lens will be published soon.


## System requirement

### GFS
#### Hardware
* Eye model (Eye-gesture/GazeFollowingSystem/3DprintingEyeModel/)
* Arduino Nano
* 9g Servo motor x 2
* Webcam

#### Software
This setup has been tested under Win10 64bits
* LabVIEW 2018 SP1
  * NI VISA 19.5
  * VIPM-> LabVIEW Interface for Arduino 2.2.0.79
* Serial port driver
* Arduino IDE
* Python 3.6 (for gaze tracking)
  * opencv_python
  * dlib

#### Make it works
* Install the required software and environment above.
* Connect servo motors to Arduino nano, connect Arduino nano to PC USB.
* Load the code of LabVIEW Interface for Arduino to Arduino nano.[see method](https://www.youtube.com/watch?v=RhdnmFJcFA0)
* Connect a webcam to your PC.
* Power the servo motors and Arduino. Open the main.vi and run
  * Caution: change the port number, location of python code (test3_2.py) in LabVIEW code (main.vi) accordingly. 
  * Caution: the direction and angle range of servo motors should be cablibrated using servotest.vi before the first use.
* Sit in front of the webcam approx. 40cm away. Keep your head still and move your eyeball.



### WirelessDAQ with Tetris game
#### Hardware
* Intergrated circuit for TMR sensor
* [DFRobot Bluno Beetle Wearable Development Board DFR0339](https://uk.rs-online.com/web/p/processor-microcontroller-development-kits/1244685/)
* [Silicon Labs USB Bluetooth Dongle Class 4](https://uk.rs-online.com/web/p/bluetooth-adapters/8077742/)
#### Software
* LabVIEW 2018 SP1
  * NI VISA 19.5
* Python 3.6 (for Tetris game)
  * pygame
* Serial port driver
* Arduino IDE

#### Make it works




## Acknowledgements
Special thanks to Antoine Lamé and Pavel Benáček: 

The code is the GFS package was based in part of the source code of the [antoinelame/GazeTracking](https://github.com/antoinelame/GazeTracking)

The code is the Tetris game was based in part of the source code of the [benycze/python-tetris](https://github.com/benycze/python-tetris)
