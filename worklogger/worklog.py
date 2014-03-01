import string
import time


class Worklog:
    def __init__(self, logfile):
        self.logfile = logfile

    def write(self, line):
        logfile = open(self.logfile, 'a')
        logfile.write(line)
        logfile.close()

    def today(self, location):
        date = self.date
        start_time = self.time
        header = self.header.substitute(
            start_time=start_time,
            date=date,
            location=location
            )
        self.write(header)

    def append(self, message):
        log = string.Template("* $time $message\n")
        self.write(log.substitute(
            time=self.time,
            message=message
        ))

    def get_last(self, num=2):
        f = open(self.logfile)
        lines = f.readlines()
        f.close()
        return lines[-num:]

    @property
    def time(self):
        return time.strftime('%H:%M')

    @property
    def date(self):
        return time.strftime('%d.%m.%Y %A')

    @property
    def header(self):
        template = "\n# $date\n\n## ($start_time - 16:00)\n* @$location\n"
        return string.Template(template)
