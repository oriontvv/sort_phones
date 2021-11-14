#include <iostream>
#include <fstream>
#include <iomanip>


int main(int argc, char** argv) {

    if (argc != 2) {
        std::cout << "Usage: gen path_to_file" << std::endl;
        return -1;
    }

    std::ofstream out(argv[1]);
    
    int n = 1000000000;

    while(--n >= 100000000) {
        out << "+79" << n << "\n";
    }

    while(--n >= 0) {
        out << "+79";
        out << std::setfill('0') << std::setw(9) << n << "\n";
    }
    out.close();

    return 0;
}
