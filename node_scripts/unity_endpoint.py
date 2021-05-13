#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService, UnityService
from sensor_msgs.msg import JointState

def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'TCPServer')
    buffer_size = rospy.get_param("/TCP_BUFFER_SIZE", 1024)
    connections = rospy.get_param("/TCP_CONNECTIONS", 10)
    tcp_server = TcpServer(ros_node_name, buffer_size, connections)
    rospy.init_node(ros_node_name, anonymous=True)

    tcp_server.start({
        'joint_states': RosPublisher('joint_states', JointState, queue_size=10),
        'joint_command': RosSubscriber('joint_command', JointState, tcp_server)
    })
    rospy.spin()


if __name__ == "__main__":
    main()
