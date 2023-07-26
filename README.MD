
git init

git pull https://github.com/again000/zkSyncTXs.git

<!-- python -m pip freeze > requirements.txt -->
python -m pip install -r requirements.txt

<!-- selects changes -->
git add .
<!-- records changes LOCALLY -->
git commit -m "new file" 
<!-- shares changes -->
git push

git push --set-upstream https://github.com/again000/zkSyncTXs.git master