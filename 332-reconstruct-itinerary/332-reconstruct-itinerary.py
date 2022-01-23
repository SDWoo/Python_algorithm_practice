class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a,b in sorted(tickets, reverse = True):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            print(a)
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
            print(a,route)
            
        dfs('JFK')
        
        return route[::-1]