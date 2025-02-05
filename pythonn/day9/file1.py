file =open("pythonn/day9/filee.txt","r")
content=file.read()
print(content)
file1=open("pythonn/day9/file1.txt","w")
file1.write("delhi \nmumbai \npune \nbengaluru ")
for line in file:
    print(line.strip())
    
file1=open("pythonn/day9/file1.txt","a")
file1.write("\n1delhi \n2mumbai \n3pune \n4bengaluru ")
for linee in file:
    print(linee.strip())

file.close()
file1.close()
