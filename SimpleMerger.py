import os
import shutil
class SimpleMerger(object):

	def __init__(self, language):
		self.__language = language

	def merge(self):
		files = self.search_file_to_merge(os.curdir)
		if not os.path.exists("done"):
			os.mkdir("done")
		#map(lambda x: os.system(self.comand_generator(x)), filter(lambda x: x.endswith(".mkv"), files))
		map(lambda x: self.i_dont_delete_files(x), filter(lambda x: x.endswith(".mkv"), files))
		#self.delete_files(files)
		map(lambda x: os.rename(x, x.replace(".mkv666", ".mkv")), filter(lambda x: x.endswith(".mkv666"), os.listdir(os.curdir)))

	def comand_generator(self, filename):
		l_code = self.LANGUAGE_CODE[self.__language]
		return "mkvmerge -o "+filename+"666 "+filename+" --language 0:"+l_code+" --track-name 0:"+self.__language+" "+filename.replace("mkv", "srt")

	def search_file_to_merge(self, directory):
		"""this function exclude mkv without the equivalent srt file"""
		file_list = os.listdir(directory)
		t_list = map(lambda x: x.replace(".srt", ".mkv"), filter(lambda x: x.endswith(".srt"), file_list))
		return filter(lambda x: x in file_list, t_list)

	def i_dont_delete_files(self, mkv):
		os.system(self.comand_generator(mkv))
		shutil.move(mkv, "./done")
		shutil.move(mkv.replace(".mkv", ".srt"), "./done")



	def delete_files(self, list_of_files):
		"""this function delete the unnecessary files after the merging process"""
		print list_of_files
		map(lambda x: os.remove(x), list_of_files)
		map(lambda x: os.remove(x.replace(".mkv", ".srt")), list_of_files )
	
	LANGUAGE_CODE = {
		'Italian': 'ita',
		'English': 'eng'
		#add more language
	}

if __name__ == '__main__':
	sm = SimpleMerger("Italian")
	sm.merge()