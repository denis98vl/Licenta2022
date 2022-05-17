from itertools import count
import RPi.GPIO as GPIO
import time
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory
import paho.mqtt.client as paho
import math

# mqtt broker & client settings
broker = 'broker.hivemq.com'
port = 1883
client_id = 'MHC - Licenta'

#listener 1883 192.168.0.110
#allow_anonymous true


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker")
        else:
            print(f'Failed to connect, return code {rc}')
    client = paho.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, topic, msg):
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


# define factory
factory = PiGPIOFactory()


# defining pin on board
LED_PIN = 13
FLOW_SENSOR_PIN = 17
SERVO = gpiozero.Servo(18, min_pulse_width=0.5/1000,
                       max_pulse_width=2.5/1000, pin_factory=factory)
ALARM = gpiozero.Buzzer(2)

# setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FLOW_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def countPulse(channel):
    global count
    if start_counter == 1:
        count = count+1


if __name__ == '__main__':
    global count
    count = 0

    GPIO.add_event_detect(FLOW_SENSOR_PIN, GPIO.FALLING, callback=countPulse)

    #MQTT_CLIENT = connect_mqtt()

    while True:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        # Pulse frequency (Hz) = 6*Q, Q is flow rate in L/min.
        flow = (count / 6)
        #print(f"The flow is: {flow:.3f} Liter/min")
        #publish(MQTT_CLIENT, "MHC_DATA/DEBIT", f"{flow:.3f}")
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
        # if flow > 20:
        #     ALARM.beep()
        #     GPIO.output(LED_PIN, GPIO.HIGH)
        #     SERVO.min()
        #     time.sleep(10)
        # elif flow == 0:

        #     ALARM.off()
        #     GPIO.output(LED_PIN, GPIO.LOW)
        #     SERVO.mid()
        # else:
        #     for i in range(45, 0, -1):
        #         SERVO.value = math.sin(math.radians(i))
        #         time.sleep(flow/500)
        #     ALARM.off()
        #     GPIO.output(LED_PIN, GPIO.LOW)
        # count = 0
