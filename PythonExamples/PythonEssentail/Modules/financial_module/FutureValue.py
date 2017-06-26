#!/usr/bin/python

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

def future_value(r, n, pmt, pv=0.0, when=1):
    """Future value in "time value of money" equations.
    
    * r: interest rate per payment (decimal fraction)
    * n: number of payments
    * pv: present value
    * when: when payment is made, either 1 (begining of period, default) or
    0 (end of period)

    """
    return -pv*(1+r)**n - pmt*(1+r*when)/r * ((1+r)**n - 1)

import sys
pymts = float(raw_input("Insert number of pymts per year: "))
years = float(raw_input("Insert number years: "))
pymtmo = float(raw_input("Insert monthly payment: "))

#if len(sys.argv)>1:
#    print (float(sys.argv[1]))
#    pymts_pyear = float(sys.argv[1])

    # print " pymts pyear is : ",test
 
# pymts_pyear = float(sys.argv[1])

# Future Value Example.
yearly_rate = .0325
monthly_rate = yearly_rate / pymts # 12 pymts
monthly_periods = years * pymts  # 5 years
monthly_payment = pymtmo  # -$100 per period.

print "future value is ", future_value(monthly_rate, monthly_periods,
                                       monthly_payment)
