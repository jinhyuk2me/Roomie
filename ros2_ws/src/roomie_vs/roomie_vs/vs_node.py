#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# Service imports with correct subdirectory paths
from roomie_msgs.srv.robot_control import SetVSMode, Location
from roomie_msgs.srv.door_elevator import ElevatorWidth, ElevatorStatus, DoorStatus
from roomie_msgs.srv.sensor import ButtonStatus, SpaceAvailability

# Message imports with correct subdirectory paths
from roomie_msgs.msg.user_interface import TrackingEvent, Registered


class VSNode(Node):
    def __init__(self):
        super().__init__('vs_node')
        
        # Services
        self.create_service(SetVSMode, '/vs/command/set_vs_mode', self.set_mode)
        self.create_service(ElevatorWidth, '/vs/command/elevator_width', self.elevator_width)
        self.create_service(ButtonStatus, '/vs/command/button_status', self.button_status)
        self.create_service(ElevatorStatus, '/vs/command/elevator_status', self.elevator_status)
        self.create_service(DoorStatus, '/vs/command/door_status', self.door_status)
        self.create_service(SpaceAvailability, '/vs/command/space_availability', self.space_availability)
        self.create_service(Location, '/vs/command/location', self.location)
        
        # Publishers
        self.tracking_pub = self.create_publisher(TrackingEvent, '/vs/tracking_event', 10)
        self.registered_pub = self.create_publisher(Registered, '/vs/registered', 10)
        
        self.get_logger().info('VS Node started')
    
    def set_mode(self, request, response):
        response.robot_id = request.robot_id
        response.success = True
        return response
    
    def elevator_width(self, request, response):
        response.robot_id = request.robot_id
        response.left_boundary = 0.0
        response.right_boundary = 1.5
        return response
    
    def button_status(self, request, response):
        response.robot_id = request.robot_id
        n = len(request.button_ids)
        response.xs = [0.0] * n
        response.ys = [0.0] * n
        response.depths = [1.0] * n
        response.is_pressed = [False] * n
        response.timestamp = [self.get_clock().now().to_msg()] * n
        return response
    
    def elevator_status(self, request, response):
        response.robot_id = request.robot_id
        response.direction = 0
        response.position = 1
        return response
    
    def door_status(self, request, response):
        response.robot_id = request.robot_id
        response.door_opened = False
        return response
    
    def space_availability(self, request, response):
        response.robot_id = request.robot_id
        response.space_availability = True
        return response
    
    def location(self, request, response):
        response.robot_id = request.robot_id
        response.location_id = 0
        return response


def main():
    rclpy.init()
    node = VSNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main() 