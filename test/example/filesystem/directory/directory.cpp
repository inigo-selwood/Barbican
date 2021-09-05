#include <filesystem>
#include <ostream>
#include <string>
#include <vector>

#include "../file/file.hpp"

#include "directory.hpp"

Directory::Directory(const std::string &path, Directory *directory) {
    auto start = path.find_last_of('/');
    if(start == std::string::npos)
        start = 0;
    else
        start = start + 1;
    this->name = path.substr(start, std::string::npos);
    this->directory = directory;

    for(const auto &entry: std::filesystem::directory_iterator(path)) {
        if(entry.is_directory())
            this->directories.push_back(Directory(entry.path(), this));
        else if(entry.is_regular_file())
            this->files.push_back(File(entry.path(), this));
    }
}
