def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    for item in range(len(items)-1,0,-1):
        for i in range(item):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items)>1:
        mid = len(items)//2
        left = items[:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k]=left[i]
                i=i+1
            else:
                items[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            items[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            items[k]=right[j]
            j=j+1
            k=k+1
        
        return items

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''

    def quick_sort_helper(items,first,last):
       if first<last:

           splitpoint = partition(items,first,last)

           quick_sort_helper(items,first,splitpoint-1)
           quick_sort_helper(items,splitpoint+1,last)


    def partition(items,first,last):
       pivotvalue = items[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and items[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while items[rightmark] >= pivotvalue and rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = items[leftmark]
               items[leftmark] = items[rightmark]
               items[rightmark] = temp

       temp = items[first]
       items[first] = items[rightmark]
       items[rightmark] = temp


       return rightmark
    
    quick_sort_helper(items,0,len(items)-1)
    return items