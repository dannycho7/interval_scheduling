#! /usr/bin/python2
import sys
from math import ceil

def interval_comp(a, b):
	return 1 if (a[1] > b[1]) == True else -1

def find_opt_sched(intervals_in):
	intervals = list(intervals_in)
	intervals.sort(interval_comp)
	intervals = [(0, 0, 0)] + intervals # make intervals a 1-indexed array by adding a dummy entry in the beginning

	def find_latest_compatible_interval(start_time, j = len(intervals) - 1):
		# returns index i where intervals[i] end <= start_time and intervals[i + 1] end > start_time
		i = 0
		while i != j - 1:
			mid = int(ceil((i + j) / 2))
			if intervals[mid][1] <= start_time:
				i = mid
			else:
				j = mid
		return i

	opt_sched = [-1] * len(intervals) # opt_sched[i] is payoff of the optimal schedule using all elements with index j <= i 
	opt_sched[0] = 0
	prev_interval = [0] * len(opt_sched) # prev_interval[i] = the interval index used for calculation of opt_sched[i]
	used_for_opt = [False] * len(opt_sched) # used_for_opt[i] = True/False based on if the current interval was used for calculating opt_sched[i]

	for i in range(1, len(opt_sched)):
		opt_sched[i] = opt_sched[i - 1]
		prev_interval[i] = i - 1
		start_time, end_time, payoff = intervals[i]

		latest_compatible_endtime_index = find_latest_compatible_interval(start_time, i)
		including_current_payoff = opt_sched[latest_compatible_endtime_index] + payoff
		if including_current_payoff > opt_sched[i]:
			opt_sched[i] = including_current_payoff
			prev_interval[i] = latest_compatible_endtime_index
			used_for_opt[i] = True

	print "Maximum Payoff: " + str(opt_sched[len(opt_sched) - 1])

	# printing schedule
	reverse_print_buf = []
	current_int_i = len(prev_interval) - 1
	while current_int_i != 0:
		if used_for_opt[current_int_i]:
			start_time, end_time, payoff = intervals[current_int_i]
			reverse_print_buf.append("{0} {1} {2}".format(start_time, end_time, payoff))
		current_int_i = prev_interval[current_int_i]

	for i in range(0, len(reverse_print_buf)):
		print reverse_print_buf[len(reverse_print_buf) - i - 1]

intervals = []
for line in sys.stdin:
	start_time, end_time, payoff = map(lambda x: int(x), line.strip().split(" "))
	intervals.append((start_time, end_time, payoff))

find_opt_sched(intervals)