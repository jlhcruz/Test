def search_white_pixel(dimensions, M):
    rows = dimensions[0]
    columns = dimensions[1]
    MDist = [[-1] * columns for _ in range(rows)]
    MVisit = [[False] * columns for _ in range(rows)]
    visit_point = []

    for i in range(rows):
        for j in range(columns):
            if M[i][j] == 1:
                MDist[i][j] = 0
                MVisit[i][j] = True
                visit_point.append((i, j))

    while visit_point:
        r, c = visit_point.pop()
        for row, col in ((r, c + 1), (r + 1, c), (r, c - 1)):
            if 0 <= row < rows and 0 <= col < columns and not MVisit[row][col]:
                MDist[row][col] = MDist[r][c] + 1
                MVisit[row][col] = True
                visit_point.append((row, col))

    return MDist


if __name__ == '__main__':
    for _ in range(int(input())):
        dimensions = list(map(int, input().split()))
        M = []
        for _ in range(dimensions[0]):
            M.append(list(map(int, list(input()))))

        MD = search_white_pixel(dimensions, M)
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                print(MD[i][j], end=' ', sep='\n')
            print()
