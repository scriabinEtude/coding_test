import sys

input = sys.stdin.readline

Tu = """
1111
0000
0000
0000
"""
Tr = """
1000
1000
1000
1000
"""
ou = """
1100
1100
0000
0000
"""
lu = """
1000
1000
1100
0000
"""
lr = """
1110
1000
0000
0000"""
ld = """
1100
0100
0100
0000"""
ll = """
0010
1110
0000
0000"""
ju = """
0100
0100
1100
0000
"""
jr = """
1000
1110
0000
0000"""
jd = """
1100
1000
1000
0000"""
jl = """
1110
0010
0000
0000"""
su = """
0110
1100
0000
0000"""
sr = """
1000
1100
0100
0000"""
zu = """
1100
0110
0000
0000"""
zr = """
0100
1100
1000
0000"""
tu = """
1110
0100
0000
0000"""
tr = """
0100
1100
0100
0000"""
td = """
0100
1110
0000
0000"""
tl = """
1000
1100
1000
0000"""


class Tetris:
    def __init__(self, shape, height, width):
        self.shape = shape
        self.height = height
        self.width = width


class TetrisFactory:
    def create(bluePrint: str) -> Tetris:
        tetris = bluePrint.strip().split()
        height = 0
        width = 0
        for index, row in enumerate(tetris):
            new = []
            for i in range(4):
                if row[i] == "1":
                    new.append(i)
                    width = max(width, i + 1)
            tetris[index] = new
        for _ in range(tetris.count([])):
            tetris.remove([])
        height = len(tetris)

        return Tetris(tetris, height, width)


class Paper:
    def __init__(self, paper, width, height):
        self.paper = paper
        self.width = width
        self.height = height


def find_max_score(paper: Paper, tetris_list: list[Tetris]):
    high_score = 0
    for t in tetris_list:
        # print(t.shape, t.width, t.height)
        for x in range(paper.width - t.width + 1):
            for y in range(paper.height - t.height + 1):
                total = 0
                for i, row in enumerate(t.shape):
                    for j in row:
                        # print(x, y, j, i, x + j, y + i, paper.paper[y + i][x + j])
                        total += paper.paper[y + i][x + j]

                # print(total)
                high_score = max(high_score, total)
        # print(high_score)

    print(high_score)


tetris = list(
    map(
        TetrisFactory.create,
        [Tu, Tr, ou, lu, lr, ld, ll, ju, jr, jd, jl, su, sr, zu, zr, tu, tr, td, tl],
    )
)

# height = 5
# width = 5
# paper = [
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
#     [2, 3, 4, 5, 6],
#     [6, 5, 4, 3, 2],
#     [1, 2, 1, 2, 1],
# ]

# height = 4
# width = 5
# paper = [
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5],
# ]

height, width = map(int, input().split())
paper = []

for _ in range(height):
    paper.append(list(map(int, input().split())))

paper = Paper(paper, width, height)
find_max_score(paper, tetris)
