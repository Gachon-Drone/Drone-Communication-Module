# Drone Communication Module  
P-Project / Gachon-Drone

This repository contains the communication module and system architecture used in the P-Project drone system.  
The goal is to define and document the entire communication pipeline between the drone, LTE router, server, web interface, and ROS2/PX4 components.

---

## Overview

The Drone Communication Module focuses on the end-to-end network flow required to remotely monitor and control a drone.  
This includes:

- LTE router configuration and port forwarding  
- Drone Companion Computer ↔ Server ↔ Web communication pipeline  
- PX4 ↔ ROS2 message flow  
- System architecture diagrams  
- Documentation needed for team integration and final presentation  

---

## Repository Structure

Drone-Communication-Module/
├── docs/
│ ├── 01_system_overview.md
│ ├── 02_communication_architecture.md
│ ├── 03_network_flow_diagram.png
│ ├── 04_lte_router_config.md
│ └── 05_px4_ros2_integration.md
├── src/
│ └── (communication code if applicable)
└── README.md

---

##  System Components

### 1. Drone (PX4 + Companion Computer)
- MAVLink communication  
- Telemetry forwarding  
- ROS2 bridge  
- Mission/command execution  

### 2. LTE Router
- Provides external access  
- NAT & port forwarding  
- Ensures stable communication when the drone is remote  

### 3. Server
- Receives telemetry  
- Sends control commands  
- Hosts monitoring dashboard / API  

### 4. Web or Client Interface
- Real-time monitoring  
- Command input (Arm, Takeoff, Land, Navigation)  

---

##  Key Features in This Repository

- Full communication architecture documentation  
- Network flow diagrams used in the team presentation  
- LTE routing + port setup explanation  
- PX4–ROS2 integration overview  
- Reference code or configuration scripts (if added later)

---

##  How to Use

1. Clone this repository:
git clone https://github.com/Gachon-Drone/Drone-Communication-Module.git

2. Check the documentation in `docs/` for full communication diagrams and explanations.

3. (Optional) Add your communication-related scripts under `src/`.

---

##  Author  
**Park Subin**  
Gachon University — P-Project Drone Team  
