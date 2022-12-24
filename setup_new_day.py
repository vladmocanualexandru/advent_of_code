import os, shutil, fileinput

yearFolder = 'y'+input("Year:")
dayFolder = path = os.path.join(yearFolder, 'd'+"{:02d}".format(int(input("Day:"))))

os.mkdir(dayFolder)

shutil.copyfile(os.path.join('templates', 'input_template.txt'), os.path.join(dayFolder, 'input.txt'))
shutil.copyfile(os.path.join('templates', 'p1_template.py'), os.path.join(dayFolder, 'p1.py'))
shutil.copyfile(os.path.join('templates', 'p2_template.py'), os.path.join(dayFolder, 'p2.py'))