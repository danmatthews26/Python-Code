#program that draws a box with |,-

width = int(input("What will be the width? ")) #width of drawing
height = int(input("What will be the height? ")) #height of drawing

def draw_box(w,h): #draws the box (width, height) 
    print("- " * w)
    for i in range(0, h):
        print("|" + "  " * (w - 1) + "|")
    print("- " * w)    

draw_box(width,height)    