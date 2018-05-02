#读取整个文件
with open('pi_digits.txt') as file_object:
    #contents=file_object.read()
    #print(contents.rstrip())
    #for line in file_object:
    #    print(line.rstrip())
    #创建一个包含文件各行内容的列表
    lines=file_object.readlines()
    for line in lines:
        print(line.rstrip())
#写入文件
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love programming too.、")
#附加到文件
with open(filename,'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love programming too.")