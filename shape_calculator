class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __str__(self):
        return ('Rectangle(width={0:}, height={1:})'.format(self.width,self.height) )
    def set_height(self,height):
        self.height = height
    def set_width(self,width):
        self.width = width
    def get_area(self):
        return (self.width * self.height)
    def get_perimeter(self):
        return ((2*self.width) + (2*self.height))
    def get_diagonal (self):
        return ((self.width ** 2 + self.height ** 2) **.5)
    def get_picture(self):
        height_num = self.height
        height_cycle = 0
        width_num = self.width
        width_cycle = 0
        if width_num > 50 or height_num > 50:
            return "Too big for picture"
        if width_num < 50 and height_num < 50:
            while height_num != 0:
                height_cycle = height_cycle + 1
                width_cycle = 0
                while width_num != 0:
                    print('*',end ='')
                    width_num = width_num - 1
                    width_cycle = width_cycle + 1
                    if width_num == 0:
                        width_num = width_num + width_cycle
                        print ('\n', end='')
                        break
                height_num = height_num - 1
    def get_amount_inside(self, object):
        height_fit = self.height//object.height
        width_fit = self.width//object.width
        return height_fit*width_fit
class Square (Rectangle):
    def __init__(self,side):
        self.width = side
        self.height = side
    def __str__(self):
        return ('Square(side={})'.format(self.width))
    def set_side(self,side):
        self.width = side
        self.height = side
