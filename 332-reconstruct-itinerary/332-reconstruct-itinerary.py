class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in tickets:
            graph[a].append(b)
        for a in graph:
            graph[a].sort()
            print(graph)
        route = []
        
        def dfs(a):
            print(a)
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
            print(a,route)
            
        dfs('JFK')
        
        return route[::-1]