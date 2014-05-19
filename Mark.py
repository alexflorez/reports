__author__ = 'Alex Florez'

from datetime import timedelta


def correct_marks(marks, ref_mks):
    for mk in marks:
        for n, ref in enumerate(ref_mks):
            print('Mark ', n)


class Mark():
    def __init__(self, hm_mark):
        hour, min = hm_mark.split(':')
        self.mark = timedelta(minutes=int(min), hours=int(hour))

    def minus(self, other):
        return self.mark - other.mark


if __name__ == '__main__':
    correct_this = ['14:11', '18:19']
    ref_marks = ['08:00', '13:00', '14:00', '17:30']
    #correct_marks(correct_this, ref_marks)
    ref = Mark('14:11')
    mk = Mark('08:00')
    print(ref.minus(mk))