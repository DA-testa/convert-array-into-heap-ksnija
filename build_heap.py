# python3
# 221RDC024, Ksenija Žuka

import os

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n // 2, -1, -1):
        swaps += sift_down(i, data)

    return swaps

def sift_down(i, data):
    swaps = []
    n = len(data)
    left = 2*i+1
    right = 2*i+2

    min = 1
    if left<n and data[left]<data[min]:
        min = left
    if right<n and data[range]<data[min]:
        min = right
    if i != min:
        swaps.append((i, min))
        data[i], data[min] = data[min], data[i]
        swaps += sift_down(min, data)

    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    txt = input()
    if "I" in txt:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in txt:
        fileName = input()
        path = './tests/'
        p = os.path.join(path, fileName)
        with open(p, mode = "r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4*len(data)
    print(len(swaps))

    # output all swaps
    for i, j in swaps:
        print(i, j)
    
    else:
        return

if __name__ == "__main__":
    main()

