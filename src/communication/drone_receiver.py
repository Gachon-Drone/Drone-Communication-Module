# ground_receiver.py
# "Earthland" Role: Receive MAVLink messages and output them in a human way

from pymavlink import mavutil

# Receive to 14550 port sent by drone
the_connection = mavutil.mavlink_connection('udp:127.0.0.1:14550')

print("[RECEIVER] MAVLink 지상국 리시버 시작")

# First HEARTBEAT wait (for system connection verification)
print("[RECEIVER] 첫 HEARTBEAT를 기다리는 중...")
the_connection.wait_heartbeat()
print(f"[RECEIVER] HEARTBEAT 수신! 시스템 ID={the_connection.target_system}, 컴포넌트 ID={the_connection.target_component}")

while True:
    msg = the_connection.recv_match(blocking=True)
    if not msg:
        continue

    msg_type = msg.get_type()

    if msg_type == "HEARTBEAT":
        print(f"[RECEIVER] HEARTBEAT - base_mode={msg.base_mode}, system_status={msg.system_status}")

    elif msg_type == "ATTITUDE":
        # Radian → conversion to degrees
        import math
        roll_deg = math.degrees(msg.roll)
        pitch_deg = math.degrees(msg.pitch)
        yaw_deg = math.degrees(msg.yaw)
        print(f"[RECEIVER] ATTITUDE - roll={roll_deg:6.2f}°, pitch={pitch_deg:6.2f}°, yaw={yaw_deg:6.2f}°")

    elif msg_type == "GLOBAL_POSITION_INT":
        # 1e7, 1e3 scaled and came in
        lat = msg.lat / 1e7
        lon = msg.lon / 1e7
        alt = msg.alt / 1000.0  # mm -> m
        print(f"[RECEIVER] GLOBAL_POSITION_INT - lat={lat:.6f}, lon={lon:.6f}, alt={alt:.2f} m")

    else:
        # You can also take other messages if you need them
        # print(f"[RECEIVER] {msg_type}: {msg}")
        pass
