#!/usr/bin/env python

import time, sys, os, subprocess

path = '/home/diogo/i386/blink1/commandline/blink1-tool'

cmd_on      = ' --on'
cmd_off     = ' --off'
cmd_red     = ' --red'
cmd_green   = ' --green'
cmd_blue    = ' --blue'
cmd_rgb     = ' --rgb '
cmd_blink   = ' --blink '
cmd_random  = ' --random '
cmd_list    = ' --list'
cmd_version = ' --version'

opt_fade    = ' -m ' # written in milliseconds
opt_timing  = ' -t ' # written in milliseconds

time_interval = 1.75

class Blink1:

	def __init__(self):
		output = subprocess.Popen(path + cmd_list, stdout=subprocess.PIPE, shell=True)
		output = output.stdout.read()
		if (output[:2] == 'no'):
			raise NameError('No blink1 Device Found!')

	def breath(self, interval):
		command = path + opt_fade + str(interval * 1000) + cmd_off
		subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
		time.sleep(interval)

		command = path + opt_fade + str(interval * 1000) + cmd_on
		subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
		time.sleep(interval)


if __name__ == '__main__':

	bl1 = Blink1()	

	while 1:
		bl1.breath(time_interval)
