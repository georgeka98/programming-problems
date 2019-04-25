def insertion_sort(a, sort):
    result = a
    for i in range(len(result)):
        j = i - 1
        if sort == "acs":
            while j >= 0:
                if result[j+1] > result[j]:
                    swap = result[j]
                    result[j] = result[j+1]
                    result[j+1] = swap
                else:
                    break
                j = j - 1
        else:
            while j >= 0:
                if result[j+1] < result[j]:
                    swap = result[j]
                    result[j] = result[j+1]
                    result[j+1] = swap
                else:
                    break
                j = j - 1
    return result
                
print(insertion_sort([4,3,7,5,3,8,7,5,7,0,9,1,2], "desc"))
