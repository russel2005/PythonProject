
def square(x):
  return x*x

def my_map(func, arg_list):
  result = []
  for i in arg_list:
    result.append(func(i))
  return result

squares = my_map(square, [1,2,3,4,5])
print(squares)

#===========================
def logger(msg):
  
  def log_message():
    print('Log:', msg)
  return log_message

log_hi = logger('Hi!')
log_hi() //output: Log:Hi!
    

#----------------------------
def html_tag(tag):
  
  def wrap_txt(msg):
    print('<{0}>{1}</{0}>'.format(tag, msg)
  return wrap_txt
          
print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Test Headline!')

print_p = html_tag('p')
print_p('test paragraph!')
