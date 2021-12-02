from bulbController import bulbStatus, fetchBulbIPAddress, setBrightness, turnOn, turnOff, toggle, displayScene

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

def displayBulbScene(sceneID):
    return displayScene(sceneID)

def setBulbBrightness(brightness):
    return setBrightness(brightness)