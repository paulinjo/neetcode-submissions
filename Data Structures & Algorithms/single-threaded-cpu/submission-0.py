import heapq

from collections import namedtuple

WaitingTask = namedtuple('WaitingTask', ['enqueue_time', 'processing_time', 'index'])
ReadyTask = namedtuple('ReadyTask', ['processing_time', 'index'])

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        current_time = 0
        ready_tasks = []
        waiting_tasks = [WaitingTask(enqueue_time=task[0], processing_time=task[1], index=i) for task, i in zip(tasks, range(len(tasks)))]
        heapq.heapify(waiting_tasks)
        
        results = []
        while waiting_tasks or ready_tasks:
            while waiting_tasks and waiting_tasks[0].enqueue_time <= current_time:
                task = heapq.heappop(waiting_tasks)
                heapq.heappush(ready_tasks, ReadyTask(processing_time=task.processing_time, index=task.index))

            if not ready_tasks:
                task = heapq.heappop(waiting_tasks)
                current_time = task.enqueue_time
                heapq.heappush(ready_tasks, task)
            
            task = heapq.heappop(ready_tasks)
            results.append(task.index)
            current_time += task.processing_time

        return results

