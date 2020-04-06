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

std::string TestResults(int seed, std::string str)
{
    uint64 hash1 = seed;
    uint64 hash2 = seed;
    //char shorturl[4][100];
    const void * a;
    //char url[4][100] = {"geeksforgeeksarraystringsc3differentwayscreate", "youtubewatchvLDGrxUBcNk", "youtubecomwatchvvzEjhC1kmY", "drivegoogledriveu1folders1poJ4O9CoE6ZZD2yerx3jLT4SqgdHctsb"};
    //for (int i = 0; i<4; i++){
      //  printf ("--------------------\n initial url is --> %s \n", url[i]);
        //std::string str = url[i];
        //size_t size = str.size();
        //printf("the unsigned decimal of the url %zu\n", size);  // prints as unsigned decimal
        //printf("the hex of the url %zx\n", size);  // prints as hex
        //printf("the signed decimal of the url %zd\n", size);  // prints as signed decimal
        //a = str.c_str();
        //SpookyHash::Hash128(a, size, &hash1, &hash2);
        //printf("data %d %p\n", *(const int *) a, a);
        //printf("%" PRIu64 "\n", hash1);
        //printf("%" PRIu64 "\n", hash2);
    size_t size = str.size();
    a = str.c_str();
    SpookyHash::Hash128(a, size, &hash1, &hash2);
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
    while (myFile.good()){
        getline(myFile, line, '\n');
        std::string result = TestResults(argc, line);
        line.erase(line.length()-1);
        newFile << line << "," << result << "\n";
        //printf("%s \n", line.c_str());
        // size_t size = line.size();
        //printf("the unsigned decimal of the url %zu\n", size);
    }
    

}
