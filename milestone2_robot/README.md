# IEEE ROS Track 2025 🚀

Welcome to the ROS simulation project, part of the IEEE RAS Training Track 2025.  
This project demonstrates building and simulating a robot using ROS Noetic,Gazebo and Rviz.

# Step 1 – Create the ROS Package
Before running the project, create a new ROS package inside your existing `catkin_ws` workspace.
```bash
# Navigate to the src directory of your workspace
cd ~/catkin_ws/src
# Create a new package (you can rename "my_robot_pkg" )
catkin_create_pkg my_robot_pkg rospy std_msgs geometry_msgs gazebo_ros

# Go back to the root of the workspace
cd ~/catkin_ws

# Build the workspace
catkin_make
```
# Step 2 – Copy Project Files into the Package
Now, copy the contents of this repository 'milestone2_robot' into your newly created package directory 'my_robot_pkg'
```bash
# Replace /path/to/IEEE_ROS_Track_25 with the actual path to the downloaded folder
cp -r ~/IEEE_ROS_Track_25/milestone2_robot ~/catkin_ws/src/my_robot_pkg/
```
```bash
Rebuild the workspace again to register the new files:
cd ~/catkin_ws
catkin_make
```
# Step 3 – Launch the Robot in Gazebo
To run the robot simulation in Gazebo, execute the following:
```bash
roslaunch milestone2_robot gazebo.launch 
```

# Step 4 – Launch Rviz for Visualization
To visualize the robot and its environment using Rviz:
```bash
roslaunch milestone2_robot display.launch 
```
# Notes
⚠️ If Gazebo doesn't open properly or the robot doesn't appear, you can forcefully kill any Gazebo-related processes using:
``` bash
sudo killall -9 gazebo gzserver gzclient
roslaunch milestone2_robot gazebo.launch
```
