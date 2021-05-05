from bulbController import bulbStatus, fetchBulbIPAddress, turnOn, turnOff, toggle

def getBulbStatus():
    return bulbStatus()

def getBulbIpAddress():
    return fetchBulbIPAddress()

def turnOnBulb():
    return turnOn()

def turnOffBulb():
    return turnOff()

def toggleBulb():
    return toggle()