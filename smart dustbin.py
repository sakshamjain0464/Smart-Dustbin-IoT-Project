from machine import Pin
from servo import Servo
import utime
import time
trigger = Pin(15, Pin.OUT)
echo = Pin(13, Pin.IN)
servo=Servo(16)
buzzer=Pin(11, Pin.OUT)
def ultrasonic():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   return distance
while True:
   distance=ultrasonic()
   print(distance)
   if(distance<8):
       servo.write(160)
       buzzer.value(1)
       time.sleep(0.5)
       buzzer.value(0)
       time.sleep(1)
       servo.write(0)
   time.sleep(0.1)

