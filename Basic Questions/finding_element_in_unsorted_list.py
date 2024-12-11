data = [10,90,50]
length = len(data)

# TC - O(N)

def find_e(arr, value, n):
    
    for i in range(n):
        if arr[i] == value:
            return i
    
    return -1


print(find_e(data, 900, length))