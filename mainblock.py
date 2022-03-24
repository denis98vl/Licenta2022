from itertools import count
import RPi.GPIO as GPIO
import time
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory

# define factory
factory = PiGPIOFactory()


# defining pin on board
LED_PIN = 13
FLOW_SENSOR_PIN = 17
SERVO = gpiozero.Servo(18, pin_factory=factory)
ALARM = gpiozero.Buzzer(2)

# setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FLOW_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

global count
count = 0


def countPulse(channel):
    global count
    if start_counter == 1:
        count = count+1


GPIO.add_event_detect(FLOW_SENSOR_PIN, GPIO.FALLING, callback=countPulse)


# def servo_control(dutycycle):
#    pwm.set_servo_pulsewidth(SERVO_PIN, dutycycle)

#pwm = pigpio.pi()
#pwm.set_mode(SERVO_PIN, pigpio.OUTPUT)
#pwm.set_PWM_frequency(SERVO_PIN, 50)

while True:
    start_counter = 1
    time.sleep(1)
    start_counter = 0
    flow = (count / 6)  # Pulse frequency (Hz) = 6*Q, Q is flow rate in L/min.
    print("The flow is: %.3f Liter/min" % (flow))
    if flow > 0:
        GPIO.output(LED_PIN, GPIO.HIGH)
        SERVO.min()
        ALARM.beep()
        # servo_control(500)
        # time.sleep(5)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        SERVO.max()
        ALARM.off()
        # servo_control(2500)
        # time.sleep(5)
        #publish.single("/Garden.Pi/WaterFlow", flow, hostname=MQTT_SERVER)
    count = 0
