# Sorts files into folders based on their last modification date; current_folder\year\month

import time
import os

curr_dir = os.getcwd()

def dir_exists(year, month):
  if not os.path.isdir(f'{curr_dir}\{year}\{month}'):
    try:
      os.mkdir(year)
    except FileExistsError:
      pass
    os.mkdir(f'{year}\{month}')

def get_formatted_date(filename):
  ti_m = os.path.getmtime(filename)
  m_ti = time.ctime(ti_m)
  t_obj = time.strptime(m_ti)
  return [str(t_obj[0]), f'{t_obj[1]:02}']

def main():
  print('Sorting...')
  for filename in os.scandir(curr_dir):
    if os.path.isdir(f'{curr_dir}\{filename.name}'): continue
    if filename.name == 'sort_by_date.py' or filename.name == 'sort_by_date.exe': continue
    year, month = get_formatted_date(filename)
    dir_exists(year, month)
    os.replace(f'{curr_dir}\{filename.name}', f'{year}\{month}\{filename.name}')
  print('Done!')
  input()

if __name__ == '__main__':
    main()