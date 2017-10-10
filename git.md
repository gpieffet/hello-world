The first tutorial on using git (from the web page):

Creating a project (repository), creatign a branch, modifying a file, committing it, pull request, and merging:
	- https://guides.github.com/activities/hello-world/
	
Tutorial:
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

### Cloning
$ git clone https://github.com/gpieffet/hello-world.git git-clone-local-dir


### Managing files
$ git add git.md		#  to start tracking a file and stage it to be commited (if already tracked)
					# think of it as add content to be commited 
