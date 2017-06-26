"""
Financial Module
----------------

Background
~~~~~~~~~~

The future value (fv) of money is related to the present value (pv)
of money and any recurring payments (pmt) through the equation::

    fv + pv*(1+r)**n + pmt*(1+r*when)/r * ((1+r)**n - 1) = 0

or, when r == 0::

    fv + pv + pmt*n == 0

Both of these equations assume the convention that cash in-flows are
positive and cash out-flows are negative.  The additional variables in
these equations are:

* n: number of periods for recurring payments
* r: interest rate per period
* when: When payments are made:

  - (1) for beginning of the period
  - (0) for the end of the period

The interest calculations are made through the end of the
final period regardless of when payments are due.

"""


def present_value(r, n, pmt, fv=0.0, when=0):
    """Present value in "time value of money" equations.

    The present value of an annuity (or a one-time future value
    to be realized later)

    * r: interest rate per period (decimal fraction)
    * n: number of periods
    * pmt: the fixed payment per period
    * fv: the amount that should be available after the final period.
    * when: when payment is made, either 1 (begining of period) or
      0 (end of period, default)
    """
    return -(fv + pmt*(1+r*when)/r * ((1+r)**n - 1)) / (1+r)**n


# Present Value Example.
yearly_rate = .06
monthly_rate = yearly_rate / 12
monthly_periods = 10 * 12  # 10 years
monthly_income = 500
fv = 1000
pv = present_value(monthly_rate, monthly_periods, monthly_income,
                   fv=fv)
print "present value is ", pv

