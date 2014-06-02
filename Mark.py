__author__ = 'Alex Florez'

from datetime import timedelta


class Mark():
    def __init__(self, hm_mark):
        self.raw = hm_mark
        hour, minute = hm_mark.split(':')
        self.mark = timedelta(minutes=int(minute), hours=int(hour))

    def minus(self, other):
        return self.mark - other.mark


def test_reps(idxs, limit):
    for i, v in enumerate(idxs):
        if idxs.count(v) > 1:
            nidx = idxs[i] + 1
            if nidx > limit or nidx in idxs:
                nidx = idxs[i] - 1
            idxs[i] = nidx
    return idxs


def correct_marks(marks, ref_mks):

    idx = []
    for mk in marks:
        i = Mark(mk)
        n_mark = []
        for n, refmk in enumerate(ref_mks):
            j = Mark(refmk)
            n_mark.append(abs(i.minus(j)))
        elem = n_mark.index(min(n_mark))
        idx.append(elem)
    idx = test_reps(idx, len(ref_mks) - 1)
    return idx


def test():
    testing = [ ['08:03', '13:52', '14:56', '17:40'],
                ['07:57', '13:49', '14:51', '18:07'],
                ['08:10', '14:40', '15:37', '20:47'],
                ['07:43', '13:51', '14:51', '17:54'],
                ['08:04', '13:52', '14:50', '18:44'],
                ['07:59', '14:04', '15:00', '18:06'],
                ['08:06', '13:47', '15:05', '18:11'],
                ['07:57', '13:47', '18:02'],
                ['08:11', '13:24', '14:44', '17:57'],
                ['07:56', '13:48', '14:51', '17:41'],
                ['08:00', '13:49', '14:50', '17:52'],
                ['08:07', '13:35', '14:30', '17:53'],
                ['12:27', '13:53', '14:50', '17:30'],
                ['08:08', '15:05', '17:34'] ]

    testing = [['12:27', '13:53', '14:50', '17:30']]
    ref_marks = ['08:00', '13:00', '14:00', '17:30']

    for t in testing:
        idxs = correct_marks(t, ref_marks)
        print(idxs)
        for i, rm in enumerate(ref_marks):
            if i not in idxs:
                t.insert(i, rm)
        print(t)


if __name__ == '__main__':
    correct_this = ['14:11', '18:19']
    ref_marks = ['08:00', '13:00', '14:00', '17:30']
    #correct_marks(correct_this, ref_marks)
    #ref = Mark('14:11')
    #mk = Mark('08:00')
    #print(ref.minus(mk))
    test()