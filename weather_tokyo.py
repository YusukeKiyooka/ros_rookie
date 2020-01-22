#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import requests

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
tenki_data = requests.get(url, params=payload).json()
rospy.init_node('count')
pub = rospy.Publisher('count_up', String, queue_size=1)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
	pub.publish(tenki_data['title'])
	pub.publish(tenki_data['forecasts'][1]['date'])
	pub.publish(tenki_data['forecasts'][1]['telop'])
	pub.publish(tenki_data['forecasts'][1]['temperature']['max']['celsius'])
	pub.publish(tenki_data['forecasts'][1]['temperature']['max']['fahrenheit'])
	rate.sleep()
