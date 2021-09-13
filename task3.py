# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 06:43:50 2021

@author: Dalang, Felix Sihitshuwam
"""


class Decorator:
  """"""
  res = []
  def __init__(self, func):
    """
    Initialise.

    Args:
      func (function): Any function.

    Returns:
      None.

    """
    self.func = func
    self.count = 0
  def __call__(self, *args, **kargs):
    """
    Call function and perform decoration task.
    
    In this virtual method, we pass all output to a file in the current 
    working directory. The file is named 'task_3_output.txt'
    
    The contents written to the file includes the decorations performed on the 
    function. And the output of the function, 
    including results returned by the function and outputs which the function
    sends to stdout (prints).

    Args:
      *args (tuple): All positional arguments.
      **kargs (dict): All keyword argument.

    Returns:
      None.

    """
    import time, io, contextlib, inspect
    self.count += 1
    func = self.func
    start = time.perf_counter()
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
      c0 = func(*args, **kargs)
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
    with open('task_3_output.txt', 'w') as file:
      file.write(out)
    self.res.append((func.__name__, elapsed))
    return func


def rank():
  """
  Rank the functions that have so far been executed.
  
  From fastest to slowest

  Returns:
    None.

  """
  a = len('PROGRAM  ')
  max_str = max([len(i[0]) for i in Decorator.res])
  if max_str < a:
    max_str = a
  print(f"{'PROGRAM  '.ljust(max_str)} | RANK | TIME ELASPED")
  for i, j in enumerate(sorted(Decorator.res, key=lambda x: x[1])):
    f = f"{j[0].ljust(max_str)}"
    print(f, ' ', i+1, '\t ', j[1])