list_1 = [4,2,7,9,12,3]
find_num = int(input())
found_num = False

for each_num in list_1:
    if(each_num == find_num):
        found_num = True
    

if(found_num == True):
    print("the number is present in the list")

else:
    print("the number is not present in the lisy")    