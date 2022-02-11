class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                print(task)
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 제거하는 유용한 핵
                counter += collections.Counter()
                
            if not counter:
                break
            
            # idle 횟수 더하기
            result += n - sub_count + 1
            
        return result