def count_sort(array):
    max_element=max(array)
    count=[0]*(max_element+1)
    for element in array:
        count[element]+=1
    sorted_array=[]

    for i in range(len(count)):
        for j in range(count[i]):
            sorted_array.append(i)

    return sorted_array
array=[2,1,1,3,4,5]
print(count_sort(array))