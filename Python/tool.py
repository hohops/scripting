s=open("test.txt","w") #looks for the file if not created it creates it
s.write("this is a test\nWelcome to my page") #writes inside the file
s.close()
read_file=open("test.txt", "r").read() #cats the file
# print(read_file)




# ls1 = [1, 2, 3, 4]

#for i in ls1:
#  print(i)
a = input("what is your parameter?")

if a in read_file:
    print("It's in here")

else:
    print("Not founded")


# line = "I am Hoho"
# conv_list = line.split(" ")
# print(conv_list)