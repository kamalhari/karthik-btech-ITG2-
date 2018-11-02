String=(input("Enter The String"))
StringToList=[]
CharOffset = 10
StringToList=String.split()
print(StringToList)
WordMap = {
		"I" : 1,
		"am" : 2,
		"a" : 1,
		"python" : 6,
		"programmer" : 10,
	}

print("Before comparig the vlaues")
print (WordMap)
check=False
check=String.isprintable()
print(check)
if check == True:
    header= [ WordMap.get(item ,item) for item in StringToList]
    print(header)
    #for i in header:
     #   if i.isalpha() == True :
      #      header.append(ord(i))
      #  else:
       #     pass
elif(check == False):
    my_new_list = [i * CharOffset for i in StringToList]
    print(my_new_list)
    S2="".join(my_new_list)
else:
     print("nothing")
print(header)
