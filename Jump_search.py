'''
JUMP SEARCH ALGORITHM
applies to sorted array of numbers
the idea is to jump to pre-determined index thus avoiding unnecessary search
the optimum jump skips should be the square root of the len(array_of_numbers)
while jumping compare the jump_index element with the search_index,if it is less than go back to the previous jumpindex and perform a linearsearch
def jump_search(num_list,search_index,len(num_list)
'''
import math
def jump_search(num_list,search_index,length):
    #sort the array first
    num_list=sorted(num_list)
    prev_index=0
    jump=math.sqrt(length)
    jump=int(jump)

    #case when the list is empty
    while length == 0:
        return -1

    #case when the list has only one element
    while length == 1:
        if num_list[0] == search_index:
            return 0
        else:
            return -1

    #case for a lengthy list
    #the min() comes in handy when the jump exceeds the len(array) thereby the len(array) is used as the reference jump index
    while num_list[min(jump,length)] < search_index:
         prev_index=jump
         jump+=jump
    else:
         for prev_index in range(prev_index,jump,1):
             if num_list[prev_index] == search_index:
                 return prev_index

num_list=num_list_=[2]
search_index=search_index_=40
length=length_=len(num_list)

print(jump_search(num_list_,search_index_,length_))
