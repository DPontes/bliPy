#A Python wrapper for thingM's blink(1) USB RGB LED

Takes the commandline instructions located at '~/.../blink1/commandline/blink1-tool' and creates classes so that it can be more easily used in a Python script

Remember to change the value of 'path' in the bliPy.py file to suit your case.

Example Python code:
 import bliPy
 interval = 1.75
 bl1 = bliPy.Blink1()
 bl1.breath(interval)

You'll see your blink(1) 'breathing' one cycle similar to the Macbooks led with a white light

