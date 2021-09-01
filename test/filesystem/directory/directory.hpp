#pragma once

#include <string>
#include <vector>
#include <ostream>

class File;

class Directory {

public:

    std::string name;

    std::vector<Directory> directories;

    std::vector<File> files;

    Directory *directory;

    friend std::ostream &operator<<(std::ostream &stream,
            const Directory &directory);

    Directory(const std::string &name,
            const std::vector<Directory> &directories,
            const std::vector<File> &files,
            Directory *directory);

    void display(std::ostream &stream,
            const std::string &leader,
            const std::string &starter) const;

};
