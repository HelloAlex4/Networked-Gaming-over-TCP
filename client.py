import socket
import keyboard

def send_message(message, host='192.168.1.2', port=12345):
    # Create a socket object
    s = socket.socket()
    
    # Connect to the server
    s.connect((host, port))
    
    s.send(message.encode())
    
    # Close the socket
    s.close()

def on_key_event(event):
    if event.name == 'a' or event.name == "left":
        send_message("LEFT")
    if event.name == 's' or event.name == "down":
        send_message("DOWN")
    if event.name == 'd' or event.name == "right":
        send_message("RIGHT")
    if event.name == 'w' or event.name == "up":
        send_message("UP")

keyboard.on_press(on_key_event)
keyboard.wait('esc')