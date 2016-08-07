import re
import glob

pattern = r'<[a-hj-zA-Z!\/].*?>'

def extract_one_doc(filename):
	with open("extracted_documents/" + filename.split(".")[0] + "-extracted.html", "w") as f_write:
		with open(filename, "r") as f_read:
			for line in f_read:
				line = re.sub(pattern, "", line)
				line = re.sub("<i>", "", line)
				if (line != '\n'):
					f_write.write(line)

if __name__ == "__main__":
	filenames = glob.glob("html/*")
	for name in filenames:
		extract_one_doc(name)
		print(name)