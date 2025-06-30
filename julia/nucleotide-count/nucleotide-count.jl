"""
    count_nucleotides(strand)

The count of each nucleotide within `strand` as a dictionary.

Invalid strands raise a `DomainError`.

"""
function count_nucleotides(strand::AbstractString)
    dict = Dict('A' => count(isequal('A'), strand),'C' => count(isequal('C'), strand),'G' => count(isequal('G'), strand),'T' => count(isequal('T'), strand))
    for i in strand
        if haskey(dict, i)
            dict = dict
        else
            throw(DomainError("INVALID"))
        end
    end
    return dict
end
