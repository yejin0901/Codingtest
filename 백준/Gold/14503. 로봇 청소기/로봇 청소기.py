# 청소하는 영역개수 구하기
# 북 동 남 서 0 1 2 3
# 반시계 90회전, 청소되지 않은 경우 한칸 전진 후 청소

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]


def clean_room(r, c, d, room):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    answer = 0
    while True:
        if room[r][c] == 0:
            room[r][c] = 2
            answer += 1

        cleaned = False
        for _ in range(4):
            nd = (d - 1) % 4 
            nx, ny = r + dx[nd], c + dy[nd]
            if room[nx][ny] == 0:
                r, c, d = nx, ny, nd
                cleaned = True
                break
            d = nd 

        if not cleaned:
            nx, ny = r - dx[d], c - dy[d]
            if room[nx][ny] == 1:
                break
            r, c = nx, ny  

    return answer

result = clean_room(r, c, d, room)
print(result)






