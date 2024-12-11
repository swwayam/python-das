data = [10,20,50,3,223,10]
length = len(data)

# TC - O(N)

def find_e(arr, n):

    max = arr[0]

    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    
    return max

print(find_e(data, length))