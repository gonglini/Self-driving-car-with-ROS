# autonomous-car-with-ROS

This project was created by ME.


<img src=https://user-images.githubusercontent.com/65767592/221577472-4a88ca98-18b0-489c-8adb-9dfcaa3cbef1.jpg width="600" height="400"/>


## Overview
This project is the source code for self-Driving car. This code implements motion control of a 1:10 sclae car, including move by keyboard or autonomatically. Supporting libraries provide additional capabilities, such as object detection by camera to provide accident. The software is implemented on a Jetson Nano running Ubuntu 18.04 with ROS Melodic installed.

The software is composed of C++ and Python nodes in a ROS framework.

#### Hardware:
The frame utilized is the 1:10 rc car. 

Component List:
* Computer: JetsonNano & Melodic ROS
* Servo control board: PCA9685, controlled via i2c (It's easy to break down, so I recommend you to buy extra products.)
* Servos: CLS6336HV x1
* Esc: Hobbywing WF brushed esc 60A
* Battery: 2s 5200 mAh Lipo, direct connection to servo board for servo power
* Camera: 1080p webcam
* other: XL4015 dc-dc stepdown converter x2



#### Software:

Software version:
* Jetpack 4.5.1
* OpenCV 4.5.1
* CUDA 10.0
* CUDNN 8.0
* Tensorflow 2.5.0
* Darknet yoloV4
* ROS Melodic

This repo is structured as a catkin workspace in a ROS Melodic envivornment on Ubuntu 16.04. The software may not work or compile outside this environment. Jetson nano images preloaded with Ubuntu 18.04 and a ROS Melodic installation can be found via ubiquity robotics. [See ubiquity robotics webpage](https://downloads.ubiquityrobotics.com/) for download, setup, and wifi setup instructions. It is suggested to also install ROS Melodic on a Ubuntu 18.04 linux installation/dual boot/virtual machine on a PC for development and for running control nodes. Instructions to install ROS melodicc can be found [here](http://wiki.ros.org/melodic/Installation/Ubuntu).

I used compact command to install ROS melodic made by zeta(https://github.com/zeta0707/installROS.git)

**NOTE**  A SWAP partition of about 8 GB on the jetson sd card is necessary to increase the virtual memory available beyond the Jetsons onboard RAM. In my experience the catkin compilation process uses all the onboard RAM and stalls indefinitely and does not complete without adding a SWAP partition. Example instructions for adding a SWAP partition. 



```
catkin_ws/
│
├── src/
│   ├── detect
│       └── src
│           └──launch      
│
```


If any git permission errors are encountered, try the following suggestions via [this stackoverflow post](https://stackoverflow.com/questions/8197089/fatal-error-when-updating-submodule-using-git).


Since the same repo is checked out on both a Json and a laptop/PC, you will need to install an i2c library on the laptop/pc for the software to compile correctly. The `i2cpwm_board` node is not run on the laptop/pc, but compilation will look for dependencies for this node. Install the necessary library via:
`sudo apt-get install libi2c-dev`

You should install additional packages.

*  `sudo pip3 install adafruit-circuitpython-pca9685`
*  `sudo pip3 install adafruit-circuitpython-servokit`
*   `sudo pip3 install board`
*   `sudo pip3 install keyboard`

#### Note on detect line


#### Running:
Open at least three terminal windows, with not ssh. 
* `rosrun detect detector_pub.py`: Run on the Json to detect object while driving. If car detect specific object, it will publish topic.
* `rosrun detect detector_sub.py` Run on the Json to predict angle for driving. If car subscribe topic, it will realize accident and stop driving.

## Additional Project Components
#### URDF Model
The project contains a URDF model of the spot micro platform, along with a custom set of stl files  for visualization. The URDF file was pulled from Florian Wilk's repo, noted at the end of this README, and modified to change the coordinate system orientation, and the dimensions to match dimensions of my spot micro robot. Currently this urdf file is **only** used for RVIZ visualization of the spot micro model. This URDF model should not be treated as perfectly accurate representation of the robot's geometry, nor should the STL files in this repo be used for 3d printing. Use the noted Thingverse files instead. 

The URDF model is defined as a `xacro` file, which is a way to define urdf file using macros to automate certain generative actions. The xacro file is located in the `spot_micro_rviz/urdf` directory. A urdf file can be generated from the `.xacro` file for inspection or use, if needed, via running `xacro` after sourcing a ROS development environment. 

#### TF2 Publishing and Odometry
Robot state transforms are published via TF2. Some primary frames of interest are `base_footprint` and `base_link`, and `lidar_link`. `base_footprint` is a coordinate frame at zero height at the base of the robot frame. `base_link` is the coordinate frame fixed to the body center of the robot, and moves and rotates with body motion. `lidar_link` is a coordinate frame aligned with an installed lidar.

An odometry frame, `odom`, is optionally available and can be enabled via a configurable parameter in the `spot_micro_motion_cmd.yaml` file. If enabled, `odom` is parent to the `base_footprint` frame.  **Note that odometry is grossly inaccurate and not calibrated whatsoever**. It is a pure integration of robot rate commands and thus drifts unbounded with errors over time. It is provided for any useful purpose it may serve.

#### SLAM
If a lidar, such as a RPLidar A1, is mounted to the robot frame, 2d mapping is possible through SLAM with additional ROS nodes, such as hector_slam. More information about running SLAM through this project is described in the [SLAM information](docs/slam_information.md) document.

## Future Work
The current software supports basic state machine operation of the spot micro robot, orientation control at rest, and rate command in forward, sideways, and yaw directions, completely through external command messages.

My desired future goals for this project, in order of preference, are to:
1. ~~Incorporate a lidar (particularly the Slamtec RPLIDAR A1) to achieve simple 2D mapping of a room via SLAM. This may require the addition of an IMU for robot orientation sensing (for example, an Adafruit 9-DOF IMU BNO055).~~
2. Develop an autonomous motion planning module to guide the robot to execute a simple task around a sensed 2D environment. For example, navigate the perimeter of a room, and dynamically avoid introduced obstacles.
3. Incorporate a camera or webcam and create a software module to conduct basic image classification. For example, perceive a closed fist or open palm, and have the robot react in specific ways to each.
4. Implement a more advanced robot controller that can reject external disturbances. 


