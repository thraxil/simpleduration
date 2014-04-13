from datetime import timedelta

"""
<number> := [0-9]*.?[0-9]*
<duration> := (<number>\s*<unit>)+
"""

units = {
    'second': 1,
    'seconds': 1,
    'sec': 1,
    'secs': 1,
    's': 1,
    'minute': 60,
    'minutes': 60,
    'm': 60,
    'min': 60,
    'mins': 60,
    'hour': 3600,
    'hours': 3600,
    'h': 3600,
    'hr': 3600,
    'hrs': 3600,
    'day': 3600 * 24,
    'days': 3600 * 24,
    'd': 3600 * 24,
}


class InvalidDuration(Exception):
    pass


def parse_single(n, u):
    if u.lower() not in units:
        raise InvalidDuration
    try:
        float(n)
    except:
        raise InvalidDuration
    return float(n) * units[u.lower()]


class Duration(object):
    def __init__(self, s, seconds=None):
        self.seconds = 0.0
        if seconds is not None:
            self.seconds = seconds
            return
        n_parts = []
        u_parts = []

        state = 'n'  # has to start with a number
        for c in s:
            if c == '.' or (c >= '0' and c <= '9'):
                if state == 'u':
                    # finished parsing a unit, now back on a number
                    # that means we need to take what was there and
                    # add it in
                    u = ''.join(u_parts)
                    n = ''.join(n_parts)
                    self.seconds += parse_single(n, u)
                    u_parts = []
                    n_parts = []
                    state = 'n'
                n_parts.append(c)
            if c >= 'A' and c <= 'z':
                if state == 'n':
                    # parsing a unit now
                    state = 'u'
                u_parts.append(c)
        # we've consumed all the chars. if we're still in 'u'
        # it means we have one more to add in
        if state == 'u':
            u = ''.join(u_parts)
            n = ''.join(n_parts)
            self.seconds += parse_single(n, u)
        else:
            if len(n_parts) > 0:
                # we have a number but no units
                raise InvalidDuration

    def timedelta(self):
        return timedelta(seconds=self.seconds)

    def __eq__(self, other):
        return self.seconds == other

    def __ne__(self, other):
        return self.seconds != other

    def __lt__(self, other):
        return self.seconds < other

    def __gt__(self, other):
        return self.seconds > other

    def __add__(self, other):
        return Duration("", seconds=self.seconds + other)

    def __radd__(self, other):
        return self.seconds + other

    def __sub__(self, other):
        return Duration("", seconds=self.seconds - other)

    def __rsub__(self, other):
        return other - self.seconds

    def __mul__(self, other):
        return Duration("", seconds=self.seconds * other)

    def __rmul__(self, other):
        return self.seconds * other

    def __iadd__(self, other):
        return Duration("", seconds=self.seconds + other)

    def __isub__(self, other):
        return Duration("", seconds=self.seconds - other)

    def __imul__(self, other):
        return Duration("", seconds=self.seconds * other)
