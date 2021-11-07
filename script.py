# Import library's 
import time
from bme280 import BME280
from ltr559 import LTR559
ltr559 = LTR559()
from enviroplus import gas
from pms5003 import PMS5003
bme280 = BME280()
pms5003 = PMS5003()
gases = gas.read_all()
particulate = pms5003.read()

# Gathers Readings from sensors


temperature = bme280.get_temperature()
pressure = bme280.get_pressure()
humidity = bme280.get_humidity()
light = ltr559.get_lux()
reducing = gases.reducing
oxidising =  gases.oxidising
nh3 = gases.nh3
PM1 = particulate.pm_ug_per_m3(1)
PM25 = particulate.pm_ug_per_m3(2.5)
PM10 = particulate.pm_ug_per_m3(10)

# Prints Readings to console

print("Temperature: %0.1f C" % temperature)
print("Pressure: %0.1f hPa" % pressure)
print("Humidity: %0.1f %%" % humidity)
print("Light: %0.1f lx" % light)
print("Reducing: %0.1f ppm" % reducing)
print("Oxidising: %0.1f ppm" % oxidising)
print("NH3: %0.1f ppm" % nh3)
print("PM1: %0.1f ug/m3" % PM1)
print("PM2.5: %0.1f ug/m3" % PM25)
print("PM10: %0.1f ug/m3" % PM10)

