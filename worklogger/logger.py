import PyZenity

class Logger:
    @staticmethod
    def log(backend):
        last = backend.get_last()
        log = PyZenity.GetText("".join(last))
        if log:
            backend.append(log)
    @staticmethod
    def today(backend):
        location = PyZenity.GetText('Where are we today?')
        backend.today(location)
