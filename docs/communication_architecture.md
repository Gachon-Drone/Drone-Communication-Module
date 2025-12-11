# Communication Architecture

This document details the full communication architecture used in the P-Project drone system, covering protocol layers, data routes, and system functions.


## End-to-End Communication Overview

The system consists of four main communication stages:

1. **PX4 ↔ Companion Computer (MAVLink)**
2. **Companion Computer ↔ LTE Router**
3. **LTE Router ↔ Public Server**
4. **Public Server ↔ Web Client**

Each stage performs a specific role in ensuring low-latency, reliable drone communication.


## Communication Pipeline

### Stage 1: PX4 → Companion Computer
- Protocol: **MAVLink**
- Purpose:
  - Receive actuator commands  
  - Stream telemetry (battery, GPS, attitude, RC status)
- Tools:
  - MAVLink Router / MAVSDK / micrortps bridge  
  (Depending on implementation)


### Stage 2: Companion Computer → LTE Router
- Communication via Ethernet/Wi-Fi cable to LTE router
- The router assigns an internal IP, typically in:

```
192.168.x.x
```
- Router handles outgoing network requests from the drone.


### Stage 3: LTE Router → Public Server
- The router forwards ports to allow external servers to access the drone.
- Example forwarded ports:
- 5000: Telemetry data
- 8080: Command channel
- Communication methods:
- TCP/UDP sockets
- WebSocket (if using real-time bidirectional traffic)


### Stage 4: Public Server → Web Client
- The server exposes REST or WebSocket APIs.
- Handles:
- Sending commands (Arm/Takeoff/Land)
- Receiving telemetry and forwarding it to the UI
- Client displays data and allows user control.


## Command Flow

**Web Client → Server → Drone**
1. User clicks "Takeoff"  
2. Web UI sends command to server  
3. Server forwards command to drone  
4. Companion Computer forwards MAVLink message to PX4  
5. PX4 executes command and returns acknowledgment  


## Telemetry Flow

**Drone → Server → Web Client**
1. PX4 publishes data through MAVLink  
2. Companion Computer formats and transmits data  
3. LTE router sends packets to server  
4. Server stores/forwards data  
5. Web UI displays updated values in real time  


## Reliability / Latency Considerations
- LTE network introduces variable latency (~50–150ms)
- Server must handle connection drops safely
- Command queueing and acknowledgment logs recommended
- Heartbeat monitoring ensures fail-safe operation


## Architecture Diagram

See: `network_flow_diagram.png`

This diagram visually represents:
- Command flow
- Telemetry flow
- Network components
