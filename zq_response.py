# Import packages 
import zmq
import random
import os

# Generate dog image locally from Zaggle
def generate_dog_image():
    # Search source and pick random file 
    source = "dataset"
    img_files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
    image = random.choice(img_files)
    return os.path.join(source, image)

# Response start
def start_service():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print("Server listening on port 5555")

    while True:
        message = socket.recv_string()
        if message == "yes":
            dog_image = generate_dog_image()
            socket.send_string(dog_image)
        elif message == "no":
            response_message = "Thank you for visiting the dog image generator."
            socket.send_string(response_message)
            break

if __name__ == "__main__":
    start_service()