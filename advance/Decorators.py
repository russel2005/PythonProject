#first class fuction
def square(x):
  return x*x

f = square
print(square)//output: <function square at 0x101978950>
print(f(5))//output: 25

#Decorators
def outer_function():
  msg = 'Hi'
  
  def inner_function():
    print(msg)
  return inner_function()

outer_function() //output: Hi
  
  
