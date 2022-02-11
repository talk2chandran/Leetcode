


def merge(left,right):
    res=[]

    lidx=0
    ridx=0

    while len(res)< len(left) + len(right):
        if left[lidx]>=right[ridx]:
            res.append(right[ridx])
            ridx+=1
        elif right[ridx]>= left[lidx]:
            res.append(left[lidx])
            lidx+=1

        if lidx == len(left):
            res.extend(right[ridx:])
            break
        if ridx == len(right):
            res.extend(left[lidx:])
            break
    print(f" inside -> {res}")
    return res

def merge_sort(l):

    #base condition
    if len(l)<=1:
        return l

    mid=len(l)//2
    print(f"{l[:mid]}   {l[mid:]}")
    return merge(merge_sort (l[:mid]),
            merge_sort (l[mid:]))


ul=[9,7,1,5,2,8]

sl=merge_sort(ul)

print(f"unsorted list is {ul}")

print(f"sorted list is {sl}")
