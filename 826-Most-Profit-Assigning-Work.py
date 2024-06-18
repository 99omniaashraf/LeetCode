class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # Pair jobs with their profits and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort workers by their ability
        worker.sort()
        
        total_profit = 0
        max_profit = 0
        job_index = 0
        n = len(jobs)
        
        # Iterate over each worker
        for ability in worker:
            # Move the job_index to the right until the worker can no longer do the job
            while job_index < n and jobs[job_index][0] <= ability:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            # Add the max profit this worker can achieve
            total_profit += max_profit
        
        return total_profit