function is_triangle(sides)
    a,b,c = sort(sides)
    return (a > 0) && (a+b > c)
end

 function is_equilateral(sides)
    a,b,c = sort(sides)
    return is_triangle(sides) && (a == c)
end
    
 function is_isosceles(sides)
    a,b,c = sides
    return is_triangle(sides) && ((a == b)||(a==c)||(b==c))       
 end
 
 function is_scalene(sides)
    a,b,c = sides
    return is_triangle(sides) && ((a != c) && (a != b) && (b != c))
 end
 