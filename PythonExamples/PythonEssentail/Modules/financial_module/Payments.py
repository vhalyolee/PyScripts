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

def payment(r, n, pv, fv=0.0, when=0):
    """Payment in "time value of money" equations.

    Calculate the payment required to convert the present value into the future
    value.

    * r: interest rate per period (decimal fraction)
    * n: number of periods
    * pv: present value
    * fv: the amount that should be available after the final period.
    * when: when payment is made, either 1 (begining of period) or
      0 (end of period, default)

    """
    return -(fv + pv*(1+r)**n) * r / (1+r*when) / ((1+r)**n - 1)


# Loan Payment
yearly_rate = .065
monthly_rate = yearly_rate / 12
monthly_periods = 15 * 12  # 15 years
loan_amount = 300000
print "payment is ", payment(monthly_rate, monthly_periods, loan_amount)
