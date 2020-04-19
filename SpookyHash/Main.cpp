#include "SpookyV2.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <cstring>
#include <inttypes.h>
#include <iostream>
#include <fstream>

std::string TestResults(int seed, const void * message, size_t size)
{
    uint64 hash1 = seed;
    uint64 hash2 = seed;
    SpookyHash::Hash128(message, size, &hash1, &hash2);
    std::string hashOne = std::to_string(hash1);
    std::string hashTwo = std::to_string(hash2);
    std::string whole = hashOne + hashTwo;
    //printf("%s\n", whole.c_str());
    return whole;
    
    
}


int main(int argc, const char **argv)
{
    

    std::ofstream newFile;
    newFile.open("hash128bit.csv");
    std::ifstream myFile;
    myFile.open("originalURL.csv");
    std::string line;
    newFile << "Cleaned Original URL" << "," << "128 bit Hash Value" << "," << "64 bit Hash Value" << "," << "32 bit Hash Value" << "\n";

    size_t mesgLength;
    std::string result;
    std::string result64;
    std::string result32;
    
    
    
    
    while (myFile.good()){
        getline(myFile, line, '\n');
        const void * mesg = line.c_str();
        mesgLength = line.size();
        //128 bit hash value
        result = TestResults(argc, mesg, mesgLength);
        //64
        result64 = std::to_string(SpookyHash::Hash64(mesg, mesgLength, 0));
        //32
        result32 = std::to_string(SpookyHash::Hash32(mesg, mesgLength, 0));
        
        line.erase(line.length()-1);
        newFile << line << "," << result << "," << result64 << "," << result32 << "\n";
        //printf("%s \n", line.c_str());
        // size_t size = line.size();
        //printf("the unsigned decimal of the url %zu\n", size);
    }
    

}
