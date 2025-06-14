# MSCS532_Assignment4
#  Heapsort & Priority Queue Implementation

This project includes:
- **Heapsort**: An efficient in-place sorting algorithm using a binary max-heap.
- **Priority Queue**: A scheduler-friendly implementation using a binary min-heap for task management and simulation.

---

##  How to Run the Code

###  Prerequisites
- Python 3.7 or above
- No external libraries required

###  Run Sorting Benchmarks
To run and compare **Heapsort**, **Mergesort**, and **Quicksort**:

```bash
python heapsort.py

Summary of Findings

Heapsort
Consistently O(n log n) performance regardless of input distribution

In-place and memory-efficient, but slightly slower in practice due to poor cache performance

Best when memory is constrained

Mergesort
Also, O(n log n) in all cases

Performs well on all inputs

Stable, but uses extra space (O(n))

 Quicksort (with random pivot)
Fastest on average due to good cache usage

Worst-case O(n²) avoided using randomized pivot

Best general-purpose sort

 Priority Queue Implementation
Based on a binary min-heap (heapq)

Core operations implemented:

insert(task)

extract_min()

decrease_key(task_id, new_priority)

increase_key(task_id, new_priority)

is_empty()

Used for task scheduling based on priority and arrival time

Time Complexity Overview
Operation	Heapsort	Priority Queue
Insert	N/A	O(log n)
Extract Min/Max	O(log n)	O(log n)
Increase/Decrease Key	N/A	O(n) (due to Python's heapq limits)
Full Sort	O(n log n)	N/A
