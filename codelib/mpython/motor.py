from mpython import i2c
M1, M2 = 0, 2
CW, CCW = 0, 1
def run(port, direction, speed):
    '''
    port: 0 for M1, 2 for M2
    direction: 0 or 1
    speed: 0~255
    '''
    global i2c
    i2c.writeto(0x10, bytearray([port, direction, speed]))
    return

def stop(port):
    global i2c
    i2c.writeto(0x10, bytearray([port, 0, 0]))
    
def stopall():
    global i2c
    i2c.writeto(0x10, bytearray([0, 0, 0]))
    i2c.writeto(0x10, bytearray([2, 0, 0]))
    