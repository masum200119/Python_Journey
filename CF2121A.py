t = int(input())  # number of test cases

for _ in range(t):
    nn, k = map(int, input().split())             # Read nn and k
    arr = list(map(int, input().split()))         # Read array elements in one line

    x = abs(arr[nn - 1] - k)
    y = abs(arr[0] - k)

    if nn == 1:
        print(abs(arr[0] - k))
    elif arr[nn - 1] < k and arr[0] < k:
        print(abs(arr[0] - k))
    elif arr[nn - 1] > k and arr[0] > k:
        print(abs(arr[nn - 1] - k))
    else:
        if x < y:
            print(2 * x + y)
        else:
            print(2 * y + x)
