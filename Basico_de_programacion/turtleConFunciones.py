import turtle

def main():
    windows = turtle.Screen()
    carlos = turtle.Turtle()
    make_square(carlos)
    turtle.mainloop()

def make_square(carlos):
    length = int (input('tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(carlos,length)

def make_line_and_turn(carlos,length):
    carlos.forward(length)
    carlos.left(90)

if __name__ == '__main__':
    main()
