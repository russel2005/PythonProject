
########try and except ############

try:
	f = open('testfile.txt')
	val = bad_val
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
#########try except else and finally block###########
try:
	f = open('testfile.txt')
except FileNotFoundError:
	print('Sorry ! file not exist.')
except Exception:
	print('Sorry. something went wrong')
	
else:
	print('it raise/execute if try block not catch anything
finally:
	pass

#################
try:
	f = open('testfile.txt')
	val = bad_val
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print("else block only run when we don't have an exception")
	print(f.read())
	f.close()
finally:
	#print('always this block run')
	print('Executing finally...')

########### catch multiple exceptions in one block
except (RuntimeError, TypeError, NameError):
    pass
################# Manually raise an exception
try:
	f = open('currupt_file.txt')
	if f.name == 'currupt_file.txt':
		raise Exception 
except FileNotFoundError as e:
	print(e)
	# or raise exception in except block to handle this exception into another method when call
	raise Exception("This is another raise exception")
except Exception as e:
	print(e)
else:
	print('else block only run when we don't have an exception')
	print(f.read())
	f.close()
finally:
	#print('always this block run')
	print('Executing finally...')
