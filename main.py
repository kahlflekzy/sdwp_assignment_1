# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 06:39:06 2021

@author: Dalang, Felix Sihitshuwam
"""

from task1 import decorator1
from task2 import decorator2
from task3 import Decorator as decorator3, rank
from task4 import Decorator as decorator4

@decorator1
def kahl():
  """
  Just a function that wastes time.

  Returns:
    None.
  """
  x = 0
  while True:
    state = lambda x: x == 10000
    if state: break
    x += 1
    

# ----------------------------------------------------------------------
@decorator1
def sum_(r: list):
    """
    Sum up items in the list r.
    
    This is part of a method I wrote for a class which performs matrix 
    calculations (dot products). It's useful for my DNLRS course.
    
    You can see some of the doctest below to understand how it works. 
    It basically sums up values in a  list. But there are some few perks, 
    particularly when the items in the list aren't all numbers, 
    it performs a peculiar addition.
    
    >>> Matrix.sum_(['c1', 1, 's1'])
    'c1+1+s1'
    >>> Matrix.sum_(['c1', 1, 's1', 0])
    'c1+1+s1'
    >>> Matrix.sum_([1, 1, 2, 2])
    6
    >>> Matrix.sum_([0, 1])
    1
    >>> Matrix.sum_([0, 0])
    0

    :param r:
    :return:
    """
    e = [str(i) for i in filter(lambda x: x != 0, r)]
    if not e:
        return 0
    to_sum = '+'.join(e)
    try:
        return eval(to_sum)
    except NameError:
        return to_sum

@decorator1
def quadratic_eqn(a: int, b: int, c: int=3) -> tuple:
  """
  Calculate the roots of a quadratic equation.
  
  Based on the coefficients of the terms of the equation. Returned value could
  be real values or complex values.

  Args:
    a (int): coefficient of x^2.
    b (int): coefficient of x.
    c (int, optional): constant term. Defaults to 3.

  Returns:
    tuple: tuple of (x1, x2) which may be a complex root.

  """
  import math
  
  det = b**2 - (4*a*c)
  
  if det > 0:
    d = math.sqrt(det)
    x1 = (-b + d)/(2*a)
    x2 = (-b -d)/(2*a)
  elif det == 0:
    x1 = x2 = -b/(2*a)
  else:
    r = -b/(2*a)
    i = -1 * det
    i = math.sqrt(i)/(2*a)
    x1 = complex(r, i)
    x2 = complex(r, -i)
  return x1, x2

@decorator1
def pascal(n: int):
  """
  Create and prints a pascal triangle based on my own algorithm.

  Args:
    n (int): Number of rows.

  Returns:
    None.

  """
  if n  < 0: 
      print(f"n ({n}) must be greater than or equal to zero")
      return
  out = [1]
  row = 0
  while row < n:
      row += 1
      out = [0] + out + [0]
      new = [0] * row
      j = 0
      while j < len(new):
          new[j] = out[j] + out[j+1]
          j += 1
      out = new
      print(out)

kahl()
kahl()
sum_([1, 2, 3, 4])
sum_(['a', 1, 'b', 2])
pascal(20)
pascal(20)
quadratic_eqn(1, 2, 3)
quadratic_eqn(1, 2, 3)

# only call below when testing decorator3, comment out otherwise
# rank()  