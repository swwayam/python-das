data = [10,40,60,1]
length = len(data)

# TC - O(N)

def is_sorted(arr, n):

    for i in range(n):

        if i + 1 == n:
            return True
        
        if arr[i] > arr[i + 1]:
            return False

print(is_sorted(data, length))