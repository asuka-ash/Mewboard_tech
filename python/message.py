import env

def send(conn, msg):
    message = msg.encode(env.FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(env.FORMAT)
    send_length += b' ' * (env.HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)

def receive(conn):
    msg_length = conn.recv(env.HEADER).decode(env.FORMAT).strip()
    if not msg_length:
        return None  # or raise an exception, depending on the use case
    msg_length = int(msg_length)
    msg = conn.recv(msg_length).decode(env.FORMAT)
    return msg

def add_listener(conn, addr):
    connected = True
    while connected:
        msg = receive(conn)
        if msg == env.DISCONNECT_MSG:
            connected = False
        print(f"[{addr}] {msg}")
    conn.close()