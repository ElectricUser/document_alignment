Image alignment script.
Takes as input an image of quadrilateral (book, document, etc...)
The user hand clicks the 4 vertices of it in a clock wise direction starting from top left vertice (it's a must be in this order or output image can be flipped upside down)
Applies an homography to the input image to align it in an upwards rectangle shape (in case of a book image it returns the book in the same position you would hold it to read it)
Outputs the aligned image.
