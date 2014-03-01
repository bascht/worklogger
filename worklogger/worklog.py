import string
import time

class Worklog:
    def __init__(self, logfile):
        self.logfile = logfile
        print("Initialized with %s" % self.logfile)
    def write(self, line):
        logfile = open(self.logfile, 'a')
        logfile.write(line)
        logfile.close()

    def today(self, message):
        date = time.strftime('%d.%m.%Y %A')
        start_time = time.strftime('%H:%M')
        header = self.header.substitute( 
            start_time =  start_time,
            date = date,
            location = message
            )
        self.write(header)

    def append(self, message):
        log = string.Template("* $time $message\n")
        self.write(log.substitute(
            time = time.strftime('%H:%M'),
            message = message
        ))

    def get_last(self):
        lines = open(self.logfile).readlines()
        return lines[-2:]

    @property
    def header(self):
        return string.Template("\n# $date\n\n## ($start_time - 16:00)\n* @$location\n")

