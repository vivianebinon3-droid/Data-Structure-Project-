# arrays_and_search.py
# In Python, lists are used to represent arrays

def linear_search(arr, key):
    for index in range(len(arr)):
        if arr[index] == key:
            return index
    return -1


def main():
    scores = [68, 74, 82, 90, 77]

    print("Scores:", scores)

    result = linear_search(scores, 82)

    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")


if __name__ == "__main__":
    main()
