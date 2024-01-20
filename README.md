# ROS2_ELP-801
Sample Codes and Resources for ELP-801

# Setting up ROS2 Fosy and Simulation Software Using Ubuntu 20.04

**Open the terminal with Ctrl+Alt+T and enter below three commands one at a time to install ROS2.**

```console
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros2_foxy.sh
sudo chmod 755 ./install_ros2_foxy.sh
bash ./install_ros2_foxy.sh
```

**After the execution of above commands run the below commands to install:**

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

## Set the ROS environment for PC

```console
echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
source ~/.bashrc
```





