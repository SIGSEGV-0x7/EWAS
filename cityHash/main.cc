

#include <cstdio>
#include <stddef.h>
#include <stdlib.h>
#include <inttypes.h>
#include <fstream>
#include <iostream>
#include <cstring>
#include <string.h>
#include "city.h"




int main(int argc, char** argv) {
    std::ofstream newFile;
    newFile.open("hashValue.csv");
    std::ifstream myFile;
    myFile.open("origin_simpleclean.csv");
    std::string line;
    newFile << "Cleaned Original URL" << "," << "City Hash: 64 bit Hash Value" << "," << "City Hash: 32 bit Hash Value" << "\n";
    
    size_t mesgLength;
    std::string result64;
    std::string result32;
    
    while (myFile.good()){
        getline(myFile, line, '\n');
        const char * mesg = line.c_str();
        mesgLength = line.size();
        
        //64
        result64 = std::to_string(CityHash64(mesg, mesgLength));
        //32
        result32 = std::to_string(CityHash32(mesg, mesgLength));
        
        
        line.erase(line.length()-1);
        newFile << line << "," << result64 << "," << result32<< "\n";

    }


    
}
