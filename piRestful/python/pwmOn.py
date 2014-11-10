from RPIO import PWM
import time
servo = PWM.Servo()
servo.set_servo(17, 2000)
time.sleep(1)

# servo right