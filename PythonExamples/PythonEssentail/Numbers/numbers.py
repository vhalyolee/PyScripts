
# coding: utf-8

# Numbers
# =======
# 
# Let's take a look at the common numerical data types within Python.
# 
# Integers
# --------
# 
# The first of these is the integer type.  We can add integers, getting another integer as the result:

# In[ ]:

1+1


# We can also assign an integer to a variable:

# In[ ]:

a = 1


# In[ ]:

a


# We can ask the variable for its type, and see that it is `int`:

# In[ ]:

type(a)


# We could assign `a` to a variable of any other type, like a float or a string or a list, but right now it's pointing at this integer.
# 
# The range of possible values of an integer depends on your system.
# 
# If you are running on a 32-bit system then you have 4 bytes per integer, then the minimum value is -2,147,483,648 and the maximum is 2,147,483,647 (roughly between positive and negative 2 billion).  That's enough for many applications, but for instance there are 300 billion stars in our galaxy, so this number falls well short of that.
# 
# But if you are running on a 64-bit system then you have 8 bytes per integer, so the range is -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (roughly 9 followed by 18 zeros).  That's more than enough to count the stars in our galaxy or seconds since the beginning of time, but not enough to count all the stars in the universe.
# 
# To see what the largest integer is on your system, the `sys` module provides standard constants for your system, and in particular `sys.maxint` holds the largest integer value:

# In[ ]:

import sys
sys.maxint


# So by looking at the output of this you can tell if you are running with a 32 or 64 bit system.

# Long Integers
# -------------
# 
# An obvious question (particularly to the troublemakers in the audience) is what happens if you add 1 to the maximum integer?

# In[ ]:

a = sys.maxint + 1


# In[ ]:

a


# As you can see, it worked, but the result has an `L` at the end, which means that this is a "long integer" or `long`.
# 
# Python's long integer data type can support arbitrarily large positive or negative integer values, but mathematical operations with them will not be as speedy as with standard integers.  However the fact that Python automatically rolls over the values for you is nice.
# 
# If you check, you can see that the type of `a` is `long`:

# In[ ]:

type(a)


# To create a long integer, you can simply type a number greater than your system's maximum integer (or less than the minimum) and Python gives you a long integer back:

# In[ ]:

a = 12345678901234567890


# In[ ]:

a


# Floating Point Numbers
# ----------------------
# 
# You can represent real numbers in Python as easily as integers.  For example, we could assign 1.4 to the variable `a`:

# In[ ]:

a = 1.4


# Notice that the type of `a` is now `float`:

# In[ ]:

type(a)


# Python's `float` data type follows the [IEEE 754 floating point standard](http://en.wikipedia.org/wiki/IEEE_floating_point), the same as C, Fortran, C# and just about every other programming language because that's what modern processors use to do math quickly.
# 
# If we add our floating point number to 1.1, we get 2.5,as we expect:

# In[ ]:

a + 1.1


# And if we add 1.2 we get 2.6:

# In[ ]:

b = a + 1.2
b


# Well, almost.  It's not quite 2.6.  If you look at the 16th decimal place it's slightly off.
# 
# This can be disconcerting if you are unfamilliar with floating point math.  The reason for this is that to minimize memory usage and maximize performance, floating point numbers take the continuous number line and divide it in little chunks.  If your number doesn't quite line up with the chunks then there will be a small round-off error.
# 
# For example, the value stored in `a` isn't 1.4, it's exactly 1.399999999999999911182158029987476766109466552734375:

# In[ ]:

print('{:.52}'.format(a))


# because that's the nearest floating point number to 1.4.
#  
# When you add numbers together, the errors can add up to the point where they are more visible. Python, instead of hiding that from you prints out all the gory details.
# 
# If you want a prettier representation of the number, it is possible to say `print(b)` or `str(b)` which uses a more-human friendly rounding (the one IPython uses by default is `repr(b)`).

# In[ ]:

print(b)


# Much like `sys.maxint` for integers, there's also `sys.float_info`:

# In[ ]:

sys.float_info


# You'll notice that it has a lot more information in it than just a single value.
# 
# There's `max`, which tells you the maximum and minimum values representable by a floating point number:

# In[ ]:

sys.float_info.max


# There's also `min` which gives the closest value to 0 that can be represented:

# In[ ]:

sys.float_info.min


# The value `epsilon` gives an upper bound on the rounding error when doing mathematical computations:

# In[ ]:

sys.float_info.epsilon


# These values are the same as double precision floating point numbers in C, which use 8 bytes, and the values are usually the same on 32 and 64 bit systems.
# 
# There's no way to specify that you want to use a different level of precision with your floating point arithmetic in standard Python, but if you use NumPy you can specify that you want to use single precision floating point numbers if you want to save memory or don't have high precision values.

# Complex Numbers
# ---------------
# 
# One of the cool things about Python is that it natively supports complex numbers.  And while you may not use them on a day-to-day basis, a lot of the mathematics that is available in NumPy and Python would not have been created if they weren't a standard part of Python because they are so important to so much analysis.
# 
# Python follows the convention used in Electrical Engineering and some parts of Physics, rather than that of Mathematics, and represents the imaginary unit with $j$ rather than $i$.
# 
# So for example:

# In[ ]:

a = 1 + 2j
a


# You precede the `j` with a floating-point number, and the value is represented with parentheses around it.
# 
# The type of the value is `complex`, as you might hope:

# In[ ]:

type(a)


# Python stores the complex number as a pair of floating point values for the real and imaginary parts, and you can access those values using the `real` and `imag` attributes:

# In[ ]:

a.real


# In[ ]:

a.imag


# In fact these also work on floating point numbers as well, with `real` just returning the floating point number and `imag` always returning 0:

# In[ ]:

b = 1.4
b.real


# In[ ]:

b.imag


# You can compute the complex conjugate by calling the `conjugate()` method of the complex number:

# In[ ]:

a.conjugate()


# More Interactive Calculation
# ----------------------------
# 
# <h3>Arithmetic Operations</h3>
# 
# Let's use an example of a more involved numerical expression to get some familiarity with Python's operation syntax and order of operations.

# In[ ]:

1 + 2 - (3*4/6)**5 + 7%5


# Looking at this, most of the operations should be straightforward, but `**` in Python indicates exponentiation, and `%` is the modulo (or remainder) operation.
# 
# Python's precedence order for operations is fairly standard (from highest to lowest):
# 
# * `( )` (parenthesis grouping)
# * `**` (exponentiation)
# * `*`, `/`, `//`, `%` (multiplication, division, integer division and modulo)
# * `+`, `-` (addition, subtraction)
# 
# So walking through this expression, the parenthesis apply first giving a sub-expression `(3*4/6)`.  Expressions of the same precedence evaluate left to right, so this simplifies to `12/6` which gives `2`:

# In[ ]:

3*4/6


# So we now have `1 + 2 - 2**5 + 7%5`.
# 
# The next operation is the power, so `2**5` is `32`:

# In[ ]:

2**5


# and the expression simplifies to `1 + 2 - 32 + 7%5`.
# 
# The modulo operation comes next, and 7 mod 5 is 2:

# In[ ]:

7%5


# And then we can evaluate the remaining operations in `1 + 2 - 32 + 2` from left to right, giving the final value of `-27`:

# In[ ]:

1 + 2 - 32 + 2


# <h3>Simple Math Functions</h3>
# 
# There are a number of simple math functions that are available in Python, and we'll show a few here to give you an idea.
# 
# You can get the absolute value with `abs()`:

# In[ ]:

abs(-3)


# You can round a floating point number to the nearest whole number using `round()`:

# In[ ]:

round(2.718281828)


# And you can use `max` and `min` to compute minimum and maximum values from a collection of values:

# In[ ]:

max(0, min(10, -1, 4, 3))


# This example is a little more involved, what's happening is that we have two parts.
# 
# The first is the minimum of 10, -1, 4 and 3:

# In[ ]:

min(10, -1, 4, 3)


# The second is the maximum of 0 and the result of the first part:

# In[ ]:

max(0, -1)


# which is 0, and that's the result.
# 
# <h3>Overwriting Functions (!)</h3>
# 
# One thing that may be surprising if you have worked with other languages is that these functions can be overridden.  The name `max`, for example, has nothing special about it---it's not a keyword---and the name can be bound to an integer or any other value:

# In[ ]:

# don't do this
max = 100


# So now we've done this `max` is an integer:

# In[ ]:

type(max)


# and if we try to call `max(4, 5)` we'll get a type error:

# In[ ]:

max(4, 5)


# because `max` is an integer now, not a function, and you can't call an integer.
# 
# In this case we can remove the local definition of `max` that is masking the built-in function by using the `del` statement:

# In[ ]:

del max


# If we check now, we'll see that `max` is back to being a function:

# In[ ]:

max(4, 5)


# <h3>Type Conversion</h3>
# 
# Python provides some functions for converting between types.
# 
# If you have a floating point number and want to cast it to an integer, use the `int()` function:

# In[ ]:

int(2.718281828)


# which always rounds towards 0.
# 
# If you have an integer and you want to create a float, you can cast it up using the `float()` function:

# In[ ]:

float(2)


# If you add an integer to a floating point number, or a floating point number to a complex number, Python always gives you the result as the widest type, so int plus float gives you float:

# In[ ]:

1 + 2.0


# <h3>Alternative Notations</h3>
# 
# There are some other ways of specifying numbers, and we'll show a few of the major ones here.
# 
# This is the floating point way of writing scientific notation:

# In[ ]:

6e3


# The others are less used, but convenient when you need them.  For integers, if you define a number with `0x` at the front, the value is treated as hexadecimal:

# In[ ]:

0xFF


# You can also use `0o` at the front to indicate octal (ie. base 8):

# In[ ]:

0o23


# You can instead just have a leading `0` and it will do the same thing, but this is not recommended because the meaning is very unclear and this behaviour can cause confusion for people who are new to Python:

# In[ ]:

023


# Finally `0b` at the front indicates a binary value:

# In[ ]:

0b1111


# <h3>In-Place Operations</h3>
# 
# In place versions of the standard arithmetic operations are possible using `+=`, `-=`, and so forth.  So for example:

# In[ ]:

b = 2.5
b += 0.5   # b = b + 0.5
b


# Boolean Data Type
# -----------------
# 
# Python has a boolean data type, which has two values, `True` and `False`.  So we could set:

# In[ ]:

q = True


# and see that the type of `q` is now `bool`:

# In[ ]:

type(q)


# Boolean values are most often created using expressions.  For example `1 < 0` is false, so if we do:

# In[ ]:

q = 1 < 0
q


# we see that `q` gets the value `False` as you might hope.
# 
# <h3>Comparison Operators</h3>
# Python's comparison operators are quite standard: `<`, `>`, `<=`, `>=`, `==` and `!=`.  So for example:

# In[ ]:

1 >= 2


# In[ ]:

1 + 1 == 2


# In[ ]:

2**3 != 3**2


# One really slick feature of Python's comparisons are chained comparisons:

# In[ ]:

1 < 10 < 100


# Effectively Python treats this expression as if it were:

# In[ ]:

1 < 10 and 10 < 100


# <h3>Logical Operations</h3>
# 
# Comparisons can be combined using the logical operators `and`, `or` and `not`.  So for example:

# In[ ]:

1 > 0 and 5 == 5


# Python uses ["short-circuit" evaluation](http://en.wikipedia.org/wiki/Short-circuit_evaluation) of logical expressions if the value of subsequent terms can't affect the result.  So for example, in the expression:

# In[ ]:

1 < 0 and max(0, 1, 2) > 1


# since the first operand is `False`:

# In[ ]:

1 < 0


# there is no way that the full expression could ever evalute to `True` and so Python skips the evaluation of the second operand, and returns `False` straight away.
# 
# Python's `or` operator works in a similar way:

# In[ ]:

a = 50
a < 10 or a > 90


# and it will short-circuit evaluation if the first operand is `True`:

# In[ ]:

a = 0
a < 10 or a > 90   # second term won't be evaluated


# And finally, the `not` operation inverts the value of the argument:

# In[ ]:

not 10 <= a <= 90


# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
