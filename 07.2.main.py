# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

class Folder:
    size = 0
    parent = []
    path = ''
    subFolders = ()
    def __init__(self, parent, name):
        self.parent = parent
        if (name == '/'):
            self.path = '/'
        else:
            self.path = parent.path + name + '/'
    def addFile(self, size):
        self.size += size
        if (not self.parent == []):
            self.parent.addFile(size)
    def addSubFolder(self, name):
        subFolder = Folder(self, name)
        self.subFolders += (subFolder, )
        return subFolder
    def getAnswer1(self):
        if (self.size < 100000):
            answer = self.size
        else:
            answer = 0
        for subFolder in self.subFolders:
            answer += subFolder.getAnswer1()
        return answer
    def getAnswer2(self, neededSpace, bestGuess):
        if (self.size > neededSpace):
            if (self.size < bestGuess):
                bestGuess = self.size
            for subFolder in self.subFolders:
                bestGuess = subFolder.getAnswer2(neededSpace, bestGuess)
        return bestGuess
    def dump(self):
        print(self.size)
        for subFolder in self.subFolders:
            subFolder.dump()

with open('07.input.txt', 'r') as file:
    for line in file:
        if (line[0 : 5] == '$ cd '):
            folderName = line[5 : -1]
            if (folderName == '/'):
                root = Folder([], '/')
                currentFolder = root
            else:
                if (folderName == '..'):
                    currentFolder = currentFolder.parent
                else:
                    currentFolder = currentFolder.addSubFolder(folderName)
        else:
            if (not line == '$ ls\n' and not line[0 : 4] == 'dir '):
                currentFolder.addFile(int(line.split(' ')[0]))
print(root.getAnswer1())
neededSpace = root.size - 40000000
print(root.getAnswer2(neededSpace, root.size))
#print(root.dump())
