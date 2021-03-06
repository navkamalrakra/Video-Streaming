import cv2
import zmq

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://192.168.1.8:5555')

camera = cv2.VideoCapture(0)

while True:
    try:
        grabbed, frame = camera.read()
        frame = cv2.resize(frame, (640, 480))
        encoded, buffer = cv2.imencode('.jpeg', frame)
        footage_socket.send(buffer)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break