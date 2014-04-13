# simpleduration

Parses human readable time durations simply and robustly. Gives you a
regular Python `datetime.timedelta` as output. There are other
libraries out there that do this, but they always seem over complicated
and yet don't handle the basic formats that I need to deal with.

## examples

    >>> from simpleduration import Duration
    >>> d = Duration("10 minutes")
    >>> d.timedelta().total_seconds()
    600.
    >>> Duration("1 day, 4 hours, 5 seconds").timedelta().total_seconds()
    100805.0
    >>> Duration("1.5h").timedelta().total_seconds()
    5400.0
    >>> d1 = Duration("10 minutes")
    >>> d2 = Duration("20 minutes")
    >>> d3 = Duration("30 minutes")
    >>> (d1 + d2) == d3
    True
    >>> d1 += d3
    >>> d1.timedelta().total_seconds()
    2400.0

## syntax details

It looks for one or more pairs of number + unit in the string. A
number is just anything that parses as a `float`. A unit is any of

* second
* seconds
* sec
* secs
* s
* minute
* minutes
* m
* min
* mins
* hour
* hours
* h
* hr
* hrs
* day
* days
* d

Case insensitive. Whitespace and punctuation are ignored.

Each duration found in the string is added to make the total. That's
very intuitive with durations like "1 hour 20 minutes" but may be a
little strange in some cases."45 minutes 45 minutes" would be
equivalent to "90 minutes".

If the string doesn't match this format in some way,
`simpleduration.InvalidDuration` is raised.
