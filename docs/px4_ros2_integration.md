# PX4–ROS2 Integration

This document explains how PX4 and ROS2 interact within the communication pipeline.


## Overview

PX4 handles flight control while ROS2 manages high-level logic, data handling, and communication with the server.

MAVLink serves as the protocol connecting the two systems.


## Integration Methods

### Option A: MAVLink Router
- Routes PX4 telemetry to multiple endpoints
- Simple and widely used

### Option B: MAVSDK
- High-level SDK for commanding PX4
- Provides API for takeoff/mission commands

### Option C: micrortps / px4_ros_com
- ROS2 topic bridging
- Publishes PX4 data directly as ROS2 topics


## Common ROS2 Nodes

- `/gps` – GPS telemetry  
- `/attitude` – Orientation data  
- `/command_server` – Processes commands from server  
- `/telemetry_publisher` – Sends data to server  


## Command Flow Example (Takeoff)

1. Server sends command `"takeoff"`  
2. ROS2 node receives message  
3. Node converts to MAVLink command  
4. MAVLink Router / SDK sends command to PX4  
5. PX4 acknowledges and performs takeoff  


## Safety Considerations

- Heartbeat monitoring required  
- Emergency stop command must always be available  
- Command timeouts prevent runaway flight  
