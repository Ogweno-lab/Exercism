"Square the sum of the first `n` positive integers"
function square_of_sum(n)
    sum = 0
    for i in 1:n
        sum = sum + i
    end
    square_of_sums = sum^2
    return square_of_sums

end

"Sum the squares of the first `n` positive integers"
function sum_of_squares(n)
    sum_of_squaress = 0 
    for i in 1:n
        sum_of_squaress = sum_of_squaress + i^2
    end
    return sum_of_squaress

end

"Subtract the sum of squares from square of the sum of the first `n` positive ints"
function difference(n)
    difference = square_of_sum(n) - sum_of_squares(n)
end
return difference
