def systolic_bubble_sort(arr):
    N = len(arr)
    # Repeat N-1 passes
    for _ in range(N - 1):
        # Each PE compares and swaps adjacent elements
        for i in range(N - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Test with a small array
if __name__ == "__main__":
    test_array = [5, 1, 4, 2, 8]
    print("Original array:", test_array)
    sorted_array = systolic_bubble_sort(test_array)
    print("Sorted array:", sorted_array)
