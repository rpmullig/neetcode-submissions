class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build graph elements 
        vertexes = set()
        out_edges = collections.defaultdict(set)
        in_edges = collections.defaultdict(set)
        for prereq in prerequisites:
            a, b = prereq[0], prereq[1]
            # vertexes.add(a)
            # vertexes.add(b)
            in_edges[a].add(b)
            out_edges[b].add(a)
        
        for i in range(numCourses):
            vertexes.add(i) # there are this many courses some to complete independently

        # identify the starting points (aka sink)
        q = collections.deque()
        for v in range(numCourses):
            if len(in_edges[v]) == 0: # no requirements
                q.append(v)


        # bfs from classes with no requirements 
        visited = set()
        courses_completed = 0
        while len(q) > 0:
            n = len(q)
            for _ in range(n):
                v = q.popleft()
                if v in visited:
                    continue 
                visited.add(v)
                courses_completed += 1
                for next_vertex in out_edges[v]:
                    if in_edges[next_vertex].issubset(visited):
                        q.append(next_vertex)
        

        return courses_completed == numCourses
