def linear_search(arr, target):
    """Return the index of target in arr or -1 if not found."""
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


if __name__ == "__main__":
    data = [5, 3, 7, 1, 9]
    print("linear_search(data,7) ->", linear_search(data, 7))
