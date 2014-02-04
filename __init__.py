# -*- coding: utf-8 -*-

# Extended convert encoding functions.
#copyright concentricpuddle, GPLv2
from puddlestuff.constants import COMBO


def extended_enconvert(text, enc_name):
    return text.encode("latin1", 'replace').decode(enc_name, 'replace')


functions = {'extended_enconvert': extended_enconvert}

#Use the PluginFunction class to register your function as a Function.

from puddlestuff.util import PluginFunction

func = PluginFunction('Extended Convert from non-standard encoding',
                      extended_enconvert,
                      u'Extended Convert to encoding: $0, Encoding: $1',
                      [('ComboBox: ', COMBO, 'big5', 'shift-jis',
                      'shift_jisx0213', 'gb2312', 'euc-jp', 'cp1250', 'cp1251',
                      'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256',
                      'cp1257', 'cp1258')])

functions.update({'extended_enconvert': func})
