class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        class Task:
            def __hash__(self):
                return hash(self.letter)

            def __init__(self, letter):
                self.letter = letter
                self.count = 1
                self.last_ran = -n - 1
            
            def increment(self):
                self.count +=1 

            def decrement(self, i):
                self.count -= 1 
                self.last_ran = i

            def get_last_run(self):
                return self.last_ran

            def get_count(self):
                return self.count
                   
            def __lt__(self, other):
                return (self.count, self.last_ran) > (other.count, other.last_ran)

        map = dict()
        for task in tasks:
            if task not in map:
                map[task] = Task(task)
            else:
                map[task].increment()

        computations = list(map.values())
        heapq.heapify(computations)

        cycle_count = 0
        while len(computations) > 0:
            current_task = heapq.heappop(computations)
            if cycle_count - current_task.get_last_run() < n:
                    cycle_count += n - (cycle_count - current_task.get_last_run())
            current_task.decrement(cycle_count)
            cycle_count += 1
            if current_task.get_count() > 0:
                heapq.heappush(computations, current_task)


        return cycle_count
