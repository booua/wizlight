import asyncio
from pywizlight import wizlight, PilotBuilder, discovery
from asgiref.sync import async_to_sync
from dbcontroller import saveIpAddress, getIpAddress
from scenes import scenes

@async_to_sync
async def fetchBulbIPAddress():
    bulbs = await discovery.find_wizlights()
    ip_address = bulbs[0].ip_address
    saveIpAddress(ip_address)
    print(ip_address)
    return ip_address

@async_to_sync
async def bulbStatus():
    ip_address = getIpAddress()
    light = wizlight(ip_address)
    state = await light.updateState()
    stateDict = state.__dict__
    print(stateDict)
    statusObj = {
        "state": stateDict['pilotResult']['state'],
        "dimming": stateDict['pilotResult']['dimming'],
        "sceneName": scenes[stateDict['pilotResult']['sceneId']],
        "stateName": "on" if stateDict['pilotResult']['state'] else "off",
        "ip_address": ip_address,
    }
    return statusObj

@async_to_sync
async def turnOff():
    ip_address = getIpAddress()
    light = wizlight(ip_address)
    await light.turn_off()

@async_to_sync
async def turnOn():
    ip_address = getIpAddress()
    light = wizlight(ip_address)
    await light.turn_on()

@async_to_sync
async def toggle():
    ip_address = getIpAddress()
    light = wizlight(ip_address)
    await light.lightSwitch()

