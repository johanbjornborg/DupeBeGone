import os
from pathlib import Path
import re
import io
from collections import defaultdict

dupes = defaultdict(list)
norm = defaultdict(list)

for dirname, dirnames, filenames, in os.walk('.'):
    
    n = re.compile('.*[jpg|png]', re.IGNORECASE)
    p = re.compile('.*\([1-9]+\).*', re.IGNORECASE)
    q = re.compile('.*.ini', re.IGNORECASE)
    if "MellyDrive" in dirname:
##        for subdirname in dirnames:
##            print(os.path.join(dirname,subdirname))
        #    print path to all filenames.
        for filename in filenames:
            if q.match(filename):
##                print("Ignoring .ini file: ", filename)
                continue
            # If the file has (1) or something in it.
            if p.match(filename):
                dupes[filename] = os.path.join("D:" + os.sep, "Media", dirname[2:], filename)
            if n.match(filename):                
                norm[filename].append(os.path.join("D:" + os.sep, "Media", dirname[2:], filename))
                if len(norm[filename]) > 1:
                    dupes[filename] = norm[filename]

##print(type(dupes))
for f, v in dupes.items():
##    print(dupes[f])
##    print(f)
    count = 0
    for w in v:
        path = ""
        if count > 0:
            newstring = f[:-4] + " (" + str(count) + ")" + f[-4:]
            path = os.path.join("D:" + os.sep, "Media", "duplicates", newstring)
            if os.path.exists(path):
                print("path exists for: ", path)
                newstring = f[:-4] + " (" + str(3) + ")" + f[-4:]
                path = os.path.join("D:" + os.sep, "Media", "duplicates", newstring)
                
        else:
            path = os.path.join("D:" + os.sep, "Media", "duplicates", f)
            
        count += 1
        try:
            os.rename(w, path)
        except FileExistsError:
            print("path exists for: ", w)

        

##for f, v in norm:
##    print(norm[f])
##    print(os.path.join("D:" + os.sep, "Media", "duplicates", f))
##for f in norm:
##    print(norm[f])
    
##print(len(dupes.keys()))
##print(len(norm.keys()))
##    if x is "":
##        x = open(gp, 'r+')
##        data = x.read()
##        x.close()
##        print(data)
             


