# spiral order LeetCode

def spiralOrder(rows, cols, rStart, cStart):
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
  result = []
  visited = set()

r, c = rStart, cStart
d = 0 # start with the direction going right
steps = 1 # initial number of steps in a particular direction

while len(result) < rows * cols:
  for _ in range(2): # we increase steps after 2 turns?
    for _ in range(steps):
      if 0 <= r < rows and 0 <= c < cols:
        result.append([r, c])
      r += directions[d][0]
      c += directions[d][1]
    # turn to the next direction
    d = (d + 1) % 4
  steps += 1

return result
