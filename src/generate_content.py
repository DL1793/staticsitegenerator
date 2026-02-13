import shutil
import os

#TODO: Delete public folder contents
def copy_static(src,dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
        os.mkdir(dst)
    else:
        os.mkdir(dst)
    recursive_copy(src,dst)

#TODO: Copy all contents of static to public
def recursive_copy(src,dst):
    for item in os.listdir(src):
        source_path = os.path.join(src, item)
        dest_path = os.path.join(dst, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dst)
        elif os.path.isdir(source_path):
            os.mkdir(dest_path)
            recursive_copy(source_path, dest_path)

#TODO: 