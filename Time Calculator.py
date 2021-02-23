#defining function
def add_time (start_time, duration_time, starting_day='' ):
	print (starting_day)
	days = {0 : 'Sunday', 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday',5 : 'Friday', 6 : 'Saturday'}
	#processing days into values
	if len(starting_day) > 1:
		keys = list(days.keys())
		values = list(days.values())
		starting = starting_day.capitalize()
		ordinal = values.index(str(starting))
	#dissecting start_time into string
	stime = start_time.split()
	stimetime = stime[0].split(':')
	halftime = stime[1].upper()
	#dissecting duration_time
	duratime = duration_time.split(':')
	#adding hours
	hours_time = int(stimetime[0]) + int(duratime[0])
	hourtime = hours_time
	#adding minutes
	min_time = int(stimetime[1]) + int (duratime[1])
	minutestimes = min_time
	cycle = 0
	x = ''
	#checking for rollovers
	#rollover minutes
	if int(min_time) >= 60:
		if int(min_time) >= 60:
			minutestimes = int(min_time) - 60
			hourtime = int(hours_time) + 1
	#rollover hours
	if int(hourtime) >= 12:
		if int(hourtime) > 12:
			while int(hourtime) > 12:
				if str(halftime) == 'AM':
					halftime = 'PM'
				else:
					halftime = 'AM'
					cycle = cycle + 2
				hourtime = int(hourtime) - 12
		if int(hourtime) == 12:
			if str(halftime) == 'AM':
				halftime = 'PM'
			else:
				halftime = 'AM'
				cycle = cycle + 2
		day = cycle*0.5
		#grouping for default x value
		if len(starting_day) > 0 or day > 0:
		#checking how many days have passed
			text =''
			if day > 0:
				if day == 1:
					text = '(next day)'
				else:
					text = '(' + str(int(day)) + ' ' + 'days' + ' ' + 'later' + ')'
		# checking if there is a start day involved:
			startday = ''
			post = ''
			if len(starting_day) > 0:
				if day < 1:
					startday = starting
				else:
					days_passed = int(ordinal) + int(day)
					if days_passed < 7:
						post = days_passed
					while days_passed >= 7:
						post = days_passed - 7
					startday = values[post]
			x = startday + text
	# adding zeroes to make the time two- digits
	if len(str(minutestimes)) < 2:
		if len (str(minutestimes)) < 2:
			minutestimes = '0' + str(minutestimes)
	new_time = print('# Returns:' + ' ' + str(hourtime) + ':' + str(minutestimes) + ' ' + str(halftime) + ' ' + x)
	return new_time