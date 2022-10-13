def BinarySearch_recursive(low,high,key):
    if len(num_list) == 0: #list is empty
        return -1
    while low <= high:
        mid=(low+high) //2
        if key == num_list[mid]:
            return mid
        elif key < num_list[mid]:
            return BinarySearch_recursive(low,mid-1,key)
        elif key > num_list[mid]:
            return BinarySearch_recursive(mid+1,high, key)
    else:
        return -1
#get user input and convert all to type(int)
user_input_str=input("Enter the list of numbers separated by a space:: ")
user_search_index=input('Enter the Value to search for, and the index will be returned..')
user_search_index=int(user_search_index)
user_input_list=user_input_str.split()
for index in range(len(user_input_list)):user_input_list[index] = int(user_input_list[index])
#create arguments to pass to the function
num_list=sorted(user_input_list)
keyholder,lowholder,highholder=int(),int(),int()
key=keyholder=user_search_index
len_list=len(num_list)
low=lowholder=0
high=highholder=len_list

print(f'The element {key} is in position - ',BinarySearch_recursive(lowholder,highholder,keyholder))
