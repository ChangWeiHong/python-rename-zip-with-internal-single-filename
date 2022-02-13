from zipfile import ZipFile
import os

directory = os.getcwd()

for file in os.listdir(directory):
	zipname = os.fsdecode(file)
	if zipname.endswith(".zip"):
		with ZipFile(zipname, 'r') as f:
			names = [info.filename for info in f.infolist()]
			print("----")
			new_name_arr = []
			new_name = ""
			new_name_arr = names[0].split("/")
			new_name = new_name_arr[0] + '.zip'
			print(new_name)
			f.close()
			#fileName = names[0].replace('/','') + '.zip'
			try:
				os.rename(zipname, new_name)
			except:
				continue
			print(zipname+" Renamed to "+new_name+" Successfully") 
		continue