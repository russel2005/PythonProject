# breakpoint() (Python 3.7+)
'''h: help, w: where, n: next, s: step
c: continue, p: print, l: list, q: quit
'''
# import pdb; pdb.set_trace()

def my_func():
  x = 5
  y = 6
  print(x+y)
  return x + y

a = int(0.1)
b = 1.0
c = a+b

breakpoint()

e = 0.1
f = 1.0
g = e+f

xy = my_func()

print('done')
