import turtle
import time

# เขาวงกตใหม่ที่มีทางออกแน่นอน
maze = [
    "#############",
    "#S#.......#E#",
    "#.#.#####.#.#",
    "#.#.....#.#.#",
    "#.#####.#.#.#",
    "#.....#.#...#",
    "#####.#.###.#",
    "#...........#",
    "#############"
]

# ขนาดช่องในเขาวงกต
CELL_SIZE = 30
OFFSET_X = -len(maze[0]) * CELL_SIZE // 2
OFFSET_Y = len(maze) * CELL_SIZE // 2

# ตั้งค่าหน้าจอ
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

# เต่าสำหรับวาดกำแพง
wall_drawer = turtle.Turtle()
wall_drawer.speed(0)
wall_drawer.color("white")
wall_drawer.penup()

# เต่าตัวหลักที่เดินทาง
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()

# วาดเขาวงกต
start = None
end = None
walls = set()

for i, row in enumerate(maze):
    for j, cell in enumerate(row):
        x = OFFSET_X + j * CELL_SIZE
        y = OFFSET_Y - i * CELL_SIZE
        
        if cell == "#":
            walls.add((i, j))
            wall_drawer.goto(x, y)
            wall_drawer.pendown()
            wall_drawer.begin_fill()
            for _ in range(4):
                wall_drawer.forward(CELL_SIZE)
                wall_drawer.right(90)
            wall_drawer.end_fill()
            wall_drawer.penup()
        elif cell == "S":
            player.goto(x, y)
            start = (i, j)
        elif cell == "E":
            end = (i, j)

screen.update()

# ทิศทางที่เต่าสามารถเดินไปได้
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# เต่าเขียนเส้นทางที่เดินผ่าน
path_drawer = turtle.Turtle()
path_drawer.speed(0)
path_drawer.shape("circle")
path_drawer.shapesize(0.5)
path_drawer.penup()
path_drawer.color("green")


def move_turtle(i, j):
    """ เคลื่อนที่เต่าตามพิกัดที่กำหนด """
    x = OFFSET_X + j * CELL_SIZE
    y = OFFSET_Y - i * CELL_SIZE
    player.goto(x, y)
    path_drawer.goto(x, y)
    path_drawer.stamp()
    screen.update()
    time.sleep(0.2)


def solve_maze(position, visited):
    """ ใช้ DFS หาทางออกจากเขาวงกต """
    x, y = position

    if position == end:
        print("🎉 เต่าออกจากเขาวงกตสำเร็จ! 🎉")
        return True  # เจอทางออก

    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        new_pos = (new_x, new_y)

        if new_pos not in walls and new_pos not in visited:
            move_turtle(new_x, new_y)
            visited.add(new_pos)

            if solve_maze(new_pos, visited):
                return True

            move_turtle(x, y)  # ถอยกลับถ้าทางตัน

    return False


# ตรวจสอบว่ามีทางออกจริง ๆ
if solve_maze(start, {start}):
    print("✔ เต่าสามารถเดินออกได้")
else:
    print("❌ ERROR: เขาวงกตไม่มีทางออก!")

screen.mainloop()
