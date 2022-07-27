from machine import ADC
import time





light_levels = [65, 60, 55, 50, 45, 40, 35, 30, 25]


# convert voltage [0-65535] to light level [0-9]
def convert_to_light_level(adcv: int) -> int:
    for (i, level) in enumerate(light_levels):
        if adcv > 1000 * level:
            return i+1
    return 0



adc0 = ADC(26) 


while True:
    a0 = adc0.read_u16()
    print(adc0.read_u16())
    time.sleep(1)
