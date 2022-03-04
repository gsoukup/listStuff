import os
import glob


path=r"C:\Users\urbansamurai\Desktop\BaszatosZenek"
path2=r"C:\Users\urbansamurai\Desktop\MGMT"
listPath = os.listdir(path2)

print(listPath)


"""
for root, dirs, files in os.walk(path2):
    print(files)
"""
"""
for root, dirs, files in os.walk(path2):
    for f in files:
        print(os.path.join(root, f))
"""

g = glob.glob('*')
for f in g:
    print(os.path.join(path, f))

# Nem jo, a CWD nem stimme CURDIR
