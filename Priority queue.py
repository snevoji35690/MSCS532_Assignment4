import heapq

# Task class to hold task information
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # Lower priority value means higher importance (min-heap)
        return self.priority < other.priority

    def __repr__(self):
        return (f"Task(ID={self.task_id}, Priority={self.priority}, "
                f"Arrival={self.arrival_time}, Deadline={self.deadline})")


# Priority Queue class using a binary heap (min-heap)
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.task_map = {}  # Helps with updating existing tasks by ID

    def insert(self, task):
        heapq.heappush(self.heap, task)
        self.task_map[task.task_id] = task  # Track task by ID
        # O(log n)

    def extract_min(self):
        if self.is_empty():
            return None
        task = heapq.heappop(self.heap)
        self.task_map.pop(task.task_id, None)
        return task
        # O(log n)

    def is_empty(self):
        return len(self.heap) == 0
        # O(1)

    def decrease_key(self, task_id, new_priority):
        if task_id not in self.task_map:
            return False
        task = self.task_map[task_id]
        if new_priority >= task.priority:
            return False  # Not a decrease

        self.heap.remove(task)          # O(n)
        heapq.heapify(self.heap)        # O(n)
        task.priority = new_priority
        heapq.heappush(self.heap, task) # O(log n)
        return True

    def increase_key(self, task_id, new_priority):
        if task_id not in self.task_map:
            return False
        task = self.task_map[task_id]
        if new_priority <= task.priority:
            return False  # Not an increase

        self.heap.remove(task)          # O(n)
        heapq.heapify(self.heap)        # O(n)
        task.priority = new_priority
        heapq.heappush(self.heap, task) # O(log n)
        return True


# -------------------------------
# Sample usage
if __name__ == "__main__":
    pq = PriorityQueue()

    # Insert tasks
    pq.insert(Task("T1", 5, 0, 10))
    pq.insert(Task("T2", 2, 1, 5))
    pq.insert(Task("T3", 3, 2, 6))

    print("\nInitial tasks in heap:")
    for task in pq.heap:
        print(task)

    # Extract highest-priority (lowest value)
    print("\nExtracted:", pq.extract_min())  # Should be T2
    print("Extracted:", pq.extract_min())    # Should be T3

    # Insert another task
    pq.insert(Task("T4", 7, 3, 8))

    # Decrease key
    pq.decrease_key("T4", 1)
    print("\nAfter decreasing T4 priority to 1:")
    print("Extracted:", pq.extract_min())  # Should be T4

    # Check if queue is empty
    print("\nIs queue empty?", pq.is_empty())
