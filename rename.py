import os

empty_dir = 'images/empty'
full_dir = 'images/full'

def rename_files(dir, new_name):
    count = 1
    for name in os.listdir(dir):
        f = os.path.join(dir, name)
        filename = new_name + str(count) + '.jpg'
        print(filename)
        new_path = os.path.join(dir, filename)
        if os.path.isfile(f):
            os.rename(f, new_path)
            count += 1

rename_files(empty_dir, 'empty')
rename_files(full_dir, 'full')