import os

message = input("What is the commit message?\n> ")
branch = input("Master branch? Y/n\n> ").lower()

if branch == "n" or branch == "no":
    branch = "gh-pages"
else:
    branch = "master"

os.system("git pull")
os.system("git add .")
os.system(f"git commit -m \"{message}\"")
os.system(f"git push origin {branch}")
