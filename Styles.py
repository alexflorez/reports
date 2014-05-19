__author__ = 'Alex Florez'

import xlwt

class Styles():
    styles = dict(
        style_ct='font: bold 1; align: horiz centre;'
                 'border: top thin, right thin, bottom thin, left thin;',
        style_nm='border: top thin, right thin, bottom thin, left thin;',
        style_lt='align: horiz centre;'
                 'pattern: pattern solid, fore_color red;'
                 'font: bold 1, color white;'
                 'border: top thin, right thin, bottom thin, left thin;',
        style_wrong='pattern: pattern solid, fore_color yellow;'
                 'font: bold 1, color red;'
                 'border: top thin, right thin, bottom thin, left thin;',
        style_pm='align: horiz centre;'
                 'pattern: pattern solid, fore_color light_blue;'
                 'font: bold 1, color white;'
                 'border: top thin, right thin, bottom thin, left thin;',
        style_tt='font: name Times New Roman, bold 1, height 320;'
                 'align: horiz centre;'
                 'border: top thin, right thin, bottom thin, left thin;',
        style_hd='font: bold 1, height 240, name Times New Roman;'
                 'align: horiz centre;'
                 'border: top thin, right thin, bottom thin, left thin;',
        style_bk='font: bold 1, height 240, name Times New Roman;'
                 'align: horiz centre;'
    )
    STYLE_WRONG = xlwt.easyxf(styles['style_wrong'])
    STYLE_TITLE = xlwt.easyxf(styles['style_tt'])
    STYLE_HEADER = xlwt.easyxf(styles['style_hd'])
    STYLE_BLACK = xlwt.easyxf(styles['style_bk'])
    STYLE_NORMAL = xlwt.easyxf(styles['style_nm'])
    STYLE_LATE = xlwt.easyxf(styles['style_lt'])
    STYLE_CENTER = xlwt.easyxf(styles['style_ct'])
    STYLE_PERMISSION = xlwt.easyxf(styles['style_pm'])