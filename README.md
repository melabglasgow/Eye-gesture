# Eye-gesture
Source code and file of eye gesture project in meLAB, University of Glasgow

Author: Xiangpeng Liang


The GFS and WirelessDAQ with Tetris gama can work indepently. The GFS maps human eye movement onto a eye model (designed by Asfand Tanwear, the source file is attached) for the experimental sitation that the human test of contact lens have not been approval. More details of TMR sensor and magnetic contact lens will be published soon.



## System requirement

### GFS
#### Hardware
* Eye model ()
* Arduino Nano
* 9g Servo motor x 2

#### Software
This setup has been tested under Win10 64bits
* LabVIEW 2018 SP1
  * NI VISA 19.5
  * VIPM-> LabVIEW Interface for Arduino 2.2.0.79
* Serial driver
* Python 3.6 (for gaze tracking)
  * opencv_python
  * dlib

#### Make it works


### WirelessDAQ with Tetris game

#### Hardware
* Intergrated circuit for TMR sensor
* [DFRobot Bluno Beetle Wearable Development Board DFR0339](https://uk.rs-online.com/web/p/processor-microcontroller-development-kits/1244685/)
* [Silicon Labs USB Bluetooth Dongle Class 4](https://uk.rs-online.com/web/p/bluetooth-adapters/8077742/)
* 


#### Software
* LabVIEW 2018 SP1
  * NI VISA 19.5
* Python 3.6 (for Tetris game)
  * pygame
