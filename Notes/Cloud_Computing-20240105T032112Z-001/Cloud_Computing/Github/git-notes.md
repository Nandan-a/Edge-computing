Read : 

https://kinsta.com/knowledgebase/what-is-github/

https://docs.github.com/en/get-started/quickstart

#Install git

sudo apt install git

The default repos can be set from :

https://github.com/settings/repositories

for example I have set it as master
-------------------------------------------------------

#Create a Repo on github

- Add a readme file
- add a lincese and then click on create repo
--------------------------------------------------------
#Create a local repo/dir on host machine

mkdir python-code

cd python-code
------------------------------------------------------
#intialize your local repo as git repo (local)

#before initialization

BHIoT$ git status
fatal: not a git repository (or any of the parent directories): .git

#after intiliazation

git init .

git status

#sample output

BHIoT$ git init .
Initialized empty Git repository in /home/bhupendra/cloud-diot-mar-22/sept-2022/Github/python-code/.git/
BHIoT$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)


#we will sync our local repo with remote repo

Remote repo have two files
1. LICENSE 
2. README.md

#One time step for setting up user name and user email

BHIoT$ git config --global user.name bhupendra592
BHIoT$ git config --global user.email bhupendra.jmd@gmail.com
BHIoT$ git config --list
user.name=bhupendra592
user.email=bhupendra.jmd@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
BHIoT$ 
-----------------------------------------------------------------------
Add repo URL to whom you are going to work

git remote add origin <remote repo>

git remote add origin https://github.com/bhupendra592/diotsept2022.git

BHIoT$ git config --list
user.name=bhupendra592
user.email=bhupendra.jmd@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=https://github.com/bhupendra592/diotsept2022.git


#check the branch in local

--> git branch

BHIoT$ git pull origin master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), 4.55 KiB | 931.00 KiB/s, done.
From https://github.com/bhupendra592/diotsept2022
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> origin/master
BHIoT$ ls
calculator.py  LICENSE  README.md

BHIoT$ git branch 
* master

----------------------------------------------------------
BHIoT$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        calculator.py

nothing added to commit but untracked files present (use "git add" to track)

#Add file to staging area

BHIoT$ git add calculator.py 
BHIoT$ git status 
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   calculator.py

BHIoT$ git log
commit 87d2e67060dda9d2552fd0a7ebbf2d775e184708 (HEAD -> master, origin/master)
Author: Bhupendra Pratap Singh <bhupendra.jmd@gmail.com>
Date:   Wed Jan 18 08:05:51 2023 +0530

    Initial commit

#commit the file

git commit -m "calculator application with add function" 

BHIoT$ git commit -m "calculator application with add function" 
[master 2533c75] calculator application with add function
 1 file changed, 5 insertions(+)
 create mode 100644 calculator.py
BHIoT$ git status
On branch master
nothing to commit, working tree clean
---------------------------------------------------------
BHIoT$ git log
commit 2533c755a4612eca6a85f2899883c141ff04d3b5 (HEAD -> master)
Author: bhupendra592 <bhupendra.jmd@gmail.com>
Date:   Wed Jan 18 14:31:53 2023 +0530

    calculator application with add function

commit 87d2e67060dda9d2552fd0a7ebbf2d775e184708 (origin/master)
Author: Bhupendra Pratap Singh <bhupendra.jmd@gmail.com>
Date:   Wed Jan 18 08:05:51 2023 +0530

    Initial commit

#create token
https://github.com/settings/tokens
settings -> developer settings -> Personal access token
token -> classic
generate new token (classic)

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

BHIoT$ git push origin master
Username for 'https://github.com': bhupendra592
Password for 'https://bhupendra592@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 392 bytes | 392.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/bhupendra592/diotsept2022.git
   87d2e67..2533c75  master -> master

-----------------------------------------------------------
Case:
when the changes being made in the file that has been pushed to
github


BHIoT$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   calculator.py

no changes added to commit (use "git add" and/or "git commit -a")

BHIoT$ git add calculator.py 

BHIoT$ git commit -m "added subtraction feature for two numbers"
[master 7de9a44] added subtraction feature for two numbers
 1 file changed, 6 insertions(+), 1 deletion(-)

BHIoT$ git push origin master
Username for 'https://github.com': bhupendra592
Password for 'https://bhupendra592@github.com': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 362 bytes | 362.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/bhupendra592/diotsept2022.git
   2533c75..7de9a44  master -> master

#How to create a new branch

git checkout -b feature-mul


BHIoT$ git checkout -b feature-mul
Switched to a new branch 'feature-mul'
BHIoT$ git branch 
* feature-mul
  master

BHIoT$ ls
calculator.py  LICENSE  README.md
BHIoT$ git status
On branch feature-mul
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   calculator.py

no changes added to commit (use "git add" and/or "git commit -a")

BHIoT$ git add .
BHIoT$ git commit -m "added Multiplication feature"
[feature-mul e968b85] added Multiplication feature
 1 file changed, 21 insertions(+), 1 deletion(-)
BHIoT$ git push
fatal: The current branch feature-mul has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin feature-mul

