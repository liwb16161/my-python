try:
	f = open("hello.txt","r")
	f1 = open("hello1.txt","wb")
except FileNotFoundError:
	print("文件不存在")
else:

	s=f.read()

	print(s)

	# s.encode("utf-8")

	f1.write(s.encode("utf-8"))

	f.close()
	f1.close()