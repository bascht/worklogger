#!/usr/bin/env python
# -- encoding: utf-8 --

import os
import sys
import time
import argparse

from worklog import Worklog
from logger import Logger

BANNER="""
Welcome to Worklogger, your friendly neighbourhood-Logger.

Worklogger helps you keeping track your work-activities by
asking you every now and then and appending it to a markdown
file.  Worklogger uses the environment-variable $WORKLOG to find 
your worklog file. Otherwise you can use the parameter --file.

Worklogger will ask you every hour (3600 seconds) - but you
can adjust this timespan via the parameter --interval.

Running Worklogger
------------------

Start Worklogger with

    $ worklogger start

Enter new Logs by simply calling worklogger

    $ worklogger


You can also pipe logs directly into worklogger:

    $ echo "This is my entry" | worklogger
"""

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=BANNER)

    parser.add_argument('--file', dest='worklog', default=os.environ['WORKLOG'], help='Path to your Worklog.md file')
    parser.add_argument('--interval', dest='interval', default=3600, type=int, help='Interval (in Seconds) between logentries')
    parser.add_argument('start', default=False, type=bool, nargs="?")

    args = parser.parse_args()

    worklog = Worklog(args.worklog)
    logger  = Logger(worklog)

    if args.start:
        logger.today()
        while(True):
            logger.log()
            time.sleep(args.interval)
    else:
        if(sys.stdin.isatty()):
            logger.log()
        else:
            lines = (line.strip() for line in sys.stdin.readlines())
            logger.log(suggestion=" ".join(lines))

main()
