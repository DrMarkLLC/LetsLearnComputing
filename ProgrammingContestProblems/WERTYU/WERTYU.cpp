#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

/**
 * C++ solution to the WERTYU Kattis problem.
 * 
 * Let's Learn Computing with Dr. Mark
 * 2021-11-20
 */
int main() {
    std::string keys = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./\n";
    std::map<char, char> map;

    // build the translation map
    for(size_t i = 1; i < keys.length(); i++) {
        map[keys[i]] = keys[i - 1];
    }
    map[' '] = ' ';

    // process the input
    std::string line;
    while(std::getline(std::cin, line)) {
        for(char ch : line) {
            std::cout << map[ch];
        }
        std::cout << std::endl;
    }
}