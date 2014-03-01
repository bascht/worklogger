class Logger:
    def __init__(self, backend, frontend):
        self.backend = backend
        self.frontend = frontend

    def log(self, suggestion=None):
        last = self.backend.get_last()
        log = self.frontend.query(text="".join(last), suggestion=suggestion)
        if log:
            self.backend.append(log)

    def today(self):
        location = self.frontend.query(text='Where are we today?')
        self.backend.today(location)
