#include "SpookyV2.h"
#include "MurmurHash2.h"
#include "MurmurHash3.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <cstring>
#include <inttypes.h>
#include <iostream>
#include <fstream>
#include <sstream>


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

std::string TestMurmur3(const void * message, size_t size, int seed){
    int len = static_cast<int>(size);
    uint32_t seedHolder = seed;
    uint64_t out[2] = {};
    MurmurHash3_x64_128 (message, len, seedHolder, out);
    std::string hashOne = std::to_string(out[0]);
    std::string hashTwo = std::to_string(out[1]);
    std::string whole = hashOne + hashTwo;
    return whole;
}


int main(int argc, const char **argv)
{
    

    std::ofstream newFile;
    newFile.open("hash128bit.csv");
    std::ifstream myFile;
    myFile.open("origin_simpleclean.csv");
    std::string line;
    newFile << "Cleaned Original URL" << "," << "Spooky Hash: 128 bit Hash Value" << "," << "Spooky Hash: 64 bit Hash Value" << "," << "Spooky Hash: 32 bit Hash Value" << "," << "Mumur Hash: 64 bit Hash Value" << ","<< "Mumur Hash: 128 bit Hash Value"<<"\n";

    size_t mesgLength;
    std::string result;
    std::string result64;
    std::string result32;
    std::string mResult64;
    std::string mResult128;

    
    
    
    
    while (myFile.good()){
        getline(myFile, line, '\n');
        const void * mesg = line.c_str();
        mesgLength = line.size();
        //SpookyHash
        //128 bit hash value
        result = TestResults(argc, mesg, mesgLength);
        //64
        result64 = std::to_string(SpookyHash::Hash64(mesg, mesgLength, 0));
        //32
        result32 = std::to_string(SpookyHash::Hash32(mesg, mesgLength, 0));
        
        //MurmurHash2
        mResult64 = std::to_string(MurmurHash64A (mesg, static_cast<int>(mesgLength), 1));
        
        //murmurHash3
        mResult128 = TestMurmur3(mesg, mesgLength, argc);
        
        line.erase(line.length()-1);
        newFile << line << "," << result << "," << result64 << "," << result32 << "," << mResult64 << ","<< mResult128 << "\n";
        //printf("%s \n", line.c_str());
        // size_t size = line.size();
        //printf("the unsigned decimal of the url %zu\n", size);
    }
    

}

