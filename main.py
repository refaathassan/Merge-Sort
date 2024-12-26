ls=[35,65,4,756,232,76,67,345,32,56]
def merge_fun(left,right):
    sorted_arr=[]
    i=j=0
    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
          sorted_arr.append(left[i])
          i+=1
        else: 
          sorted_arr.append(right[j])
          j+=1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge_fun(left,right)

arr=merge_sort(ls)
print(arr)
        