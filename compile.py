#!/usr/bin/python
import subprocess
import os
import fnmatch

assembler = "i686-elf-as"
cCompiler = "i686-elf-gcc"

objDirs = ['./obj/i686/boot']

cFiles = []
for root, dirnames, filenames in os.walk('src'):
	for filename in fnmatch.filter(filenames, '*.c'):
		cFiles.append(os.path.join(root, filename))

asmFiles = []
for root, dirnames, filenames in os.walk('src'):
	for filename in fnmatch.filter(filenames, '*.S'):
		asmFiles.append(os.path.join(root, filename))

objectFiles = []
for root, dirnames, filenames in os.walk('obj'):
	for filename in fnmatch.filter(filenames, '*.o'):
		objectFiles.append(os.path.join(root, filename))

for x in objDirs:
	if not os.path.exists(x):	
		os.makedirs(x)



for asmSourceFile in asmFiles:
	subprocess.call([assembler, asmSourceFile, '-o', asmSourceFile.replace('src', './obj').replace('.S', '.o')])

for cSourceFile in cFiles:
	subprocess.call([cCompiler, '-c', cSourceFile, '-o', cSourceFile.replace('src', './obj').replace('.c', '.o'),
	 '-std=gnu99', '-ffreestanding', '-O2', '-Wall', '-Wextra'])


linkerParams = ['-T', './linker.ld', '-o', './summit.bin', '-ffreestanding', '-O2', '-nostdlib', '-lgcc']


for objectFile in objectFiles:
	linkerParams.append(objectFile)

subprocess.call([cCompiler] + linkerParams)