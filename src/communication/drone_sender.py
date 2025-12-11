# drone_sender.py
# "Drone" role: MAVLink HEARTBEAT + Continue sending fake posture/position information

from pymavlink import mavutil
import time
import math

# Send to UDP port to be received by the ground station (14550 is the primary port often used by MAVLink)
master = mavutil.mavlink_connection('udpout:127.0.0.1:14550')

print("[SENDER] MAVLink 드론 시뮬레이터 시작")

t0 = time.time()

while True:
    t = time.time() - t0

    # 1) Send the HEARTBEAT message (signal that the system is alive)
    master.mav.heartbeat_send(
        mavutil.mavlink.MAV_TYPE_QUADROTOR,   # Airframe Type (Quadcopter)
        mavutil.mavlink.MAV_AUTOPILOT_GENERIC,
        0, 0, 0
    )

    # 2) Send fake attitude message (roll/pitch/yo)
    roll = math.radians(10.0 * math.sin(t))
    pitch = math.radians(5.0 * math.sin(t / 2.0))
    yaw = math.radians(30.0 * math.sin(t / 3.0))

    master.mav.attitude_send(
        int(t * 1e6),   #time_boot_ms (in μs)
        roll,
        pitch,
        yaw,
        0.0, 0.0, 0.0   # The angular velocity is zero
    )

    # 3) Fake GPS/global position message (lat, lon, alt)
    base_lat = 37.450000 * 1e7  # Example: Widow near Gachon University (Daegang)
    base_lon = 127.130000 * 1e7 # Example: Hardness
    base_alt = 50.0 * 1000      # 50 m (mm)

    # It's like we're moving with time
    lat = int(base_lat + 1e5 * math.sin(t / 10.0))
    lon = int(base_lon + 1e5 * math.cos(t / 10.0))
    alt = int(base_alt + 5000 * math.sin(t / 5.0))  # Changes by ±5m

    master.mav.global_position_int_send(
        int(t * 1e3),  # time_boot_ms
        lat,
        lon,
        alt,
        alt,           # Relative_alt is the same as alt
        0, 0, 0, 0     # Speed/direction is 0
    )

    print(f"[SENDER] t={t:5.1f}s 에 HEARTBEAT + 자세 + 위치 전송")

    time.sleep(1.0)  # Send at 1-second intervals
