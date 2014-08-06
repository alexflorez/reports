__author__ = 'Alex Florez'

from datetime import timedelta


class Mark():
    def __init__(self, date=None, hm_mark=None):
        self.date = date
        self.marks = hm_mark

    def check_marks(self, ref_marks):
        """ check registered marks respect to the reference marks"""
        idxs = self.find_indexes(ref_marks)
        self.marks = self.check_repeated(idxs)
        return self.insert_missing(idxs, ref_marks)

    def find_indexes(self, ref_mks):
        """ find the indexes where one or more marks are missing """
        idx = []
        for mk in self.marks:
            ik = self.closer_mark(ref_mks, mk)
            idx.append(ik)
        return idx

    @staticmethod
    def str2time(a_mark):
        hour, minute = a_mark.split(':')
        mk_hour = timedelta(minutes=int(minute), hours=int(hour))
        return mk_hour

    def closer_mark(self, ref_mks, a_mark):
        """ determine which mark is closer to the one of the reference """
        mks = [self.str2time(mk) for mk in ref_mks]
        a_mark = self.str2time(a_mark)
        minimum = [abs(a_mark - mk) for mk in mks]
        idx = minimum.index(min(minimum))
        return idx

    def check_repeated(self, idxs):
        """ Check if there are multiples marks referencing to only one """
        tocorrect = {}
        for i, v in enumerate(idxs):
            if v in tocorrect:
                tocorrect[v].append(self.marks[i])
            else:
                tocorrect[v] = [self.marks[i]]

        corrected = [min(v) for v in tocorrect.values()]
        return corrected

    def insert_missing(self, idxs, ref_mks):
        """ insert in appropiate position missing marks """
        for i, rm in enumerate(ref_mks):
            if i not in idxs:
                self.marks.insert(i, rm)

    def __repr__(self):
        return "Mark(date={}, marks={})".format(self.date, self.marks)


if __name__ == '__main__':
    # 07:30 a 17:00
    list_marks = [['07:37', '12:06', '17:07'],
                ['07:23', '12:50', '17:30'],
                ['07:24', '12:11', '12:47'],
                ['07:31', '12:08', '17:00'],
                ['07:34', '12:03', '13:01'],
                ['07:21', '12:09', '12:30', '13:05', '17:07'], []]

    # 13:00 a 21:00
    #list_marks = [['12:54']]

    # 05:30 a 13:00
    #list_marks = [['04:57'], ['04:50'], ['04:53'], ['04:53', '13:02', '13:16'], ['05:04', '13:06', '13:22'] ]

    refs = ['07:30', '12:00', '13:00', '17:00']
    #refs = ['13:00', '21:00']
    #refs = ['05:00', '13:00']
    fecha = '30/07/2014'
    for l_mks in list_marks:
        mark = Mark(fecha, l_mks)
        mark.check_marks(refs)
        print(mark)
