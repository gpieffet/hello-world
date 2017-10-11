The first tutorial on using git (from the web page):

	- https://guides.github.com/activities/hello-world/ (Creating a project (repository), creatign a branch, modifying a file, committing it, pull request, and merging:)
	
**More Tutorial:**

	- http://rogerdudler.github.io/git-guide/

	- https://git-scm.com/book/id/v2/Getting-Started-First-Time-Git-Setup

	- https://github.com/GarageGames/Torque2D/wiki/Cloning-the-repo-and-working-with-Git

	

## Git Commands:
$ git --version
$ git verb --help
$ git config --list

### Configuration 
settings go to ~/.gitconfig 
$ git config --global user.name "name here"
$ git config --global user.email "email address here"
$ git config --global core.editor "Fav. editor here if different from default"


### Cloning or starting a local repository
$ git clone https://github.com/gpieffet/hello-world.git git-clone-local-dir
$ git init			# initialize a git repository
$ git remote add origin <server@>	# connect to a remote repos (with nick origin)


### Getting information
$ git status
$ git diff			# diff berween the the staging area and the working directory
$ git diff --staged	# diff berween the the staged files and the last commit
$ git log
$ git branch			# show existing branches
$ git remote [-v]		# list which remote servers are configured
=> a cloned repo. appears as "origin"
$ git remote add shortname [url]	# add new repository as shortname
$ git remote show origin			# informations about a particular remote repos


### Managing branches
$ git checkout -b branch1	# create a new branch and switch to it (a branch is just a pointer to a commit)
$ git checkout master		# go back to the master
$ git checkout branch1	# go back to branch1
$ git branch -d branch1	# delete the branch
$ git push origin branch1	# to make a branch available to others (so that they can make a pull)
$ git merge <branch>	# merge <branch> to the active branch
$ git push origin --delete branch1	# delete remote branch1


### Managing files
$ git add git.md		#  to start tracking a file and stage it to be commited (if already tracked)
					# think of it as add content to be commited 
$ git commit			# record the snapshot set up in the staging area
or $ git commit -m "Write the commit message"
$ git commit -a		# record all the tracked files without having to stage them before
$ git rm filename		# remove from staging area and delete from hard disk (durign the next commit)
$ git rm --cached file1# remove from staging and tracking (but keep it on hard disk) 
$ git mv file1 file2	# rename file1 to file2
$ git reset HEAD		# to unstage a file (but keep it tracked)
$ git checkout -- file1# to discard changes in file 1 and get it back as it was the first time around
$ git fetch origin		# get any new file that was done since it was cloned (or last fetched) but doesn't merge it
$ git pull			# fetches data from the server and tries to merge it
$ git push origin master	# push the changes to the server origin and the branch master   


### Files that you don't want to appear (in the status) even as untracked
=> Put them in .gitignore
and more with sublime text, and more and more
from a new branch

