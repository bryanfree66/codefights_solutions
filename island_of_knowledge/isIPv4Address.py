import socket

def isIPv4Address(inputString):
    try:
        socket.inet_pton(socket.AF_INET, inputString)
        return True
    except AttributeError:
        try:
            socket.inet_aton(inputString)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:
        return False
