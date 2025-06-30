#include <string>

namespace log_line {
    std::string message(std::string line) {
        // return the message
          if (line.find("WARNING") != std::string::npos){
            return line.substr(11);
        }
        else if (line.find("INFO") != std::string::npos){
            return line.substr(8);
        }
        else if (line.find("ERROR") != std::string::npos){
            return line.substr(9);
        }
        else {
            return 0;
        }
    }

    std::string log_level(std::string line) {
        // return the log level
         if (line.find("INFO") != std::string::npos){
            return ("INFO");
        }
        else if (line.find("WARNING") != std::string::npos){
            return ("WARNING");
        }
        else if (line.find("ERROR") != std::string::npos) {
            return ("ERROR");
        }
        else {return 0;}
    }

    std::string reformat(std::string line) {
        // return the reformatted message
         if (line.find("INFO") != std::string::npos){
            return line.substr(8)+ " " + "(INFO)";
        }
        else if (line.find("WARNING")!= std::string::npos){
            return line.substr(11)+ " " + "(WARNING)";
        }
        else if (line.find("ERROR") != std::string::npos){
            return line.substr(9)+ " " + "(ERROR)";
        }
        else {return 0;}

    }
}
