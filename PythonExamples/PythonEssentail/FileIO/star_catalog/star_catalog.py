""" 
Near Star Catalog
-----------------

The file `stars.dat` contains data about some of the nearest stars.  Data is
arranged in the file in fixed-width fields::

    0:17    Star name
    18:28   Spectral class
    29:34   Apparent magnitude
    35:40   Absolute magnitude
    41:46   Parallax in thosandths of an arc second

A typical line looks like::

    Proxima Centauri  M5  e      11.05 15.49 771.8

In addition, some lines may start with the '#' character, indicating
that the line is a comment.

In this exercise you will write two functions: one that reads
in data from files of this format, and one which writes data
out to files of this format.

The data read in from the file should be returned as a list
of dictionaries, one for each star, with keys: "name",
"spectral_class", "apparent_magnitude", "absolute_magnitude",
and "parallax".

Similarly, the function that writes the data to a file should
expect a list of dictionaries of this form.

The read function should ignore comment lines, while the
write function should accept an optional argument containing
a multiline comment, which should be written at the start of
the file.

Hint
~~~~

You may want to review the lecture on string formatting and
the 'star_format' exercise.

Bonus
~~~~~

Gracefully handle errors such as invalid file names, badly
formatted data, and data which doesn't match the expected
structure (such as missing keys or values of the wrong type).

Notes
~~~~~

Data from:

    Preliminary Version of the Third Catalogue of Nearby Stars
    GLIESE W., JAHREISS H.
    Astron. Rechen-Institut, Heidelberg (1991)

"""

def read_stars(filename):
    """ Read stellar information from a file.
    
    This function opens the specified file and reads the
    data, returning a list of dictionaries.
    
    Parameters
    ----------
    
    filename : str
        The name of the file to read.
    
    Returns
    -------
    data : list of dict
        A list of dictionaries with keys "name", "spectral_class",
        "apparent_magnitude", "absolute_magnitude", and "parallax"
        containing the data from the file.
    
    """
    # your code goes here
    pass


def write_stars(filename, data, comment=None):
    """ Write stellar information to a file.
    
    This function opens the specified file and writes the
    data.
    
    Parameters
    ----------
    
    filename : str
        The name of the file to read.
        
    data : list of dict
        A list of dictionaries with keys "name", "spectral_class",
        "apparent_magnitude", "absolute_magnitude", and "parallax"
        containing the data to be written to the file.
    
    comment : str or None
        An optional comment to be written at the start of the file.
    
    """
    # your code goes here
    pass
    
    
if __name__ == "__main__":
    # test your code:
    # write all stars closer than 5 parsecs to a new file
    stars = read_stars('stars.dat')
    comment = """
All stars within 5 parsecs
Extracted from stars.dat
"""
    near_stars = [star for star in stars if 1000./star['parallax'] < 5]
    write_stars('near_stars.dat', near_stars, comment)
    
