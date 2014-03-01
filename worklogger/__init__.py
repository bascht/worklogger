#!/usr/bin/env python
# -- encoding: utf-8 --

import os
import sys
import time
import argparse

from worklog import Worklog
from logger import Logger

WORKLOG = '/tmp/Worklog.md'
worklog = Worklog(WORKLOG)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Your friendly neighborhood worklogger')
    subparsers = parser.add_subparsers()

    log = subparsers.add_parser('log')
    log.add_argument('--text')
    log.set_defaults(subparser='log')

    loop = subparsers.add_parser('loop')
    loop.set_defaults(subparser='loop')

    today = subparsers.add_parser('today')
    today.set_defaults(subparser='today')

    args = parser.parse_args()

    if args.subparser == 'today':
        Logger.today(worklog)
    elif args.subparser == 'log':
        Logger.log(worklog)
    else:
        while(True):
            time.sleep(5)
            Logger.log(worklog)
