import motor
from mpython import sleep
motor.run(motor.M2, motor.CW, 100)
sleep(5)
motor.run(motor.M2, motor.CCW, 200)
sleep(5)
motor.stopall()
