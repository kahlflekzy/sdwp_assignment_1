# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:20:01 2021

@author: Dalang, Felix Sihitshuwam
"""

def decorator2(func):
  """
  Decorate passed function.
  
  Each function to be decorated should have a docstring, this original source 
  code of the function and others will be dumped to sys.out.
  
  """
  count = 0
  import time, inspect, contextlib, io
  def wrapper(*args, **kargs):
    """
    Wrap function with supplied arguments and perform decoration.

    Args:
      *args (TYPE): DESCRIPTION.
      **kargs (TYPE): DESCRIPTION.

    Returns:
      None.

    """
    nonlocal count
    count += 1
    start = time.perf_counter()
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
      c0 = func(*args, **kargs)
    c = f"{c0}\n{out.getvalue()}"
    end = time.perf_counter()
    out = f"""
{func.__name__} call {count} executed in {end- start} sec
Name:   {func.__name__}
Type:   {type(func)}
Sign:   {inspect.signature(func)}
Args:   positional {args}
        key=worded {kargs}
Doc:    {inspect.getdoc(func)}

Source: {inspect.getsource(func)}

Output: {c}
    """
    print(out)
  return wrapper