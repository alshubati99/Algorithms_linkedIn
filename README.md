## Algorithms_linkedIn_Course

# This is the linkedIn course: 
# Programming Foundations: Algorithms.
#### Excersises are all in python.  
------------------------------
### Algorhims Characteristics:
- Space and time complexity. 
- Input, output
- Classification: serial/ parallel, exact/ approximate, deterministic/non-deterministic
------------------------------
### Common Algorithms: 
- Search Algorithms
- Sorting Algorithms.
- Computational Algorithms.
- Collection algorithms. 
### Euclid's Algorithm: 
- Greatest Common Denominator (GCD) of two integers. 
== GCD of 20 and 8 = 4
- a > b divide a by b. 
- if remainder is 0 stop so GCD is b 
- otherwise set a to b and b to remainder and repeat until r is 0. 
----------------------------------
### measure how algorithm responds to dataset size: 
- Big-O notation:order of operation, usually describes worst case senaroi. 
### big-O terms: 
- O(1): constant time=> looking up a single element in an array. 
- O(log n): logarithmic=> finding item in a sorted array with binary search. 
- O(n): linear time=> searching an unsorted array for a specific value.  
- O(nlogn): log-linear=> heap sort and merge sort.  
- O(n^2): Quadratic=> not good like bubble sort, selection sort, insertion sort. 
---------------------------------
## Data Structures: 
- Used to organize data so it can be processed. 
### Common Data Structures:
- Arrays. 
- Linked lists.
- Stacks and queues. 
- Trees. 
- Hash Tables. 

### Arrays: 
- Collection of elements identified by index or key. 
- Claculate item index: O(1).
- Insert or delete item at beginning: O(n)
- Insert of delete item in middle: O(n).
- Insert or delete item at the end: O(1)

### linked Lists: 
- Collection of data elements called nodes. 
- Contains references to the next node in the list. 
- Hold whatever data the application needs. 
- Elements can be easily inserted and removed. 
- Underlying memory doesn't need to reorganized. 
- Can't do constant time random item access. 
- Item lookup is linear in time complexity O(n). 

### Stacks and Queues: 
- Collection of elemens supports push and pop operations. 
- The last item pushed is the first one popped. 
- Queues: supports adding and removing items. 
- First item added is the first time out. 

### Practical Applications for stacks and queues: 
- Expression processing => stack. 
- Backtracking => stack.
- Order processing => queue.
- Messaging => queue. 

### Hash Tables: 
- Assosaitive arrays. 
- Maps keys to thier assosaitive values.  
- Key to value mapping are unique. 
- Hash tables are typically very fast. 
- For small dataset, array are usually more efficient. 
- Hash tables don't enter enteries in predictible way. 
------------------------------------
### Recursion: 
- A function calls itself. 
- Recursive functions terminates using breaking conditions which prevents infinte calls. 
- Every time function is called, the previous step is saved. 

### Sorting Data: 
- Sorting is build-in in most modern languages. 
- Bubble sort.
- Merge sort.
- Quick sort. 

### Bubble Sort: 
- Simple to understand and implement. 
- Performance = O(n^2)
- Not a practical solution. 

### Merge Sort: 
- Divide and conquer algorithm.
- Uses recursion. 
- Performs well on large set of data. 
- Complexity of merge sort = O(nlogn).

### QuickSort: 
- Divide and conquer algorithm.
- Uses recursion to perform sorting. 
- Generally performs better than merge sort O(nlogn)
- Worst case is O(n^2) when data is mostly sorted already. 
- Selection of pivot point. 

### Linear Search and Binary Search. 
