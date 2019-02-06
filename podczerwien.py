import pylirc, time
import RPi.GPIO as GPIO

blocking = 0;

pylirc.init("pilot", "/etc/lirc/lircd.conf", blocking)

while True:
    s = pylirc.nextcode(1);

    while(s):
        for (code) in s:
            print 'Command: ', code["config"]

        if (not_blocking):
            s = pylirc.nextcode(1);
        else:
            s = []
