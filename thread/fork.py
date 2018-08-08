#!/usr/local/bin/python3

import sys
import os
import time
import translog

log = translog.Log("DEBUG")
log.logname("fork.py")

path = os.getcwd()
filename = path + "/des1.txt"
filename0 = path + "/des2.txt"
print(filename0)
filename1 = path + "/des3.txt"


for i in range(2):
	pid = os.fork()

	if pid < 0:
		print("create process failed ")
	elif pid == 0:
		print("this is new process ",i)
		fp = open(filename, "r")
		size = os.path.getsize(filename)
		fp.seek(size/2*i)
		filenamea = 'filename' + '%s'%i
		print("aaaaa",filenamea)
		fp1 = open(filenamea,'a')
		lines = fp.read(int(size/2))
		fp1.write(lines)
		fp1.close()
		fp.close()
		log.TransLog("我是子进程，我执行完了")
		time.sleep(0.01)
		os._exit(0)

else:
	while True:
		print("this is parent process ")
		try:
			p,status = os.wait()
			print(os.WEXITSTATUS(status))
			print(p,status)
		except ChildProcessError as cpe:
			print(cpe)
			break
		try:
			sys.exit('game over')
		except SystemExit as e:
			print(e)
	os.system('cat filename0 filename1 >> filename2')
