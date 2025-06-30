#include "raindrops.h"

namespace raindrops {
    std::string convert(int x){
        std::string sound  = "";
        
        if (x%3==0){sound += "Pling";}
        if (x%5==0){sound += "Plang";}
        if (x%7==0){sound += "Plong";}
        if (sound == "") {sound = std::to_string(x);}
        
        return sound;
    }

}  // namespace raindrops
