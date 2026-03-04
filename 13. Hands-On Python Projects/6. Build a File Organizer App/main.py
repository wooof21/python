

import os


# rename all jpg files to be the format of `photo-0.jpg` ...
# move all jpg files to a folder `images`
# keep other files
def arrange_files(files, ext):
    # list comprehension: 
    #   1. Loops over each file in files
    #   2. Checks: file.endswith(ext)
    #   3. Keeps only the filenames that end with the given extension
    #   4. Stores them in files_with_ext
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)

    if not(os.path.exists("images")):
        os.mkdir("images")

    '''
    enumerate(): is a built-in Python function that lets you loop over items AND their index at the same time.

    e.g:
        files_with_ext = ["a.jpg", "b.jpg", "c.jpg"]

        enumerate(files_with_ext) produce:
            (0, "a.jpg")
            (1, "b.jpg")
            (2, "c.jpg")

    equivalent to:

        i = 1
        for file in files_with_ext:
            os.rename(file, f"photo-{i}{ext}")
            i+=1 
    '''
    for i, file in enumerate(files_with_ext):
        os.rename(file, f"images/photo-{i}{ext}")

# gatekeeper of Python programs:
# the Python file build-in variable `__name__`, the value depends on `how the file is used`
#   1. Run file (program) directly: `__name__ == __main__`
#   2. import the file inside another file (app.py): `__name__ == app`
# the gatekeeper: ensure the code is only running if executed directly, not if it's improted
#   1. prevent the side effect of import: without it, every import will also run the program
#   2. with it, import will not run the code unless explict call it
if __name__== "__main__":
    files = os.listdir()
    arrange_files(files, ".jpg")