from fastapi import FastAPI
from smart_home import SmartHomeFacade
from bridge import RemoteController
app = FastAPI()

smart_home = SmartHomeFacade()

lighting_controller = RemoteController(smart_home.lighting)
climate_controller = RemoteController(smart_home.climate)
security_controller = RemoteController(smart_home.security)


@app.get("/security/on")
def arm_security():
    return {"status": security_controller.turn_on()}

@app.get("/security/off")
def disarm_security():
    return {"status": security_controller.turn_off()}

@app.get("/lighting/on")
def lighting_on():
    return {"status": lighting_controller.turn_on()}

@app.get("/lighting/off")
def lighting_off():
    return {"status": lighting_controller.turn_off()}

@app.get("/lighting/brightness/{level}")
def set_brightness(level: int):
    return {"status": smart_home.set_brightness(level)}

@app.get("/climate/on")
def climate_on():
    return {"status": climate_controller.turn_on()}

@app.get("/climate/off")
def climate_off():
    return {"status": climate_controller.turn_off()}

@app.get("/climatecontrole/temperature/{temp}")
def set_temperature(temp: int):
    return {"status": smart_home.activate_climate_control(temperature=temp)}

