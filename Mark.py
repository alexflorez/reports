__author__ = 'Alex Florez'

from datetime import timedelta


class Mark():
    def __init__(self, hm_mark):
        self.raw = hm_mark
        hour, minute = hm_mark.split(':')
        self.mark = timedelta(minutes=int(minute), hours=int(hour))

    def minus(self, other):
        return self.mark - other.mark


def closer_mark(ref_marks, mark):
    """ determine which mark is closer to the one of the reference """
    ref = Mark(mark)
    mks = [Mark(mk) for mk in ref_marks]
    minimum = [abs(ref.minus(mk)) for mk in mks]
    idx = minimum.index(min(minimum))
    return idx

def check_repeated(idxs, marks):
    """ Check if there are multiples marks referencing to only one """
    tocorrect = {}
    for i, v in enumerate(idxs):
        if v in tocorrect:
            tocorrect[v].append(marks[i])
        else:
            tocorrect[v] = [marks[i]]

    corrected = [min(v) for v in tocorrect.values()]
    return corrected


def find_indexes(marks, ref_mks):
    idx = []
    for mk in marks:
        ik = closer_mark(ref_mks, mk)
        idx.append(ik)

    return idx

def test():
    # 07:30 a 17:00
    testing = [ ['07:37', '12:06', '17:07'],
                ['07:23', '12:50', '17:30'],
                ['07:24', '12:11', '12:47'],
                ['07:31', '12:08', '17:00'],
                ['07:34', '12:03', '13:01'],
                ['07:21', '12:09', '12:30', '13:05', '17:07'] ]

    # 13:00 a 21:00
    #testing = [['12:54']]

    # 05:30 a 13:00
    #testing = [['04:57'], ['04:50'], ['04:53'], ['04:53', '13:02', '13:16'], ['05:04', '13:06', '13:22'] ]

    ref_marks = ['07:30', '12:00', '13:00', '17:00']
    #ref_marks = ['13:00', '21:00']
    #ref_marks = ['05:00', '13:00']

    for t in testing:
        idxs = find_indexes(t, ref_marks)
        t = check_repeated(idxs, t)
        #print(idxs)
        for i, rm in enumerate(ref_marks):
            if i not in idxs:
                t.insert(i, rm)


if __name__ == '__main__':
    test()
    refs = ['07:00', '12:30', '13:00', '17:30']
    mk = '12:46'
    index = closer_mark(refs, mk)
    print(index)
