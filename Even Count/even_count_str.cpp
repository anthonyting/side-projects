#include <iostream>
#include <fstream>
#include <string>
#include <cerrno>
#include <cstring>
#include <chrono>

using namespace std;

// Implemented with a buffer and C++ strings

class totalWithLen {
// container for returning both a total and the size
    public:
        totalWithLen(unsigned long long int total, unsigned long long int len) : total(total), len(len) {};
        const unsigned long long int total;
        const unsigned long long int len;
};

totalWithLen get_file_contents(const char *filename) {
    
    ifstream in(filename, ios::binary | ios::ate);

    if (in) {
        unsigned long long int total = 0;
        const streamoff len = in.tellg(); // streamoff (should be type long long) used to cast tellg()
        in.seekg(0, ios::beg);

        constexpr unsigned int bufferSize = 1024*1024;
        string buffer;
        buffer.reserve(bufferSize);
        
        const streamoff maxPos = len - bufferSize;
        unsigned int i = 0;

        while (in) {
            if ((streamoff) in.tellg() >= maxPos) {
            // when the buffer exceeds the length of file (last section)
                in.read(&buffer[0], len-in.tellg()); // read to end of file
                for (char& c: buffer) {
                    // do stuff
                    if (buffer[i]%2) {
                        total++;
                    }
                }
                break;
            }
            in.read(&buffer[0], bufferSize);
            for (; i < bufferSize; i++) {
            // calculate total of even numbers in buffer
                if (buffer[i]%2) {
                    total++;
                }
            }
            i = 0;
        }

        in.close();

        totalWithLen result(total, len);

        return result;
    }
    cerr << "Error: " << strerror(errno) << endl;
    throw(errno);
}

int main(int argc, char *argv[]) {
    if (argc == 1) {
        cerr << "Error: Missing filename argument" << endl;
        return 0;
    }

    auto start = chrono::high_resolution_clock::now();
    
    totalWithLen result = get_file_contents(argv[1]);

    auto finish = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed = finish - start;
    cout << "Total: " << result.total << endl;
    cout << "Filesize: " << result.len << endl;
    cout << "Ratio: " << result.total/(long double) result.len << endl;
    cout << "Elapsed time: " << elapsed.count() << " s" << endl;
}