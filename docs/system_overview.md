# 01. System Overview

This document provides an overview of the communication and control pipeline used in the P-Project drone system.  
The system enables a drone to be monitored and controlled remotely through an LTE network, public server, and web-based interface.

---

## 1.1 System Components

### 1) Drone (PX4 + Companion Computer)
- PX4 Autopilot handles low-level flight control.
- Companion Computer (Jetson/Raspberry Pi) processes high-level commands.
- MAVLink is used for communication between PX4 and the Companion Computer.
- ROS2 nodes run on the Companion Computer for data handling and mission execution.

### 2) LTE Router
- Provides mobile network connectivity.
- Forwards external traffic to the drone.
- Enables remote operation without requiring a local network.

### 3) Public Server
- Acts as a communication relay between the drone and web client.
- Handles telemetry forwarding, command dispatching, and connection management.

### 4) Web/Client Interface
- User interface to monitor drone status.
- Sends control commands such as Arm, Takeoff, Move, Land.
- Displays live mission data and system states.

---

## 1.2 High-Level Data Flow

1. Drone publishes status → Companion Computer → LTE Router  
2. LTE Router → Public Server through forwarded ports  
3. Server → Web UI for monitoring  
4. User commands from Web UI → Server → Drone (via Companion Computer → PX4)

---

## 1.3 Purpose of the System

The primary goals of this system are:

- Enable safe and reliable **remote operation** of a drone.
- Support **long-distance communication** using LTE.
- Provide a **structured and modular network architecture** for team development.
- Allow real-time **monitoring of telemetry data** such as GPS, attitude, and mission status.

---

## 1.4 System Architecture Diagram

See: `network_flow_diagram.png`

The diagram illustrates each major component and how data moves between them.