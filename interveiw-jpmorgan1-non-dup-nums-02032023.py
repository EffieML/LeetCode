# input [2,2,[1,19],[9,19]]
# where [1, 9] means[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# output only print no return as 18, 10

def nonDupNums(arr):
    result = []
    duplicate_set = set()
    for elem in arr:
        if type(elem) == int:
            # str_elem = str(elem)
            # if len(str_elem) == len(set(str_elem)):
            result.append(0)
            # else:
            #     result.append(1)
        elif type(elem) == list:
            count = 0
            for i in range(elem[0], elem[1]+1):
                str_i = str(i)
                # if str_i in duplicate_set:
                #     continue
                if len(str_i) == len(set(str_i)):
                    count += 1
                # else:
                #     duplicate_set.add(str_i)
            result.append(count)
    return result


arr = [2, 2, [1, 19], [9, 19], [110, 119]]
print(nonDupNums(arr))
