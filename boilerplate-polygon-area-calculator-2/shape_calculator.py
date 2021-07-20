

class Rectangle:

  def __init__(self,width,height):
    '''When a Rectangle object is created, 
    it should be initialized with `width` and `height` attributes'''
    self.width=width
    self.height=height
  def __str__(self):
    '''if an instance of a Rectangle is represented as a string, it should look like: `Rectangle(width=5, height=10)`'''
    return f"Rectangle(width={self.width}, height={self.height})"
      
    
  def set_width(self,width):
    '''`set_width`'''
    self.width=width

  def set_height(self,height):
    self.height=height
  
  def get_area(self):
    '''get_area`: Returns area (`width * height`)'''
    return self.width*self.height
  
  def get_perimeter(Self):
    '''`get_perimeter`: Returns perimeter (`2 * width + 2 * height`)'''
    return ((2*Self.height)+(2*Self.width))

  def get_diagonal(self):
    '''`get_diagonal`: Returns diagonal (`(width ** 2 + height ** 2) ** .5`)'''
    return (((self.width**2)+(self.height**2))**.5)

  def get_picture(self):
    '''`get_picture`: Returns a string that represents the shape using lines of "\*".
     The number of lines should be equal to the height and the number of "\*" 
     in each line should be equal to the width. 
     There should be a new line (`\n`) at the end of each line. 
     If the width or height is larger than 50, this should 
     return the string: "Too big for picture.".'''
    if(self.width>50)or(self.height>50):
      return "Too big for picture."
    string=(("*"*self.width)+"\n")*self.height
    return string

  def get_amount_inside(self,shape):
    '''`get_amount_inside`: Takes another shape (square or rectangle) as an argument.
     Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
     For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.'''
    return int(self.get_area()/shape.get_area())






class Square(Rectangle):
  
  def __init__(self, side):
    '''The Square class should be a subclass of Rectangle. When a Square object is created, 
    a single side length is passed in. The `__init__` method should store the side length in 
    both the `width` and `height` attributes from the Rectangle class.'''
    self.width=side
    self.height=side

  def __str__(self):
    '''The Square class should be able to access the Rectangle class 
    methods but should also contain a `set_side` method.
     If an instance of a Square is represented as a string, 
     it should look like: `Square(side=9)`'''
    return f"Square(side={self.width})"

  def set_side(self,side):
    self.width=side
    self.height=side
   
  
