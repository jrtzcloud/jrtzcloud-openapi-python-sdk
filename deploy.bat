@echo on
git.exe push --progress "origin" develop:develop
git.exe checkout master --
git.exe merge develop
git.exe push --progress "origin" master:master
git.exe checkout develop --
pause