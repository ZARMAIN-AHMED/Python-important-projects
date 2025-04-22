from graphics import Canvas

def main():
    canvas = Canvas(400, 400)
    canvas.create_rectangle(50, 50, 150, 150, 'blue')
    canvas.wait_for_click()

if __name__ == '__main__':
    main()
