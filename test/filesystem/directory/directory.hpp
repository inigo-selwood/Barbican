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

    Directory(const std::string &path, Directory *directory);

    void display(std::ostream &stream,
            const std::string &leader,
            const bool &final,
            const bool &root) const;

};
