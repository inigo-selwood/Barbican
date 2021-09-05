#include <string>

#include "file.hpp"

File::File(const std::string &path, Directory *directory) {
    auto start = path.find_last_of('/');
    if(start == std::string::npos)
        start = 0;
    else
        start = start + 1;
    this->name = path.substr(start, std::string::npos);

    this->directory = directory;
}
