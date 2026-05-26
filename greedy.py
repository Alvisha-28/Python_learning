# You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker 
# where: difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and 
# worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with 
# difficulty at most worker[j]). 
# Every worker can be assigned at most one job, but one job can be completed multiple times. 
# For example, if 3 workers all can do the same job that pays $1, then you can assign the job to all 3 workers and make $3. 
# Return the maximum profit we can achieve
from typing import List

class Worker:
    def maxProfit(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        max_profit = 0
        total_profit = 0
        job_index = 0
        for ability in worker:
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                total_profit = max(total_profit, jobs[job_index][1])
                job_index += 1
            max_profit += total_profit
        return max_profit
res1 = Worker()
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
print(res1.maxProfit(difficulty, profit, worker))
res2 =  Worker()
difficulty = [85,47,57]
profit = [24,66,99] 
worker = [75,25,25]
print(res2.maxProfit(difficulty, profit, worker))