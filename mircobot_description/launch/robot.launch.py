import os
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    display_robot_rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
        get_package_share_directory('mircobot_description'),
        'launch/display.launch.py'
    )
        ))   # it contain Robot_state_pub , Joint_state_pub , and rviz
    
    # need to create node for gazebo launch

 




    return LaunchDescription([
        display_robot_rviz



    ])