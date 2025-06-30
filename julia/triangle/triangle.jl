
 function is_equilateral(x,y,z)
     if (x>0)&&(y>0)&&(z>0)
         if (x+y>=z)||(x+z>=y)||(y+z>=x)
             if (x == z == y)
                 return true
             else 
                 return false
             end
         else
             return false
         end
     else 
         return false
     end
 end
 
 function is_isosceles(x,y,z)
     if (x>0)&&(y>0)&&(z>0)
         if (x+y>=z)||(x+z>=y)||(y+z>=x)
             if (x == z)||(x==y)||(y==z)
                 return true
             else 
                 return false
             end
         else
             return false
         end
     else 
         return false
     end
     
 end
 
 function is_scalene(x,y,z)
     if (x>0)&&(y>0)&&(z>0)
         if (x+y>=z)||(x+z>=y)||(y+z>=x)
             if (x != z)||(x !=y)||(y !=z)
                 return true
             else 
                 return false
             end
         else
             return false
         end
     else 
         return false
     end
     
 end
 