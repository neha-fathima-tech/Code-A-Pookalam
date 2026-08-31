import turtle
import math

# ============================================================
# POOKALAM - RECREATION OF THE REFERENCE IMAGE
# ============================================================

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("#eeeeee")
screen.title("Pookalam")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

# ------------------------------------------------------------
# BASIC FUNCTIONS
# ------------------------------------------------------------

CX, CY = 0, 0


def polygon(radius, sides, rotation=0, fill="#000000",
            outline=None, width=1):
    points = []
    for i in range(sides):
        a = math.radians(rotation + i * 360 / sides)
        points.append((CX + radius * math.cos(a),
                       CY + radius * math.sin(a)))

    t.goto(points[0])
    t.pendown()

    if outline:
        t.pencolor(outline)
        t.pensize(width)

    t.fillcolor(fill)
    t.begin_fill()

    for p in points[1:]:
        t.goto(p)

    t.goto(points[0])
    t.end_fill()
    t.penup()


def circle(radius, color):
    t.goto(CX, CY - radius)
    t.setheading(0)
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def scalloped_ring(inner_r, outer_r, petals, color):
    # Alternating points create the scalloped/flower edge
    points = []

    for i in range(petals * 2):
        if i % 2 == 0:
            r = outer_r
        else:
            r = inner_r

        a = math.radians(i * 360 / (petals * 2))

        points.append(
            (CX + r * math.cos(a),
             CY + r * math.sin(a))
        )

    t.goto(points[0])
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.pendown()

    for p in points[1:]:
        t.goto(p)

    t.goto(points[0])
    t.end_fill()
    t.penup()


def line(x1, y1, x2, y2, color, width=1):
    t.goto(x1, y1)
    t.pencolor(color)
    t.pensize(width)
    t.pendown()
    t.goto(x2, y2)
    t.penup()


# ============================================================
# OUTER POOKALAM
# ============================================================

# Dark outer silhouette
polygon(
    355, 20, 9,
    fill="#70170f"
)

# Outer red flower layer
polygon(
    335, 20, 9,
    fill="#8d2115"
)

# Orange-red inner layer
polygon(
    315, 20, 9,
    fill="#bd301d"
)

# Bright orange-red layer
polygon(
    292, 20, 9,
    fill="#df3d20"
)

# Slightly lighter inner region
polygon(
    265, 20, 9,
    fill="#ed4b20"
)


# ============================================================
# GEOMETRIC LATTICE
# ============================================================

# The reference has a dark-red woven geometric pattern
# covering the outer orange/red section.

lattice_color = "#781a12"

# radial-ish polygon lines
for rotation in range(0, 360, 20):

    a = math.radians(rotation)

    # start near the outer edge
    x1 = CX + 285 * math.cos(a)
    y1 = CY + 285 * math.sin(a)

    # opposite point
    x2 = CX - 285 * math.cos(a)
    y2 = CY - 285 * math.sin(a)

    line(x1, y1, x2, y2, lattice_color, 3)


# second family of diagonals
for rotation in range(10, 360, 20):

    a = math.radians(rotation)

    x1 = CX + 285 * math.cos(a)
    y1 = CY + 285 * math.sin(a)

    x2 = CX - 285 * math.cos(a)
    y2 = CY - 285 * math.sin(a)

    line(x1, y1, x2, y2, lattice_color, 2)


# Circular boundary lines over lattice
for r in [280, 300, 320, 340]:
    t.goto(CX, CY - r)
    t.pencolor("#71180f")
    t.pensize(3)
    t.pendown()
    t.circle(r)
    t.penup()


# ============================================================
# YELLOW INNER PETAL RING
# ============================================================

# Yellow polygonal layer
polygon(
    230, 20, 9,
    fill="#f5c531"
)

# Orange-yellow inner layer
polygon(
    205, 20, 9,
    fill="#f7c52f"
)


# Make yellow radial petal sections visible
for i in range(20):
    a1 = math.radians(i * 18 - 5)
    a2 = math.radians(i * 18 + 5)

    p1 = (CX + 215 * math.cos(a1),
          CY + 215 * math.sin(a1))

    p2 = (CX + 155 * math.cos(a2),
          CY + 155 * math.sin(a2))

    line(
        p1[0], p1[1],
        p2[0], p2[1],
        "#d99c1c",
        2
    )


# ============================================================
# WHITE RING
# ============================================================

circle(150, "#f4f4f4")


# ============================================================
# GREEN SCALLOPED RING
# ============================================================

scalloped_ring(
    103,
    125,
    20,
    "#087c1c"
)


# Slight darker green edge
# creates a little depth similar to the reference
t.goto(CX, CY - 112)
t.pencolor("#075f18")
t.pensize(3)
t.pendown()
t.circle(112)
t.penup()


# ============================================================
# CENTRAL YELLOW / GOLD CIRCLE
# ============================================================

circle(100, "#f4b52d")

# subtle inner golden disk
circle(82, "#f6bd36")


# ============================================================
# CENTRAL SUN / FLOWER
# ============================================================

sun_color = "#8f280e"

# Large 20-point pointed sun
points = []

for i in range(40):
    if i % 2 == 0:
        r = 66
    else:
        r = 38

    a = math.radians(i * 9)

    points.append(
        (
            CX + r * math.cos(a),
            CY + r * math.sin(a)
        )
    )

t.goto(points[0])
t.fillcolor(sun_color)
t.pencolor(sun_color)
t.begin_fill()
t.pendown()

for p in points[1:]:
    t.goto(p)

t.goto(points[0])
t.end_fill()
t.penup()


# ============================================================
# INNER GOLD CIRCLE OF SUN
# ============================================================

circle(28, "#f5bd35")

# Dark central circle
circle(17, sun_color)

# Tiny golden center
circle(9, "#e9a928")


# ============================================================
# EXTRA INNER SUN DETAILS
# ============================================================

# Thin dark ring around the center
t.goto(CX, CY - 32)
t.pencolor("#a63a0e")
t.pensize(3)
t.pendown()
t.circle(32)
t.penup()


# ============================================================
# FINAL OUTER ACCENT
# ============================================================

# Small dark accents between outer petals
for i in range(20):
    a = math.radians(i * 18 + 9)

    x = CX + 337 * math.cos(a)
    y = CY + 337 * math.sin(a)

    t.goto(x, y)
    t.dot(7, "#5e130d")


# ============================================================
# DONE
# ============================================================

screen.mainloop()
