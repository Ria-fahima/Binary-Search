def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint]== target:
        return midpoint
    elif target > l[midpoint]:
        return binary_search(l, target, midpoint +1, high)
    else:
        return binary_search(l, target, low, midpoint-1)

if __name__ == "__main__":
    l= [1,3,6,9,10,11,12,13,14,15,16,17]
    target = 13
    print(binary_search(l,target))