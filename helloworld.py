#!/usr/bin/python2

import os
import shutil

source_path = "/home/nithya/sorc"
source_folder_content = os.listdir(source_path)

for file in source_folder_content:
	print file

destination_path = "/home/nithya/dest"
destination_folder_content = os.listdir(destination_path)



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

