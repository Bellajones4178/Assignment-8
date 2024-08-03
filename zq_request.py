# Import packages
import zmq

def send_request():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    while True:
        script = input("Send request (yes/no): ").strip().lower()
        if script == "yes":
            socket.send_string(script)
            response = socket.recv_string()
            print(f"Received response: '{response}'")
        elif script == "no":
            socket.send_string(script)
            response = socket.recv_string()
            print(f"Received response: {response}")
            break
        else:
            print("Please enter yes or no.")

if __name__ == "__main__":
    send_request()