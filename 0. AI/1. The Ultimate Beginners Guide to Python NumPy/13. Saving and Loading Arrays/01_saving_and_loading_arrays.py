

import numpy as np

array_1 = np.array([0, 1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8, 9])

print("-------------save-----------------")
# save array into a binary file, end with .npy
# cannot the see the content
np.save(file = 'array_1_file', arr = array_1)

print("-------------load-----------------")
# to load the array content from file
array_1_loaded = np.load(file = 'array_1_file.npy')
print(array_1_loaded) # [0 1 2 3 4]


print("-------------savez-----------------")
# save more than 1 array in the same variable
np.savez('array_savez', array_1, array_2)

arrayz_loaded = np.load(file = 'array_savez.npz')
print(arrayz_loaded) # NpzFile 'array_savez.npz' with keys: arr_0, arr_1

# to access individual array by key
array1 = arrayz_loaded['arr_0']
array2 = arrayz_loaded['arr_1']
print(array1) # [0 1 2 3 4]
print(array2) # [5 6 7 8 9]

print("-------------savez_compressed-----------------")
# save multiple arrays in a file and compressed
# savez: 586 bytes
# savez_compressed: 413 bytes
np.savez_compressed('array_compressed', array_1, array_2)
array_com_loaded = np.load(file = 'array_compressed.npz')
print(array_com_loaded) # NpzFile 'array_compressed.npz' with keys: arr_0, arr_1

# to access individual array by key
array1 = array_com_loaded['arr_0']
array2 = array_com_loaded['arr_1']
print(array1) # [0 1 2 3 4]
print(array2) # [5 6 7 8 9]

print("-------------savetxt-----------------")
# save array in a txt format
array_2d = np.vstack([array_1, array_2])
'''
[[0 1 2 3 4]
 [5 6 7 8 9]]
'''
print(array_2d)
# values stored in scientific notation
np.savetxt(fname = 'array_csv.csv', X = array_2d)
# to keep the orginal format - string format
np.savetxt(fname = 'array_csv_fmt.csv', X = array_2d, fmt = '%s')
# set a delimiter - default empty space
np.savetxt(fname = 'array_csv_fmt_del.csv', X = array_2d, fmt = '%s', delimiter = ',')

print("-------------loadtxt-----------------")
array_csv_loaded = np.loadtxt(fname = 'array_csv.csv')
'''
[[0. 1. 2. 3. 4.]
 [5. 6. 7. 8. 9.]]
'''
print(array_csv_loaded)

'''
[[0 1 2 3 4]
 [5 6 7 8 9]]

 the array saved in csv, data was format to string, when load the file, convert the data type back
'''
array_csv_fmt_loaded = np.loadtxt(fname = 'array_csv_fmt.csv', dtype = int)
print(array_csv_fmt_loaded)

# ValueError: could not convert string '0,1,2,3,4' to int64 at row 0, column 1.
array_csv_fmt_del_loaded = np.loadtxt(fname = 'array_csv_fmt_del.csv', dtype = int, delimiter = ',')
print(array_csv_fmt_del_loaded)

'''
Other parameters:

    skiprows: number of rows to skip from the beginning of the file
    usecols: column indexes to load
    max_rows: maximum number of rows to load

'''