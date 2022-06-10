import cereal.messaging as messaging
# test subscriber cereal
# in subscriber
sm = messaging.SubMaster(['sensorEvents'])
while 1:
  sm.update()
  print(sm['sensorEvents'])