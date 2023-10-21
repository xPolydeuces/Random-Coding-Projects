# Sorts files into folders based on their extension; current_folder\extension

import os

curr_dir = os.getcwd()

def dir_exists(ext):
  if not os.path.isdir(f'{curr_dir}\{ext}'):
    os.mkdir(ext)

def main():
  print('Sorting...')
  for filename in os.scandir(curr_dir):
    if os.path.isdir(f'{curr_dir}\{filename.name}'): continue
    ext = os.path.splitext(filename)[1]
    if ext == '.py': continue
    dir_exists(ext)
    os.replace(f'{curr_dir}\{filename.name}', f'{ext}\{filename.name}')
  print('Done!')
  input()

if __name__ == '__main__':
    main()