from PIL import Image
import os
import sys
from timeit import default_timer as timer


# Get all the file paths from the directory specified
def get_file_paths(dirname):
    file_paths = []  
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
    return file_paths





if __name__ == "__main__":
	count = 20 
	folder_name = sys.argv[1]
	file_paths = get_file_paths(folder_name)
	round_times = []
	for i in range(count):
		tic = timer()
		file_properties = []
		for file in file_paths:
			with Image.open(file) as img:
				width, height = img.size
			file_size = os.path.getsize(file)
			file_properties.append([str(file.split(os.sep)[-1]),(width, height), file_size])
		toc = timer() -tic
		print("Time needed for round {} is {}".format(i, toc))
		round_times.append(toc)
	#print(file_properties)
	print(round_times)
