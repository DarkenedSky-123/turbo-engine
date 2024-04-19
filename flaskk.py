import os
FILE = 'file.txt'
gmail = "armx94522@gmail.com"
name = "DarkenedSky-123"
os.system(f"git config --global user.email {gmail}")
os.system(f"git config --global user.name {name}")
os.system(f'git add {FILE}')
os.system("git commit -m 'update file'")
