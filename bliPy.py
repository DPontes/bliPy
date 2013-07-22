#!/usr/bin/env python

import time, sys, os, subprocess

path = '/home/diogo/i386/blink1-tool'

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


def emitCommand(command):

    output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = output.stdout.read()
    return output


class Blink1:

    def __init__(self):
        output = emitCommand(path + cmd_list)
        if (output[:2] == 'no'):
		    raise NameError('No blink1 Device Found!')

    def breath(self, interval, rgb = None):
        command = path + opt_fade + str(interval * 1000) + cmd_off
        emitCommand(command)
        time.sleep(interval)
        if(rgb != None):
            color = ','.join(str(x) for x in rgb)
            command = path + opt_fade + str(interval * 1000) + cmd_rgb + color
        else:
		    command = path + opt_fade + str(interval * 1000) + cmd_on

        emitCommand(command)
        time.sleep(interval)


if __name__ == '__main__':

    bl1 = Blink1()	

    time_interval = 1.75

    while 1:
        bl1.breath(time_interval)



