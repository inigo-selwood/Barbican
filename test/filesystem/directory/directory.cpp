#include <string>
#include <vector>
#include <ostream>

#include "../file/file.hpp"

#include "directory.hpp"

Directory::Directory(const std::string &name,
        const std::vector<Directory> &directories,
        const std::vector<File> &files,
        Directory *directory) {

    this->name = name;
    this->directories = directories;
    this->files = files;
    this->directory = directory;
}
