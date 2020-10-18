# Sorting Algorithms

This folder contains various sorting algorithms used in programming for sorting and arranging data.
Understanding and learning to implement these algo's is an important skill to have for a programmer.

All these sorting algorithm are written in such a way that they are east to 
grasp and understand for a beginner level programmer

## Files

<details>
<summary>1.<a href="https://github.com/Anjan50/Python/blob/main/Algorithms/Sorting%20Algorithms/InsertionSort.py">Insertion Sorting</a>
<br>
<b>Insertion Sort</b> is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.</summary>
<br>The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Algorithm

To sort an array of size n in ascending order:
<ol>
  <li> Iterate from arr[1] to arr[n] over the array. </li>
  <li> Compare the current element (key) to its predecessor.</li>
<li> If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.</li>
  </ol><br>

<img src="https://upload.wikimedia.org/wikipedia/commons/4/42/Insertion_sort.gif">

</details>

<details>
<summary>2.<a href="https://github.com/Anjan50/Python/blob/main/Algorithms/Sorting%20Algorithms/SelectionSort.py">Selection Sorting</a>
<br>
<b>Selection Sort</b> is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.</summary> <br>
The algorithm divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.
  
Algorithm
<blockquote>
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 
</blockquote>
<br>
<img src= "https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif" style="transform:rotate(-90deg)">
</details>
<details>
	<summary>
		3. <a href="https://github.com/Anjan50/Python/blob/main/Algorithms/Sorting%20Algorithms/BubbleSort.py">Bubble Sort</a>
		<br><b>Bubble Sort</b> is a simple sorting algorithm. This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order.
	</summary> <br>
	Bubble sort should be avoided in the case of large collections. It will not be efficient in the case of a reverse-ordered collection. 


<blockquote><br>
	
### Step-by-step example

Take an array of numbers " 5 1 4 2 8", and sort the array from lowest number to greatest number using bubble sort. In each step, elements written in bold are being compared. Three passes will be required;

First Pass 	<br>
    ( 5 1 4 2 8 ) → ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. <br>
    ( 1 5 4 2 8 ) → ( 1 4 5 2 8 ), Swap since 5 > 4 <br>
    ( 1 4 5 2 8 ) → ( 1 4 2 5 8 ), Swap since 5 > 2<br>
    ( 1 4 2 5 8 ) → ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.<br>
Second Pass<br>
    ( 1 4 2 5 8 ) → ( 1 4 2 5 8 )<br>
    ( 1 4 2 5 8 ) → ( 1 2 4 5 8 ), Swap since 4 > 2<br>
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )<br>
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )<br>

Now, the array is already sorted, but the algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.<br>

Third Pass<br>
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )<br>
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )<br>
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )<br>
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )<br>
</blockquote>
	<img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif">
</details>

<details>
  <summary>4.<a href="https://github.com/Anjan50/Python/blob/main/Algorithms/Sorting%20Algorithms/quicksort.py">Quick Sort</a> <br>
  <b>Quick Sort</b> is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
  There are many different versions of quickSort that pick pivot in different ways. </summary><br>
  The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct 
  position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.
  All this should be done in linear time.
  
  ### Algorithm
  
  <blockquote>
  <ol>
  <li>Always pick first element as pivot.</li>
  <li>Always pick last element as pivot (implemented below)</li>
  <li>Pick a random element as pivot.</li>
  <li>Pick median as pivot.</li>
  </ol>
  </blockquote>
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif">

</details>

<details>
<summary>
5.<a href="https://github.com/Anjan50/Python/blob/main/Algorithms/Sorting%20Algorithms/HeapSort.py"> Heap Sort</a> <br>
<b> Heap Sort</b>Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. 
We repeat the same process for the remaining elements.
</summary><br> Unlike selection sort, heapsort does not waste time with a linear-time scan of the unsorted region; rather, heap sort maintains the unsorted region in a heap data structure to more quickly find the largest element in each step.[1]



### Algorithm
<blockquote>
1. Build a max heap from the input data. <br>
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of the tree.<br>
3. Repeat step 2 while size of heap is greater than 1.<br>
</blockquote>
<img src = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif">
</details>

<details>
<summary>6.<a href = "https://github.com/Anjan50/Python/blob/main/Algorithms/Sorting%20Algorithms/MergeSort.py">Merge Sort</a><br>
<b>Merge Sort</b> is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. 
</summary><br> 
The merge() function is used for merging two halves.The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See following C implementation for details.

### Algorithm
<blockquote>
following C implementation for details.

MergeSort(arr[], l,  r) <br>
If r > l <br>
<ol>
     1. Find the middle point to divide the array into two halves:  <br>
             middle m = (l+r)/2 <br>
     2. Call mergeSort for first half:   <br>
             Call mergeSort(arr, l, m)<br>
     3. Call mergeSort for second half:<br>
             Call mergeSort(arr, m+1, r)<br>
     4. Merge the two halves sorted in step 2 and 3:<br>
             Call merge(arr, l, m, r)<br>
</blockquote>
<img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif">
</details>

<details>
<summary>
6. <a href ="https://github.com/aswnss-m/Python/blob/main/Algorithms/Sorting%20Algorithms/RadixSort.py">Radix Sort</a><br>
<b>Radix sort</b> is an integer sorting algorithm that sorts data with integer keys by grouping the keys by individual digits that share the same significant position and value (place value).
Radix sort uses counting sort as a subroutine to sort an array of numbers.
</summary><br>
Because integers can be used to represent strings (by hashing the strings to integers), radix sort works on data types other than just integers. Because radix sort is not comparison based, it is not bounded by \Omega(n \log n)Ω(nlogn) for running time — in fact,
radix sort can perform in linear time.

### Algorithm
<blockquote>
<ol>
<li>Find the largest element in the array, i.e. max. Let X be the number of digits in max. X is calculated because we have to go through all the significant places of all elements.<br>

In this array [121, 432, 564, 23, 1, 45, 788], we have the largest number 788. It has 3 digits. Therefore, the loop should go up to hundreds place (3 times).</li>
<li>Now, go through each significant place one by one.<br>

Use any stable sorting technique to sort the digits at each significant place. We have used counting sort for this.<br>

Sort the elements based on the unit place digits (X=0).</li>
<li>Now, sort the elements based on digits at tens place.</li>
<li>Finally, sort the elements based on the digits at hundreds place.</li>
</blockquote>
#### No Gif found 
<a href="http://www.algostructure.com/sorting/radixsort.php">Radix Sort Visual</a>
</details>








