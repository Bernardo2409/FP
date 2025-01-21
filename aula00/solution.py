# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)
    with open( 'D:\UA\1ano\FP\aula06\drawing.txt' , 'r') as fileobj:
        for line in fileobj:
            line = line.strip()
            if line == "UP":
                t.up()
            elif line == "DOWN":
                t.down()
            else:
                coords = line.split(" ")
                x,y = int(coords[0]), int(coords[1])
                t.goto(x,y)
        

    # Put your code here


    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()


