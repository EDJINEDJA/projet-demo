initialize_git:
	@echo "git init .."
	git init
	sleep 1
	git add .
	sleep 1
	git commit -m "first commit"
	sleep 1
	git branch -M main
	sleep 1
	git remote add origin https://github.com/EDJINEDJA/projet-demo.git 
	sleep 1
	git push -u origin main

