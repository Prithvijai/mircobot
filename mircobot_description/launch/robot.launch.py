import os
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch import LaunchDescription
from launch.substitutions import TextSubstitution

def generate_launch_description():
    display_robot_rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
        get_package_share_directory('mircobot_description'),
        'launch/display.launch.py'
    )
        ))   # it contain Robot_state_pub , Joint_state_pub , and rviz
    
    world_var = DeclareLaunchArgument(
        name='world',
        default_value=TextSubstitution(text="empty.world")
    )

    # need to create node for gazebo launch
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch/gazebo.launch.py'
            )),
            launch_arguments={
                'world': LaunchConfiguration('world'),
                'pause':'true'
            }.items()
        )
    
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity','mircobot',
            '-topic','robot_description'
        ],
        output='screen'
    )
    # The robot is spawned in Gazebo now add control system to the robot and camera and lidar.



    return LaunchDescription([
        display_robot_rviz,
        world_var,
        gazebo_launch,
        spawn_robot




    ])