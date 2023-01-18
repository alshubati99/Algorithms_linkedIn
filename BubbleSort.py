def bubbleSort (dataset):
    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if dataset[j]> dataset [j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
    print("Current state: ", dataset)
def main():
    list1 = [6, 20, 9, 33, 89, 2, 4, 6, 7,98]
    bubbleSort(list1)
    print("Result: ", list1)
    
if __name__ == "__main__":
    main()