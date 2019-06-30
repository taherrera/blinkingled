#!/usr/bin/env python

import os


class directory():
	def __init__(self, rootname):
		self.root = rootname
		self.subdirs = list()
		self.subdirs_names = list()
	
	def add_subdir(self,subdir_obj):
		self.subdirs.append(subdir_obj)

	def add_subdirnames(self, subdir_name):
		self.subdirs_names.append(subdir_name)


def traverse(root):
	listofdirs_raw = list()
	for rootdir, subdirs, files in os.walk(root):
		if "README.md" in files:
			listofdirs_raw.append(rootdir)
	
	listofdirs_ok= list()
	for d in listofdirs_raw:
		if "implementation" not in d:
			listofdirs_ok.append(d[2:])
	
	return listofdirs_ok


# asume node is part os subdirs
def create_hiarchy(node, subdirs):
	for d in subdirs:
		dl = d.split("/")
		new_dir = directory(dl[0])
		node.add_subdir(new_dir)
		if len(dl) >= 2:
			dl.pop(0)
			#print("/".join(dl))
			create_hiarchy(new_dir, ["/".join(dl)])

# asume node is part os subdirs
def create_hiarchy2(node, subdirs):
	sub = dict()
	for d in subdirs:
		dl = d.split("/")
		if dl[0] not in sub.keys():
			new_dir = directory(dl[0])
			sub.update({dl[0]:new_dir})
			node.add_subdir(new_dir)
		else:
			new_dir = sub[dl[0]]

		if len(dl) >= 2:
			
			dl.pop(0)
			
			new_dir.add_subdirnames("/".join(dl))

	for dir_obj in node.subdirs:
		create_hiarchy2(dir_obj, dir_obj.subdirs_names)

	
def create_html(rootnode):
	maindir = "https://github.com/taherrera/blinkingled/tree/master"
	with open("platforms.html", "w") as f:
		f.write("<ul>"+"\n")
		for a in rootnode.subdirs:
			f.write("\t<li>  <a href=" + maindir + "/" + a.root + ">" + a.root + "</a>" + "\n")
			f.write("\t<ul>"+"\n")
			for b in a.subdirs:
				f.write("\t\t<li> <a href=" + maindir + "/" + a.root + "/" + b.root + ">" + b.root + "</a>" + "\n")
				f.write("\t\t<ul>"+"\n")
				for c in b.subdirs:
					f.write("\t\t\t<li>  <a href=" + maindir + "/" + a.root + "/" + b.root + "/" + c.root + ">" + c.root + "</a>" + "\n")
					f.write("\t\t\t<ul>"+"\n")
					for d in c.subdirs:
						f.write("\t\t\t\t<li>  <a href=" + maindir + "/" + a.root + "/" + b.root + "/" + c.root + "/" + d.root + ">" + d.root + "</a>" +"\n")
					f.write("\t\t\t</ul>"+"\n")
				f.write("\t\t</ul>"+"\n")
			f.write("\t</ul>"+"\n")
		f.write("</ul>"+"\n")

		

if __name__ == "__main__":
	dirs = traverse(".")
	root = directory(".")
	create_hiarchy2(root,dirs)
	create_html(root)


