#pragma once

#include <ostream>
#include <string>

class Directory;

class File {

public:

    Directory *directory;

    std::string name;

    friend std::ostream &operator<<(std::ostream &stream, const File &file);

    File(const std::string &path, Directory *directory);

    void display(std::ostream &stream,
            const std::string &leader,
            const bool &final) const;

};
