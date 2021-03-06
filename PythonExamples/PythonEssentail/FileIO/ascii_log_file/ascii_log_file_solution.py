"""
ASCII Log File
--------------

Read in a set of logs from an ASCII file.

Read in the logs found in the file `short_logs.crv`.
The logs are arranged as follows::

    DEPTH    S-SONIC    P-SONIC ...
    8922.0   171.7472   86.5657
    8922.5   171.7398   86.5638
    8923.0   171.7325   86.5619
    8923.5   171.7287   86.5600
    ...

So the first line is a list of log names for each column of numbers.
The columns are the log values for the given log.

Make a dictionary with keys as the log names and values as the
log data::

    >>> logs['DEPTH']
    [8922.0, 8922.5, 8923.0, ...]
    >>> logs['S-SONIC']
    [171.7472, 171.7398, 171.7325, ...]

Bonus
~~~~~

Time your example using::

    run -t 'ascii_log_file.py'

And see if you can come up with a faster solution. You may want to try the
`long_logs.crv` file in this same directory for timing, as it is much larger
than the `short_logs.crv` file. As a hint, reading the data portion of the
array in at one time combined with strided slicing of lists is useful here.

Bonus Bonus
~~~~~~~~~~~

Make your example a function so that it can be used in later parts of the class
to read in log files::

        def read_crv(file_name):
            ...

"""

log_file = open('long_logs.crv')

# The first line is a header that has all the log names:
header = log_file.readline()
log_names = header.split()
log_count = len(log_names)

# Read in each row of values, converting them to floats as
# they are read in.  Assign them to the log name for their
# particular column:
logs = {}

# Initialize the logs dictionary so that it contains the log names
# as keys, and an empty list for the values.
for name in log_names:
    logs[name] = []

for line in log_file:
    values = [float(val) for val in line.split()]
    for i, name in enumerate(log_names):
        logs[name].append(values[i])

log_file.close()

# output the first 10 values for the DEPTH log.

print 'DEPTH:', logs['DEPTH'][:10]
