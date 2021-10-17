#.csv file is a simplified schedule made in excel, exported to csv

import itertools
import math

class employee:
	def __init__(self, name, avbl):
		self.name = name
		self.avbl = avbl

class schedule:
	def __init__(self, mon, tue, wed, thu, fri):
		self.mon = mon
		self.tue = tue
		self.wed = wed
		self.thu = thu
		self.fri = fri

def parse(str):
	file = open(str, "r")
	lines = file.readlines()
	file.close()
	for i in range(2):
		lines.remove(lines[0])
	return lines

def getname(item):
	name = ''
	for char in item:
		if char == ';':
			return name
		name += char

def getavbl(item):
	avbl = []
	for char in item:
		if char == '0' or char == '1':
			avbl.append(int(char))
	return avbl

def getobjects(file):
	employees = [employee(getname(item), getavbl(item)) for item in file]
	return employees

def combine(maxValue, repeat):
	combinations = list(itertools.combinations(range(maxValue), repeat))
	return combinations

def index2name(available, indices):
	comb_names = []
	for item in indices:
		temp = []
		for index in item:
			temp.append(available[index])
		comb_names.append(temp)
	return comb_names

def printschedule(sched):
	print(sched.mon)
	print(sched.tue)
	print(sched.wed)
	print(sched.thu)
	print(sched.fri)
	print('\n')

#this should quasi-recursively create each possibility day-by-day, not sure what's going wrong
def add_day(old_schedules, new_day):
	new_schedules = []
	for sched in old_schedules:
		new_sched = sched
		for potential in new_day:
			if sched.mon == []:
				new_sched.mon = potential
			elif sched.tue == []:
				new_sched.tue = potential
			elif sched.wed == []:
				new_sched.wed = potential
			elif sched.thu == []:
				new_sched.thu = potential
			elif sched.fri == []:
				new_sched.fri = potential
			new_schedules.append(new_sched)
	printschedule(new_sched)
	return new_schedules

emplist = getobjects(parse("rooster.csv"))

#make lists with all available employees per day
mon = []
tue = []
wed = []
thu = []
fri = []
week = [mon, tue, wed, thu, fri]

for emp in emplist:
	day = 0
	for shift in emp.avbl:
		if shift:
			week[day].append(emp.name)
		day += 1

#make lists with all possible indices for availability lists to fill each day, hardcoded 2 employees a day
pos_mon = combine(len(mon), 2)
pos_tue = combine(len(tue), 2)
pos_wed = combine(len(wed), 2)
pos_thu = combine(len(thu), 2)
pos_fri = combine(len(fri), 2)

#change indices to names
pos_mon = index2name(mon, pos_mon)
pos_tue = index2name(tue, pos_tue)
pos_wed = index2name(wed, pos_wed)
pos_thu = index2name(thu, pos_thu)
pos_fri = index2name(fri, pos_fri)

#make list of schedule objects covering all possible schedules
sched = schedule([], [], [], [], [])
pos_schedules = [sched]
pos_week = [pos_mon, pos_tue, pos_wed, pos_thu, pos_fri]
for day in pos_week:
	pos_schedules = add_day(pos_schedules, day)

print(len(pos_schedules))