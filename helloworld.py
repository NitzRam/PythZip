#!/usr/bin/python2

import os
import shutil

source_path = "/home/nithya/sorc"
source_folder_content = os.listdir(source_path)

for file in source_folder_content:
	print file

destination_path = "/home/nithya/dest"
destination_folder_content = os.listdir(destination_path)


# for file in destination_folder_content:
# 	print file
sorted = []
list = []



def convert_bytes(num):
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if num < 1024.0:
			return "%3.1f %s" % (num, x)
		num /= 1024.0


def file_size(element):
	if os.path.isfile(element):
		file_info = os.stat(element)
		return file_info.st_size


file_list = []


m = 0
i = 0
new_size = 0
limit = 4000000
for file in source_folder_content:
	filename = os.path.join(source_path, file)
	if os.path.isfile(filename):
		file_list.append(filename)
		size = file_size(filename)
		print size
		new_size = new_size + size
		print "new_size:",new_size
		if new_size < limit:
			new_path = destination_path + "/" + "test" + str(i)
			print new_path
			print "new new_size",new_size
			shutil.copy(filename, new_path)
		if new_size > limit:
		 	new_size=0;i = i + 1

		# shutil.copy(filename, destination_path)
		# print file_size(source_path)
		# print "Copying Done!!"


		# file_info = os.stat(filename)
		# print file_info
		# size = os.path.getsize(filename) -- get size of file
		# size = file_info.st_size




	# 	list.append((size, file))
	# list.sort(key=lambda s: s[0])
	# for lists in list:
	# 	# print lists
	# 	sorted = lists




	# 	print "size:",size
	# 	new_size = new_size + size
	# print "new_size:",new_size
	# limit = 2000000
	# if new_size > limit * i and new_size < limit * (i + 1):
	# 	print "greater"
	# 	new_path = destination_path + "/" + "test" + str(i)
	# 	shutil.copy(filename, new_path)
	# 	i = i + 1
	# 	try:
	# 		os.mkdir(new_path, 0755)
	# 	except OSError as e:
	# 		raise
	# 	print "created"




	# m = convert_bytes(size)
	# print m




	

	# size=0
	# for file in sorted:
	# 		size+=os.path.getsize(file)
	# 		if size > 100000000:
	# 			print "greater"
	# 			for i in range(01, 50):
	# 				new_path = destination_path+"/"+"test"+i
	#    				os.makedirs(new_path)
	#     			print "created"





	# for file in source_folder_content:
	# 	filename = os.path.join(source_path,file)


	# for file in destination_folder_content:
	# 	print file


	# print "Destination folder is :%s"%sys.argv[2]
	# print "a = %d"%a
	# print "\nb = %d"%b
