# PythonProject
basic to advanced
## Find the python version
`$ python -V`  note: V should be CAPITAL

### Install pip
`$ python -m pip install --upgrade pip`

### Install python package
`$ sudo pip install wheel`

### Find the list of package
`$ pip list` | `$ pip freeze` | `$ pip show wheel` | `pip list --local`

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

### 5. create virtual env from python system packages which you already installed
`$ python -m venv venv --system-site-packages` --here 2nd venv is the virtual

### =========================

## Create new virtual environment `venv02` from existing another custom virtual environment `venv01`:
### 1. go and activate custom virtual env
`$ venv01/Scripts/activate`
### 2. create package list from current venv with version and put it in the .txt file
(venv01) {location of your virtual env} `$ pip freeze > requirements.txt` | `$ pip freeze --local > requirements.txt`
### 3. see the list from requirements.txt
`$ more requirements.txt`
### 4. move it into new venv02
`(venv01) {location of your virtual env} $deactivate` | 
`$ python -m venv venv02` | 
`$ venv02/Scripts/activate` |
`$ pip install -r requirements.txt`
### 5. now check all installed pacakes from old env to new env
`$ pip list`
### =========================

## Better way to create virtual environments in windows machine:
### 1. Install package 
`$ pip install virtualenvwrapper-win`

### 2. create centralize location or folder of all virtual env
`$ mkvirtualenv new-venv-name` or 
`$ mkvirtualenv regression -p c:\Python35\python.exe`

### 3. list all created virtual env
`$ workon` or `lsvirtualenv`
 
### 4. switch one environment to another env
`$ workon env-name`

## Delete the environment
`rmvirtualenv <name>` or 
`$ rmdir venv01 /s` -- here /s means subfolder will be deleted, you can also manually delete folder in windows.
`$ rm -rf env-name/`
## Open Command Prompt and enter `pip install virtualenv`
Download the desired python version (do NOT add to PATH!), and remember the path\to\new_python.exe of the newly installed version
To create a virtualenv, open Command Prompt and enter
`virtualenv \path\to\env -p path\to\new_python.exe`
If you are using PyCharm, update the Project Interpreter and the Code compatibility inspection.
To install packages:
(I) Activate virtualenv: open Command Prompt and enter `path\to\env\Scripts\activate.bat`
(II)  Install desired packages
(III)  Deactivate with `deactivate` .
