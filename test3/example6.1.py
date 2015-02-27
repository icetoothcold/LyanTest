#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Lyan'

import string
print string.ascii_uppercase
print string.ascii_lowercase
print string.ascii_letters

alphas=string.ascii_letters+'_'
nums=string.digits

print u'Welcome to the Identifier Check V1.0'
print u'only can check the identifier at least 2 chars long'

identifier=raw_input(u'input the identifire to check >>> ')
idlenth=len(identifier)
if idlenth>2 :
    if identifier[0] in alphas :
        for i in identifier[1:] :
            if i in alphas+nums :
                pass
            else:
                print u'%s 不符合规则' %i
        print u'检查完毕'
    else:
        print u'第一位必须是字母或者\'_\''
else:
    print u'***identifier at least 2 chars long***'