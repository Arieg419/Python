#Implementatoin of basic sorting algorithms in Python
import random;
import heapq;

#Bubble Sort: best case O(n), average/worst case O(n^2)
def bubbleSort(nums):
	for i in range(len(nums)):
		for j in range(len(nums)-1-i):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j];
	return nums;

#Insertion Sort: best case O(n), average/worst case O(n^2)
def insertionSort(nums):
	for i in range(1, len(nums)):
		j = i;
		while j > 0 and nums[j] < nums[j-1]:
			nums[j], nums[j-1] = nums[j-1], nums[j];
			j -= 1;
	return nums;

#Merge Sort: bes/average/worst case O(n log n)
def mergeSort(nums):
	if len(nums) > 1:
		mid = int(len(nums) / 2); #midpoint
		leftArray = nums[0:mid];
		rightArray = nums[mid:];

		mergeSort(leftArray);
		mergeSort(rightArray);

		#merge sorted arrays back together
		left, right = 0, 0;
		for i in range(len(nums)):

			l = leftArray[left] if left < len(leftArray) else None;
			r = rightArray[right] if right < len(rightArray) else None;

			if (l and r and l < r) or r is None:
				nums[i] = l;
				left += 1;
			elif (l and r and l >= r) or l is None:
				nums[i] = r;
				right += 1;
	return nums;

#Quick Sort: best/average O(n log n), worst case O(n^2)
def quickSort(nums):
	if len(nums) > 1:
		pivot = int(len(nums) / 2);
		lessThan = [];
		greaterThan = [];

		for i, val in enumerate(nums):
			if i != pivot:
				if val < nums[pivot]:
					lessThan.append(val);
				else:
					greaterThan.append(val);
		quickSort(lessThan);
		quickSort(greaterThan);
		nums[:] = lessThan + [nums[pivot]] + greaterThan;
	return nums;

#Heap Sort: best/average/worst case O(n log n)
def heapSort(nums):
	heapq.heapify(nums);
	nums[:] = [heapq.heappop(nums) for i in range(len(nums))];
	return nums;

if __name__ == "__main__":
	numsToSort = [random.randint(-10, 10) for num in range(10)];
	
	print "Numbers to sort: " , numsToSort;
	numbersSorted = insertionSort(numsToSort);
	print "After Insertion Sort: " , numbersSorted;

	print "\nNumbers to sort: " , numsToSort;
	numbersSorted = bubbleSort(numsToSort);
	print "After Bubble Sort: " , numbersSorted;

	print "\nNumbers to sort: " , numsToSort;
	numbersSorted = mergeSort(numsToSort);
	print "After Merge Sort: " , numbersSorted;

	print "\nNumbers to sort: " , numsToSort;
	numbersSorted = quickSort(numsToSort);
	print "After Quick Sort: " , numbersSorted;

	print "\nNumbers to sort: " , numsToSort;
	numbersSorted = heapSort(numsToSort);
	print "After Heap Sort: " , numbersSorted;
