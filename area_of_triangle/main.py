import triangle
side_a=(int(input("Enter Length of Side A")))
side_b=(int(input("Enter Length of Side B")))
side_c=(int(input("Enter Length of Side C")))

s=(triangle.perimeter(side_a, side_b, side_c))/2
print(f'Perimeter in Main is: {s}')

area=triangle.find_area(s, side_a, side_b, side_c)
print(f'Area of given triangle is: {area}')
