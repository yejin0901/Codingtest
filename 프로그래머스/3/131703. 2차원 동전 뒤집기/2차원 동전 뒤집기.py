def solution(beginning, target):
    n, m = len(beginning), len(beginning[0])
    
    # 행을 뒤집는 경우의 수 계산
    def flip_row(matrix, row):
        new_matrix = [list(r) for r in matrix]
        for c in range(m):
            new_matrix[row][c] = 1 - new_matrix[row][c]
        return new_matrix
    
    # 열을 뒤집는 경우의 수 계산
    def flip_col(matrix, col):
        new_matrix = [list(r) for r in matrix]
        for r in range(n):
            new_matrix[r][col] = 1 - new_matrix[r][col]
        return new_matrix

    # DFS로 최소 뒤집기 횟수 찾기
    def dfs(matrix, flips, row, col):
        if row == n:
            # 모든 행을 처리한 후, 열 처리 시작
            if col < m:
                # 현재 열을 뒤집는 경우
                new_matrix = flip_col(matrix, col)
                dfs(new_matrix, flips + 1, row, col + 1)
                # 현재 열을 뒤집지 않는 경우
                dfs(matrix, flips, row, col + 1)
            else:
                # 모든 열 처리가 완료된 경우, 최종 상태 확인
                if matrix == target:
                    nonlocal min_flips
                    min_flips = min(min_flips, flips)
            return

        # 현재 행을 뒤집는 경우
        new_matrix = flip_row(matrix, row)
        dfs(new_matrix, flips + 1, row + 1, col)
        # 현재 행을 뒤집지 않는 경우
        dfs(matrix, flips, row + 1, col)

    min_flips = float('inf')
    dfs(beginning, 0, 0, 0)
    return min_flips if min_flips != float('inf') else -1

