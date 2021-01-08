# PythonProject
basic to advanced
## Find the python version
`$ python -V`  note: V should be CAPITAL

### Install pip
`$ python -m pip install --upgrade pip`

### Install python package
`$ sudo pip install wheel`

### Find the list of package
`$ pip list` , `$ pip show wheel`

### Uninstall package
`$ sudo pip uninstall wheel`

### activate/deactivate environment 
`$ source venv/bin/activate` | 
`$ deactivate`

### ========================= 
## virtual enviromnent setup:
### 1.create
`$ python -m venv my-test-venv-1` --it will create folder in the current location

### 2.activate
`$ my-test-venv-1/Scripts/activate`

### 3. install package into custom venv
`$ pip installl packagename`

### 4. deactivate
`$ deactivate`
### =========================

## Create new virtual environment `venv02` from existing another custom virtual environment `venv01`
### 1. go and activate custom virtual env
`$ venv01/Scripts/activate`
### 2. create package list from current venv with version and put it in the .txt file
(venv01) {location of your virtual env} `$ pip freeze > requirements.txt`
### 3. see the list from requirements.txt
`$ more requirements.txt`
### 4. move it into new venv02
`(venv01) {location of your virtual env} $deactivate`
`$ python -m venv venv02`
`$ venv02/Scripts/activate`
`$ pip install -r requirements.txt`
### 5. now check all installed pacakes from old env to new env
`$ pip list`
# Better way to create virtual environments in windows machine.
### 1. Install package 
`$ pip install virtualenvwrapper-win`

### 2. create centralize location or folder of all virtual env
`$ mkvirtualenv new-venv-name`

### 3. list all created virtual env
$ workon
 
### 4. switch one environment to another env
$ workon env-name



