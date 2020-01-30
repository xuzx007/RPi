import RPi.GPIO as GPIO
import time
import sys

fan_pin = 12 #BCM number
delaystart = 5
delay = 20 #
pwm_freq = 25 #Hz

dutyCycleLevel00 = 0
spinFanLevel01 = 45
dutyCycleLevel01 = 30
spinFanLevel02 = 55
dutyCycleLevel02 = 60
spinFanLevel03 = 60
dutyCycleLevel03 = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT, initial=GPIO.LOW)
fan = GPIO.PWM(fan_pin, pwm_freq)
fan.start(100) # start the PWM on 100 percent duty cycle, duty cycle value can be 0.0 to 100.0%, floats are OK
time.sleep(delaystart)

try:
    while(1):
         cpuTempFile = open("/sys/class/thermal/thermal_zone0/temp", "r")
         cpuTemp = float(cpuTempFile.read()) / 1000
         cpuTempFile.close()

         if cpuTemp <= spinFanLevel01:
             fan.ChangeDutyCycle(dutyCycleLevel00)
         elif spinFanLevel01 < cpuTemp <= spinFanLevel02:
             fan.ChangeDutyCycle(dutyCycleLevel01)
         elif spinFanLevel02 < cpuTemp <= spinFanLevel03:
             fan.ChangeDutyCycle(dutyCycleLevel02)
         else:
             fan.ChangeDutyCycle(dutyCycleLevel03)
         time.sleep(delay)

except KeyboardInterrupt:
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()
