# 04. LTE Router Configuration

This document describes settings required on the LTE router to enable remote drone communication over a public network.


## 4.1 Purpose

The LTE router acts as a gateway allowing:
- Drone telemetry to reach the public server
- Server commands to reach the drone
- Reliable long-distance operation without local network dependency


## 4.2 Network Layout

```
Drone (Companion Computer)
↓
LTE Router
↓
Public Internet
↓
Remote Server
```


## 4.3 Required Settings

### 1) Port Forwarding
Forward ports needed for communication:

| External Port | Internal IP       | Internal Port | Usage              |
|---------------|------------------|----------------|--------------------|
| 5000          | 192.168.x.x      | 5000           | Telemetry          |
| 8080          | 192.168.x.x      | 8080           | Command channel    |

Your actual ports may differ depending on implementation.


### 2) Static Internal IP Assignment
Assign a stable internal IP for the Companion Computer.

Example:
```
192.168.0.10
```


### 3) Firewall / NAT Settings
- Allow inbound connections on forwarded ports
- Disable aggressive NAT session timeout if possible
- Ensure outbound traffic is unrestricted


## 4.4 Connectivity Testing

### Ping Test
```
ping <public-server-ip>
```

### Port Check
Use external port-check tools to verify openness.


## 4.5 Common Issues & Solutions

- **High latency:** LTE tower congestion → try different provider  
- **No connection:** Incorrect forwarded internal IP  
- **Packets dropped:** NAT session timeout too short  
