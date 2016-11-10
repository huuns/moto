# -*- coding:utf-8 -*-

#reference : http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python

def pw_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
