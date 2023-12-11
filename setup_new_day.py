import os, shutil, fileinput
yearLabel = yearFolder = 'y'+input("Year:")
dayLabel = 'd'+"{:02d}".format(int(input("Day:")))

dayFolder = path = os.path.join(yearFolder, dayLabel)

os.mkdir(dayFolder)

with open(os.path.join(dayFolder, 'input.txt'), 'w') as tf:
    pass

shutil.copyfile(os.path.join('templates', 'p.py.template'), os.path.join(dayFolder, 'p1.py'))
shutil.copyfile(os.path.join('templates', 'p.py.template'), os.path.join(dayFolder, 'p2.py'))

launchFile = open(os.path.join(dayFolder, 'launch.py'), 'wt', encoding='utf-8')

for line in open(os.path.join('templates', 'launch.py.template'), 'r').readlines():
    launchFile.write(line.replace("{yearLabel}", yearLabel).replace("{dayLabel}", dayLabel))
