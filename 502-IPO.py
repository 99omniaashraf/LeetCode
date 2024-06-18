class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        \\\
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        \\\
        # Create a list of projects with (capital, profit)
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        
        # Sort projects by their capital requirements
        projects.sort()
        
        max_profit_heap = []
        current_capital = w
        index = 0
        n = len(projects)
        
        for _ in range(k):
            # Push all projects that can be started with the current capital to the max profit heap
            while index < n and projects[index][0] <= current_capital:
                heapq.heappush(max_profit_heap, -projects[index][1])
                index += 1
            
            # If we have no projects we can start, break
            if not max_profit_heap:
                break
            
            # Select the project with the maximum profit
            current_capital += -heapq.heappop(max_profit_heap)
        
        return current_capital

        