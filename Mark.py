__author__ = 'Alex Florez'

from datetime import timedelta


def correct_marks(marks, ref_mks):
    for mk in marks:
        for n, ref in enumerate(ref_mks):
            print('Mark ', n)


class Mark():
    def __init__(self, hm_mark):
        self.raw = hm_mark
        hour, minute = hm_mark.split(':')
        self.mark = timedelta(minutes=int(minute), hours=int(hour))

    def minus(self, other):
        return self.mark - other.mark


if __name__ == '__main__':
    to_correct = ['14:11', '18:19']
    ref_marks = ['08:00', '13:00', '14:00', '17:30']
    #correct_marks(to_correct, ref_marks)
    ref = Mark('14:11')
    mk = Mark('18:00')
    print(abs(ref.minus(mk)))

