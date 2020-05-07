#include <cstdio>
#include <stddef.h>
#include <stdlib.h>
#include <inttypes.h>
#include <fstream>
#include <iostream>
#include <cstring>
#include <string.h>
#include "city.h"

//read input file and 
int main(int argc, char** argv) {
    //open new csv file to store ouput
    std::ofstream newFile;
    newFile.open("hashValue.csv");
    //open input file
    std::ifstream myFile;
    myFile.open("origin_simpleclean.csv");
    std::string line;
    //named each column
    newFile << "Cleaned Original URL" << "," << "City Hash: 64 bit Hash Value" << "," << "City Hash: 32 bit Hash Value" << "\n";
    
    size_t mesgLength;
    std::string result64;
    std::string result32;
    
    while (myFile.good()){
        //read line
        getline(myFile, line, '\n');
        const char * mesg = line.c_str();
        mesgLength = line.size();
        
        //64 bit hash value
        result64 = std::to_string(CityHash64(mesg, mesgLength));
        //32 bit hash value
        result32 = std::to_string(CityHash32(mesg, mesgLength));
        
        //store the ouput to the new csv
        line.erase(line.length()-1);
        newFile << line << "," << result64 << "," << result32<< "\n";

    }


    
}
