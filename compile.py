#!/usr/bin/python
import subprocess
import os
import fnmatch
import sys
import shutil

def clean():
	print ("--- Summit Compilation Helper --- ")
	print ("Operation: Clean")
	if os.path.exists("./summit.bin"):
		os.remove("./summit.bin")

	if os.path.exists("obj") and os.path.isdir("obj"):
		shutil.rmtree("obj")

	print ("Clean: done.")

def build():
	print ("--- Summit Compilation Helper --- ")
	print ("Operation: Build")
	assembler = "i686-elf-as"
	cCompiler = "i686-elf-gcc"


	cFiles = []
	print("Updating list of C files.")
	for root, dirnames, filenames in os.walk("src"):
		for filename in fnmatch.filter(filenames, "*.c"):
			cFiles.append(os.path.join(root, filename))
			print("Adding C file ", filename, " to list of C files.")

	print("-----------------")
	asmFiles = []
	print("Updating list of assembly files.")
	for root, dirnames, filenames in os.walk("src"):
		for filename in fnmatch.filter(filenames, "*.S"):
			asmFiles.append(os.path.join(root, filename))
			print("Adding assembly file ", filename, " to list of assembly files.")

	print("-----------------")


	# Determine if all obj dirs are around
	print("Determining if nescessary object directories are present.")

	for cSourceFile in cFiles:
		if not os.path.exists(os.path.dirname(os.path.abspath(cSourceFile)).replace("src", "obj")):
			os.makedirs(os.path.dirname(os.path.abspath(cSourceFile)).replace("src", "obj"))
			print("Made directory ", os.path.dirname(os.path.abspath(cSourceFile)).replace("src", "obj"))

	for asmFile in cFiles:
		if not os.path.exists(os.path.dirname(os.path.abspath(cSourceFile)).replace("src", "obj")):
			os.makedirs(os.path.dirname(os.path.abspath(cSourceFile)).replace("src", "obj"))
			print("Made directory ", os.path.dirname(os.path.abspath(cSourceFile)).replace("src", "obj"))
	print("-----------------")


	print("Directories up-to-date.\nUpdating list of include directories.\n")

	cCompilerArguments = ["-std=gnu99", "-ffreestanding", "-O2"]

	for root, dirnames, filenames in os.walk("include"):
		for dirname in dirnames:
			cCompilerArguments.append("-I{0}".format(os.path.join(os.path.join(root, dirname))))
			cCompilerArguments.append("-I"+root)
			print("Added ", "-I{0}".format(os.path.join(os.path.join(root, dirname))), " to list of arguments.")

	print("Added -Iinclude to list of arguments.")


	print("Include directories done.")
	print("-----------------\nCompiling.")

	# Build all files

	for asmSourceFile in asmFiles:
		print("Assembling ", asmSourceFile, " to ", asmSourceFile.replace("src", "obj").replace(".S", ".o"))
		subprocess.call([assembler, asmSourceFile, "-o", asmSourceFile.replace("src", "obj").replace(".S", ".o")])

	for cSourceFile in cFiles:
		print("Compiling ", cSourceFile, " to ", cSourceFile.replace("src", "obj").replace(".c", ".o"))
		subprocess.call([cCompiler, "-c", cSourceFile, "-o", cSourceFile.replace("src", "obj").replace(".c", ".o")] + cCompilerArguments)
	print("Compilation finished.\n-----------------\nLinking kernel to summit.bin.\n")

	linkerParams = ["-T", "./linker.ld", "-o", "./summit.bin", "-ffreestanding", "-O2", "-nostdlib", "-lgcc"]

	print("Updating list of object files.")
	objectFiles = []
	for root, dirnames, filenames in os.walk("obj"):
		for filename in fnmatch.filter(filenames, "*.o"):
			print("Adding ", filename, " to object file list.")
			objectFiles.append(os.path.join(root, filename))



	for objectFile in objectFiles:
		linkerParams.append(objectFile)

	print("Invoking linker.\n-----------------")
	subprocess.call([cCompiler] + linkerParams)

	print ("Build: done.")

def pull():
	print ("--- Summit Compilation Helper --- ")
	print ("Operation: Pull")
	subprocess.call(["git", "pull", "origin", "master"])
	print ("Pull: done.")

def update():
	print ("--- Summit Compilation Helper --- ")
	print ("Operation: Update")

	clean()
	pull()

	build()

	print ("Update: done.")

if __name__ == "__main__":
	
	if sys.argv.__len__() > 1:
		for x in sys.argv[0:]:
			if x == "clean":
				clean()
			elif x == "build":
				build()
			elif x == "pull":
				pull()
			elif x == "update":
				update()
			elif x == "help":
				print("Valid options: \nclean : deletes object directories and object files \nbuild : builds the current source tree\npull: pulls the source tree from git\nupdate: cleans, updates and builds the source tree.\nstart-emu: starts the qemu-system-i386 emulator, if present in path.")
			elif x == "start-emu":
				print("Invoking emulator")
				subprocess.call(["qemu-system-i386", "-kernel", "summit.bin"])
	else:
		print("Usage: compile.py argument")
		print("Example usage:\n\tcompile.py help")
