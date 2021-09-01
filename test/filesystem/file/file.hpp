#pragma once

#include <ostream>
#include <string>

class Directory;

class File {

public:

    Directory *directory;

    std::string name;

    friend std::ostream &operator<<(std::ostream &stream, const File &file);

    File(const std::string &file);

    void display(std::ostream &stream,
            const std::string &leader,
            const std::string &starter) const;

};
