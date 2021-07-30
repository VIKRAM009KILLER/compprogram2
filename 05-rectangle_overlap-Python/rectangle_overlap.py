# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function 
# takes two rectangles described this way, and returns True if the rectangles 
# overlap at all (even if just at a point), and False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, and while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 
# head down (so we say that "up is down")

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):

    x1, y1 = left1, top1
    p1, q1 = left1+width1, top1
    m1, n1 = left1, top1+height1
    a1, b1 = width1+left1, height1+top1

    x2, y2 = left2, top2
    p2, q2 = left2+width2, top2
    m2, n2 = left2, top2+height2
    a2, b2 = width2+left2, height2+top2

    r1 = []

    t11 = (x1, y1)
    r1.append(t11)
    t12 = (p1, q1)
    r1.append(t12)
    t13 = (m1, n1)
    r1.append(t13)
    t14 = (a1, b1)
    r1.append(t14)

    r2 = []

    t21 = (x2, y2)
    r2.append(t21)
    t22 = (p2, q2)
    r2.append(t22)
    t23 = (m2, n2)
    r2.append(t23)
    t24 = (a2, b2)
    r2.append(t24)

    for i in r1:
        if i in r2:
            return True
    
    return False





    


    


    return True

        