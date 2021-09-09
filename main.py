# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 06:39:06 2021

@author: Dalang, Felix Sihitshuwam
"""

from task1 import decorator1
from task2 import decorator2
from task3 import Decorator as decorator3, rank

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
    


@decorator3
def quadratic_eqn(a: int, b: int, c: int=3) -> tuple:
  """
  Calculate the roots of a quadratic equation.
  
  Based on the coefficients of the terms of the equation.

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

@decorator3
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

pascal(20)
pascal(20)
quadratic_eqn(1, 2, 3)
quadratic_eqn(1, 2, 3)
rank()  # only call this when testing decorator3, comment out otherwise