#!/usr/bin/env python3

""" Module to test lab3.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from lab3 import days_in_month

MONTHS_WITH_31 = ["January", "March", "May", "July", "August", "October", "December"]
MONTHS_WITH_30 = ["April", "June", "September", "November"]
MONTHS_WITH_28_or_29 = ["February"]


def test_months_with_31():
    """
    Test months with 31 days
    """
    for item in MONTHS_WITH_31:
        assert days_in_month(item) == 31

# Write a test function for the months with 30 days

def test_months_with_30():
    """
    Test months with 30 days
    """
    for item in MONTHS_WITH_30:
        assert days_in_month(item) == 30
# Write a test function for the months with 28 or 29 days

def test_months_with_28_or_29():
    """
    Test months with 28 or 29 days
    """
    for item in MONTHS_WITH_28_or_29:
        assert days_in_month(item) == 28 or 29

# Write a test function for months that are not capitalized properly
# Hint: use the lower() string method

# Write a test function for unexpected input
# Hint: use a try/except block to deal with the exception
# Hint: use data types other than strings as input

def days_in_month_exception():
    try:
        item = MONTHS_WITH_28_OR_29 or MONTHS_WITH_30 or MONTHS_WITH_31
    except ValueError:
        Print ("Whoops")