def quick_sort(list):
    if len(list)<1:
        return list
    else:
        pv=list[0]
        left_list= [i for i in list if i<pv]
        right_list=[i for i in list if i>pv]
        return quick_sort(left_list)+[pv]+quick_sort(right_list)



list=list(map(int,input().split()))
quick_sort(list)






