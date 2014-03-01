import PyZenity

class Logger:
    def __init__(self, backend):
        self.backend = backend

    def log(self, suggestion=None):
        last = self.backend.get_last()
        log = PyZenity.GetText(text="".join(last), entry_text=suggestion)
        if log:
            self.backend.append(log)
    def today(self):
        location = PyZenity.GetText('Where are we today?')
        self.backend.today(location)
