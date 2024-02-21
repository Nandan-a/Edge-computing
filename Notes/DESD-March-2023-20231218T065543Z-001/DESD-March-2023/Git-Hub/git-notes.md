BHIoT$ git init .
Initialized empty Git repository in /home/bhupendra/DESD-IoT/git-python/.git/

BHIoT$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)

----------------------------------------------------------------------
BHIoT$ git config --global user.name bhupendra592
BHIoT$ git config --global user.email bhupendra.jmd@gmail.com
BHIoT$ git config --list
user.name=bhupendra592
user.email=bhupendra.jmd@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true

------------------------------------------------------------------------

BHIoT$ git pull https://github.com/bhupendra592/desd-python.git
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), 4.50 KiB | 1.13 MiB/s, done.
From https://github.com/bhupendra592/desd-python
 * branch            HEAD       -> FETCH_HEAD
-------------------------------------------------------------------------
BHIoT$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Helloworld.py

nothing added to commit but untracked files present (use "git add" to track)

BHIoT$ git add Helloworld.py 
BHIoT$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   Helloworld.py
------------------------------------------------------------------------------
BHIoT$ git commit -m "Adding the fresh python program with basic req"
[master fb3892b] Adding the fresh python program with basic req
 1 file changed, 1 insertion(+)
 create mode 100644 Helloworld.py
--------------------------------------------------------------------------------
BHIoT$ git branch
* master
---------------------

#Add Remote URL:

git remote add origin https://github.com/bhupendra592/desd-python.git

----------------------------------------------------------------------------
BHIoT$ git remote -v
origin	https://github.com/bhupendra592/desd-python.git (fetch)
origin	https://github.com/bhupendra592/desd-python.git (push)

#create a Branch main

git checkout -b main
#Token Value
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
-----------------------------------------------------------------------------
BHIoT$ git push -u origin main
Username for 'https://github.com': bhupendra592
Password for 'https://bhupendra592@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 376 bytes | 376.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/bhupendra592/desd-python.git
   2ec5605..fb3892b  main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
------------------------------------------------------------------------------





