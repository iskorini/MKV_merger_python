import os
class SimpleMerger(object):
	"""docstring for SimpleMerger"""
	def __init__(self):
		pass

	def merge(self):
		files = os.listdir(os.curdir)
		map(lambda x: os.system("mkvmerge -o "+x+"666 "+x+" --language 0:ita --track-name 0:Italian "+x.replace("mkv", "srt")), 
			filter(lambda x: x.endswith(".mkv"), files))
		files = os.listdir(os.curdir)
		map(lambda x: os.remove(x), filter(lambda x: x.endswith(".srt"), files))
		map(lambda x: os.remove(x), filter(lambda x: x.endswith(".mkv"), files))
		map(lambda x: os.rename(x, x.replace(".mkv666", ".mkv")), filter(lambda x: x.endswith(".mkv666"), files))



if __name__ == '__main__':
	sm = SimpleMerger()
	sm.merge()