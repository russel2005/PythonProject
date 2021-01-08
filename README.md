# PythonProject
basic to advanced
## find the python version
$ python -V
# note V should be CAPITAL

# install pip
$ python -m pip install --upgrade pip

# install python package
$ sudo pip install wheel

# find the list of package
$ pip list
$ pip show wheel

# uninstall package
$ sudo pip uninstall wheel

# activate environment variable
$ source venv/bin/activate
$ deactivate

# iphthon will install all dependency
$ sudo pip install iphthon

============== virtual enviromnent setup ===============
#1.create
$ python -m venv my-test-venv-1
--it will create folder in the current location

#2.activate
$ my-test-venv-1/Scripts/activate

#3. install package into custom venv
$ pip installl packagename

#4. check all installed venv packagename
$pip list

#4. deactivate
$ deactivate
#========================================================

#create new virtual env venv02 from existing another custom virtual env venv01
#========================================================
#1. go and activate custom virtual env
$ venv01/Scripts/activate
#2. create package list from current venv with version and put it in the .txt file
(venv01) {location of your virtual env} $ pip freeze > requirements.txt
#3. see the list from requirements.txt
$ more requirements.txt
#4. move it into new venv02
(venv01) {location of your virtual env} $deactivate
$ python -m venv venv02
$ venv02/Scripts/activate
$ pip install -r requirements.txt
#5. now check all installed pacakes from old env to new env
$ pip list
#========================================================

$ pip install virtualenvwrapper-win

# create centralize location or folder of all virtual env
$ mkvirtualenv new-venv-name

# list all created virtual env
$ workon
 
# switch one environment to another env
$ workon env-name



