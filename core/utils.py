import serial.tools.list_ports


def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    list = []
    for port in ports:
        dict = {
            "port" : port.device,
            "description":f"Port: {port.device}, Description: {port.description}"
        }
        list.append(dict)


    return list