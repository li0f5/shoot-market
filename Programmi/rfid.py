import serial

arduino = serial.Serial('COM7', 9600)

def readuid():
    return arduino.readline().removesuffix(b'\n').decode()