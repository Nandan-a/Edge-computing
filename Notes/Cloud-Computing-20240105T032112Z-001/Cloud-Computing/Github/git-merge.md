How to merge two branches

Use Case :

main branch - master (where changes to be merged)

feature branch ->  feature-mul

git branch 

BHIoT$ git branch 
* feature-mul
 master

BHIoT$ git status 
On branch feature-mul
Your branch is up to date with 'origin/feature-mul'.

nothing to commit, working tree clean
BHIoT$ git branch 
* feature-mul
  master

Content in calculator.py
-------------------------------
BHIoT$ cat calculator.py 
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

res_add = add(10,20)
print(res_add)
res_sub = sub(20,10)
print(res_sub)
res_mul = sub(20,10)
print(res_mul)
--------------------------------
BHIoT$ git checkout master
Switched to branch 'master'
--------------------------------
BHIoT$ cat calculator.py 
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

res_add = add(10,20)
print(res_add)
res_sub = sub(20,10)
print(res_sub)
-----------------------------------------
#Merging feature into master
------------------------------------------
BHIoT$ git merge feature-mul 
Updating 7de9a44..7e4a8e7
Fast-forward
 calculator.py | 7 ++++++-
 1 file changed, 6 insertions(+), 1 deletion(-)
-----------------------------------------------------
BHIoT$ cat calculator.py 
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

res_add = add(10,20)
print(res_add)
res_sub = sub(20,10)
print(res_sub)
res_mul = sub(20,10)
print(res_mul)
-------------------------------------------------------

#Clonning:

git clone <repo URL>

https://github.com/bhupendra592/Socket-Programming

#git stash

HIoT$ git checkout feature-div 
Switched to branch 'feature-div'
BHIoT$ git status
On branch feature-div
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   calculator.py

no changes added to commit (use "git add" and/or "git commit -a")
BHIoT$ git checkout feature-mul 
error: Your local changes to the following files would be overwritten by checkout:
	calculator.py
Please commit your changes or stash them before you switch branches.
Aborting
BHIoT$ git stash
Saved working directory and index state WIP on feature-div: 831888e added division feature
BHIoT$ git status
On branch feature-div
nothing to commit, working tree clean
BHIoT$ git branch feature-mul 
fatal: A branch named 'feature-mul' already exists.
BHIoT$ git checkout  feature-mul 
Switched to branch 'feature-mul'
Your branch is up to date with 'origin/feature-mul'.
BHIoT$ git checkout feature-div 
Switched to branch 'feature-div'
BHIoT$ git stash apply 
On branch feature-div
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   calculator.py

no changes added to commit (use "git add" and/or "git commit -a")
BHIoT$ git stash
Saved working directory and index state WIP on feature-div: 831888e added division feature

BHIoT$ git branch 
* feature-div
  feature-mul
  master
BHIoT$ git checkout -b test_branch
Switched to a new branch 'test_branch'
BHIoT$ git status
On branch test_branch
nothing to commit, working tree clean
BHIoT$ ls
calculator.py  LICENSE  README.md
BHIoT$ git branch --delete test_branch 
error: Cannot delete branch 'test_branch' checked out at '/home/bhupendra/cloud-diot-mar-22/sept-2022/Github/python-code'
BHIoT$ git checkout master
Switched to branch 'master'
BHIoT$ git branch --delete test_branch 
Deleted branch test_branch (was 831888e).

--------------------------------------------------------------
BHIoT$ git branch 
* feature-div
  feature-mul
  master
BHIoT$ git checkout -b test_branch
Switched to a new branch 'test_branch'
BHIoT$ git status
On branch test_branch
nothing to commit, working tree clean
BHIoT$ ls
calculator.py  LICENSE  README.md
BHIoT$ git branch --delete test_branch 
error: Cannot delete branch 'test_branch' checked out at '/home/bhupendra/cloud-diot-mar-22/sept-2022/Github/python-code'
BHIoT$ git checkout master
Switched to branch 'master'
BHIoT$ git branch --delete test_branch 
Deleted branch test_branch (was 831888e).
