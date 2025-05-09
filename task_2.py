import turtle
import math

def draw_tree(t, length, depth):
    if depth > 0:
        t.forward(length)
        t.left(45)
        draw_tree(t, length * math.sqrt(2)/2, depth - 1)
        t.right(90)
        draw_tree(t, length * math.sqrt(2)/2, depth - 1)
        t.left(45)
        t.backward(length)

def main():
    turtle_speed = 10  
    initial_length = 100  

    depth = int(input("Enter recursion level: "))

    t = turtle.Turtle()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(turtle_speed)

    draw_tree(t, initial_length, depth)

if __name__ == "__main__":
    main()
