import os


def GetDiskUsage(pathname) :
	out = os.path.getsize(pathname);
	print(out);
	if(not os.path.isdir(pathname)) :
		return out;
	else :
		ls = os.listdir(pathname);
		print(ls);
		for ePath in ls :
			out += GetDiskUsage(pathname+'/'+ePath);
		return out;


tPath = '/Users/Ashment/Desktop/NYU/CS/CS1134'
print(GetDiskUsage(tPath));