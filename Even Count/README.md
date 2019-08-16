# Even Count

Iterates through all digits in a .txt file and displays how many are even. Optimized for large data sets like pi available at <https://archive.org/details/Math_Constants> or <https://archive.org/details/pi_dec_1t>. The operation done at each digit can be modified.

Available are three C++ implementations, and one Python 3.6+ implementation.

Filename|Speed|Memory
--|--|--
even_count_char.cpp | very fast | low memory usage
even_count_str.cpp | very fast | low memory usage
even_count_no_buffer.cpp | fast | very high memory usage
even_count_slow.py | extremely slow | low memory usage

## Usage

Get the files in the directory, then:

Compile the C++ files with fast optimizations in Windows or Linux.

* MSVC: `cl <filename>.cpp /O2 /EHsc /Feeven_count`
* g++: `g++ <filename>.cpp -O3 -o even_count`

Run code via command line with the name of a file containing only digits.

* Windows Powershell: `./even_count <filename>` and `python even_count_slow.py <filename>`
* Linux: `./even_count <filename>` and `./even_count_slow.py <filename>`

## Tests

On my machine, testing on 1 billion digits of pi from <https://archive.org/details/Math_Constants>. Linux tests were done in WSL.

File|Time (s)|Compiler/Interpreter
--|--|--
-|-|**Linux**
even_count_char.cpp|0.458392|gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04)
even_count_str.cpp|0.455864|gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04)
even_count_no_buffer.cpp|1.32035|gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04)
even_count_slow.py|172.531|Python 3.6.8 [GCC 8.0.1 20180414] on linux
-|-|**Windows**
even_count_char.cpp|1.23241|Microsoft (R) C/C++ Optimizing Compiler Version 19.22.27905 for x64
even_count_str.cpp|1.42918|Microsoft (R) C/C++ Optimizing Compiler Version 19.22.27905 for x64
even_count_no_buffer.cpp|1.59137|Microsoft (R) C/C++ Optimizing Compiler Version 19.22.27905 for x64
even_count_char.cpp|3.46499|gcc version 8.2.0 (MinGW.org GCC-8.2.0-3)
even_count_str.cpp|3.51098|gcc version 8.2.0 (MinGW.org GCC-8.2.0-3)
even_count_no_buffer.cpp|3.96471|gcc version 8.2.0 (MinGW.org GCC-8.2.0-3)
even_count_slow.py|201.852|Python 3.7.2 [MSC v.1916 64 bit (AMD64)] on win32
