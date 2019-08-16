#include <iostream>
#include <fstream>
#include <string>
#include <cerrno>
#include <chrono>

using namespace std;

// Implemented without a buffer, this can use a lot of memory and take much more time for larger sets.

void get_file_contents(const char *filename, string& contents) {
  ifstream in(filename, ios::binary | ios::ate);
  if (in) {
    contents.resize(in.tellg());
    in.seekg(0, ios::beg);
    in.read(&contents[0], contents.size());
    in.close();
    return;
  }
  throw(errno);
}

int main(int argc, char *argv[]) {
    if (argc == 1) {
        cerr << "Error: Missing filename argument" << endl;
        return 0;
    }

    string file;
    auto start = chrono::high_resolution_clock::now();
    get_file_contents(argv[1], file);
    
    unsigned long long int total = 0;
    
    for(char& c : file) {
      // do stuff
        if (c%2) {
            total++;
        }
    }
    auto finish = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed = finish - start;
    
    cout << "Total: " << total << endl;
    cout << "Filesize: " << file.length() << endl;
    cout << "Ratio: " << total/(long double) file.length() << endl;
    cout << "Elapsed time: " << elapsed.count() << " s" << endl;
}