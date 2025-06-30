
function bob(stimulus)
     stimulus = strip(stimulus)
     if length(stimulus) == 0
         return "Fine. Be that way!"
     end
 
     is_yell = any(isletter, stimulus) && stimulus == uppercase(stimulus)
     is_question = last(stimulus) == '?'
 
     if is_yell && is_question
         return "Calm down, I know what I'm doing!"
     end
     if is_yell
         return "Whoa, chill out!"
     end
     if is_question
         return "Sure."
     end
 
     return "Whatever."
 end