# ROS2_ELP-801
Sample Codes and Resources for ELP-801

## Setting up ROS2 Foxy and Simulation Software on Ubuntu 20.04

**Open the terminal with Ctrl+Alt+T and enter below three commands one at a time to install ROS2 Foxy.**

```console
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros2_foxy.sh
sudo chmod 755 ./install_ros2_foxy.sh
bash ./install_ros2_foxy.sh
```

**After the execution of above commands run the commands below to install:**

**Gazebo11**


```console
sudo apt-get install ros-foxy-gazebo-*
```

**Cartographer**


```console
sudo apt install ros-foxy-cartographer
sudo apt install ros-foxy-cartographer-ros
```
**Navigation2**

```console
sudo apt install ros-foxy-navigation2
sudo apt install ros-foxy-nav2-bringup
```

**Install TurtleBot3 Packages**


```console
source ~/.bashrc
sudo apt install ros-foxy-dynamixel-sdk
sudo apt install ros-foxy-turtlebot3-msgs
sudo apt install ros-foxy-turtlebot3
```

**Now Set the ROS environment for PC**

```console
echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
source ~/.bashrc
```

# Testing the Gazebo Simulation

**Install Simulation Package**

```console
cd ~/colcon_ws/src/
git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/colcon_ws && colcon build --symlink-install
```
**Now close all the terminals and open a new terminal and proceed below**

**Launch Simulation World**
```console
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

You must be able to see the turtlebot in an empty world like the picture below
![image](https://github.com/Ruudddiiii/ROS2_ELP-801/assets/107204888/a247dc00-939f-498f-9cb5-4c6f701049f0)

**In order to teleoperate the TurtleBot3 with the keyboard, launch the teleoperation node with below command in a new terminal window.**

```console
ros2 run turtlebot3_teleop teleop_keyboard
```
Now you can move the Turtlebot using W,A,S,X,D keys on your keyboard.

## Assignment


*Making a circle
[circle](https://github.com/Ruudddiiii/ROS2_ELP-801/assets/107204888/d480d9b2-506e-4718-b6bb-7ffb339655d4)


*Making a infinity sign
https://github.com/Ruudddiiii/ROS2_ELP-801/assets/107204888/37f3c4f6-edb5-4b02-813e-b0884423b8af



## Updates

1. I've shared the move_fwd.py and ELP801_1.pptx files. Kindly review them; I've covered fundamental ROS2 concepts and provided a simple code snippet for moving the TurtleBot forward. I'll delve into the details during our class discussion, but it would be beneficial if you could familiarize yourself with the material beforehand.

