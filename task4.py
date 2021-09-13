# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:39:35 2021

@author: Dalang, Felix Sihitshuwam
"""

class Decorator:
  res = []
  def __init__(self, func):
    """
    

    Args:
      func (function): Any function.

    Returns:
      None.

    """
    self.func = func
    self.count = 0
  def __call__(self, *args, **kargs):
    """
    Call function passed to constructor.
    
    Here we catch all errors (Exceptions) in a try and except block. We pass
    these to a log file named 'task_4_error_log.txt'.
    
    The outputs and results of function, with it's returned value and the
    functions descriptions are saved in a file named 'task_4_output.txt'

    Args:
      *args (tuple): All positional arguments.
      **kargs (dict): All keyword argument.

    Returns:
      None.

    """
    import time, io, contextlib, inspect, datetime
    self.count += 1
    func = self.func
    start = time.perf_counter()
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
      try:
        c0 = func(*args, **kargs)
      except Exception as e:
        with open('task_4_error_log.txt', 'a+') as file:
          file.write(f"{func.__name__}\n{e}\n{datetime.datetime.now()}\n\n")
        c0 = None
    c = f"{c0}\n{out.getvalue()}"
    end = time.perf_counter()
    elapsed = end - start
    out = f"""
{func.__name__} call {self.count} executed in {elapsed} sec
Name:   {func.__name__}
Type:   {type(func)}
Sign:   {inspect.signature(func)}
Args:   positional {args}
        key=worded {kargs}
Doc:    {inspect.getdoc(func)}

Source: {inspect.getsource(func)}

Output: {c}
    """
    with open('task_4_output.txt', 'w') as file:
      file.write(out)
    self.res.append((func.__name__, elapsed))
    return func

