import shutil
import errno
def copy(src, dest):
    try:
        shutil.copytree(src, dest,ignore=shutil.ignore_patterns('node_modules')) #
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)



srcPath = "D://input_path_folder"
targetPath = "G://output_path_folder"


copy(srcPath,targetPath);
