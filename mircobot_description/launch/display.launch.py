from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
import xacro
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    share_dir = get_package_share_directory('mircobot_description')

    xacro_file = os.path.join(share_dir, 'urdf', 'mircobot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    robot_urdf = robot_description_config.toxml()

    rviz_config_file = os.path.join(share_dir, 'config', 'display.rviz')

    gui_arg = DeclareLaunchArgument(
        name='gui',
        default_value='True'  # True if you need joint movement verification 
    )

    sim_time_arg = DeclareLaunchArgument(
        name='use_sim_time',
        default_value='True',
        description='Use simulation time if true'
    )


    show_gui = LaunchConfiguration('gui')
    # sim = LaunchConfiguration('sim')
    use_sim_time = LaunchConfiguration('use_sim_time')

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[
            {'robot_description': robot_urdf,'use_sim_time' : use_sim_time}
        ]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[{'use_sim_time' : use_sim_time}]
        #output='screen'
        
    )

    joint_state_publisher_gui_node = Node(
        condition=IfCondition(show_gui),
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen'
    )

    return LaunchDescription([
        gui_arg,
        sim_time_arg,
        robot_state_publisher_node,
        #joint_state_publisher_node,
        #joint_state_publisher_gui_node,
        rviz_node
    ])
