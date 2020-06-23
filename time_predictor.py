#!/usr/bin/env python3

import csv
import operator
import collections
from datetime import datetime

#assumption - time is in "Y-m-d HH:MM:SS"


def time_averages():
	with open('issues.csv','r') as file:
		fields=file.readline().strip().split(',')
		issues=csv.DictReader(file,',')
		issues.fieldnames=fields
		answer_time=datetime.now()-datetime.now()
		answer_time_count=0
		abandoned_time=datetime.now()-datetime.now()
		abandoned_time_count=0
		for issue in issues:
			t_start=datetime.strptime(issue['start_time'],"%Y-%m-%d %H:%M:%S")
			if issue['result']=='abandoned':
				t_end=datetime.strptime(issue['abandoned_time'],"%Y-%m-%d %H:%M:%S")
				if t_end>=t_start:
					t_diff=t_end-t_start
					abandoned_time+=t_diff
					abandoned_time_count+=1
			elif issue['result']=='resolved':
				t_end=datetime.strptime(issue['answer_time'],"%Y-%m-%d %H:%M:%S")
				if t_end>=t_start:
					t_diff=t_end-t_start
					answer_time+=t_diff
					answer_time_count+=1
			else :
				print("Please enter valid response")
	return answer_time,answer_time_count,abandoned_time,abandoned_time_count

def seconds_to_time(average):
	days=average.days
	seconds=average.seconds
	hours=seconds//3600
	minutes=(seconds//60)%60
	seconds=seconds-minutes*60-hours*3600
	ans="{} days , {}:{}:{}".format(days,hours,minutes,seconds)
	return ans
def predict_time():
	answer_time,answer_count,abandon_time,abandon_count=time_averages()
	answer=datetime.now()-datetime.now()
	total_count=answer_count+abandon_count
	if total_count==0:
		print("Wrong input")
	else:
		average=(answer_time+abandon_time*abandon_count)/total_count
		time=seconds_to_time(average)
		print(time)	

predict_time()