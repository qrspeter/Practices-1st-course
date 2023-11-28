# based on https://stackoverflow.com/questions/67257646/get-control-over-thorlabs-pm100usb-from-python

# import visa
import pyvisa as visa
from ThorlabsPM100 import ThorlabsPM100

import time

rm = visa.ResourceManager()
print(rm.list_resources())

# AttributeError: module 'visa' has no attribute 'ResourceManager'
# исправил
# Вывод: ('USB0::0x1313::0x8078::P0013429::INSTR',)



inst = rm.open_resource('USB0::0x1313::0x8078::P0013429::INSTR')
power_meter = ThorlabsPM100(inst=inst)

inst.timeout = None

power_meter.system.beeper.immediate() 

print(power_meter.read) # Read-only property # Timeout expired before operation completed.
print(power_meter.sense.average.count) # read property
power_meter.sense.average.count = 10 # write property


# по ссылке вверху рекомендуют посмотреть на пример https://github.com/clade/ThorlabsPM100/blob/master/example.py

print("Current value    :", power_meter.read)
power_meter.sense.power.dc.range.auto = "ON"
print("Measurement type :", power_meter.getconfigure)
print("Current value    :", power_meter.read)

print(inst.query("*IDN?"))
print(rm)
print(inst)

for x in range(20):
    print(f"Current value: {power_meter.read:.3e}")
#    print("Current value: ", power_meter.read)
    time.sleep(0.1)
