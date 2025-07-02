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
