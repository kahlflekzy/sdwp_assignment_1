# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 07:40:51 2021

@author: Dalang, Felix Sihitshuwam
"""

def decorator1(func):
  """
    Create a function decorator that calculates function execution time and the
    number of times the decorated function was called (function call trace).
  """
  count = 0
  import time, contextlib, io
  def wrapper(*args, **kargs):
    """"""
    nonlocal count
    count += 1
    start = time.perf_counter()
    out = io.StringIO()
    with contextlib.redirect_stdout(io.StringIO()):
      func(*args, **kargs)
    c = out.getvalue()
    end = time.perf_counter()
    print(f"{func.__name__} call {count} executed in {end- start} sec")
  return wrapper