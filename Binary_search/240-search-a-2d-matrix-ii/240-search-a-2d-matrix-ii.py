class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -=1
            elif target > matrix[row][col]:
                row +=1
                
        return False

# Solution 2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)

# any() 와 all() 함수
# any()는 포함된 값중 어느 하나가 참이라면 항상 참으로 출력(논리 합)
# all()은 포함된 값들 모두가 참이라면 참으로 출력 (논리 곱)