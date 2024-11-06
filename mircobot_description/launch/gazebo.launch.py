from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
import os
import xacro
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    
    display_launch = IncludeLaunchDescription(
                    PythonLaunchDescriptionSource([os.path.join(
                        get_package_share_directory("mircobot_description"),'launch','display.launch.py'
                    )]), launch_arguments={'use_sim_time': 'true','use_gui':'false'}.items()
        )
    
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'
                    )]), launch_arguments={}.items()
             )

    urdf_spawn_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'mircobot',
            '-topic', 'robot_description'
        ],
        output='screen'
    )

    return LaunchDescription([
        display_launch,
        gazebo,
        urdf_spawn_node,
    ])
