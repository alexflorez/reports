__author__ = 'Alex Florez'


class Report:
    def header(self):
        raise NotImplementedError

    def content(self):
        raise NotImplementedError

    def footer(self):
        raise NotImplementedError

    def report(self):
        self.header()
        self.content()
        self.footer()


class DailyReport(Report):
    pass