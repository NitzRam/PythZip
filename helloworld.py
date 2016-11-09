#!/usr/bin/python2

import os
import shutil

source_path = "/home/nithya/sorc" #Assigning path of the source folder
source_folder_content = os.listdir(source_path) #Assigning list of files and directories in source folder

for file in source_folder_content: #Prints the list of files and directories
	print file

destination_path = "/home/nithya/dest"  #Assigning path of the destination folder
destination_folder_content = os.listdir(destination_path)#Assigning list of files and directories in destination folder



sorted = []
list = []



def convert_bytes(num):#Function to convert bytes 
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if num < 1024.0:
			return "%3.1f %s" % (num, x)
		num /= 1024.0


def file_size(element):#Function to find size of file
	if os.path.isfile(element):
		file_info = os.stat(element)
		return file_info.st_size


file_list = []


m = 0
i = 0
new_size = 0
limit = 4000000
for file in source_folder_content:
	filename = os.path.join(source_path, file)#To obtain complete path
	if os.path.isfile(filename):
		file_list.append(filename)#Appending the file to the list file_list
		size = file_size(filename)
		print size
		new_size = new_size + size #Adding size of each file
		print "new_size:",new_size
		if new_size < limit: #If the total size is less than the limit copy the files to test+str(i) 
			new_path = destination_path + "/" + "test" + str(i)#Creating new path
			print new_path
			print "new new_size",new_size
			shutil.copy(filename, new_path)#To copy files
		if new_size > limit:#If the total size greater than limit reset new_size
		 	new_size=0;i = i + 1

