from ppadb.client import Client as AdbClient
import time

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device('DeviceName')


def bomber(number):
    for i in range(number):
        device.shell(
            f'am start -a android.intent.action.SENDTO -d sms:CCXXXXXXXXXX --es sms_body "{100 - i} bottles of '
            f'beer on the wall {100 - i} bottles of beer... you take one down pass it around {100 - (i + 1)} bottles of beer on the wall"')
        time.sleep(.3)
        device.shell("input keyevent 22")
        device.shell("input keyevent 22")
        device.shell("input keyevent 66")
        time.sleep(5)


bomber(100)
