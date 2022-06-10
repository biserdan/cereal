import cereal.messaging as messaging
import time
# test publisher cereal
# in publisher
pm = messaging.PubMaster(['sensorEvents'])
dat = messaging.new_message('sensorEvents', size=1)
for x in range(10):
    dat.sensorEvents[0] = {"gyro": {"v": [0.1, -0.1, x]}}
    pm.send('sensorEvents', dat)
    time.sleep(1.0)

