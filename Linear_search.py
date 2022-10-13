'''

Code to implement linear search
List doesn't have to be sorted.
Get the list
find out the search index
starting from the left most loop through every value while checking,
if position found return the index
if position not found return -1
'''
def linear_search(input_list_int,search_index,len_list):

    for loop_index in range(len_list):
        if input_list_int[loop_index] == search_index:
            return loop_index

    return -1
#getting user input
input_string=input('Enter a list of numbers separated by a single space ::')
search_index= input('Which number do you wish to find::')
input_list=input_string.split()
for looping in range(len(input_list)):input_list[looping] = int(input_list[looping])
search_=search_index=int(search_index)
len_=len_list=len(input_list)

print(f'The position of element {search_} is = ',linear_search(input_list,search_,len_))
