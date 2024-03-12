def main():
    n = 7
    arr = [1,5,8,15,8,25,9]
    for i in range(n):
        s = set()
        for j in range(n):
            if arr[j] < arr[i]:
                s.add(arr[j])
        rank = len(s) + 1
        print(rank, end=' ')

if __name__ == "__main__":
    main()
