#include <ostream>
#include <string>

#include "directory.hpp"

#include "../file/file.hpp"

std::ostream &operator<<(std::ostream &stream, const Directory &directory) {
    directory.display(stream, "", "");
    return stream;
}

void Directory::display(std::ostream &stream,
        const std::string &leader,
        const std::string &starter) const {

    stream << leader << starter << this->name << '\n';

    for(const Directory &directory : this->directories) {
        directory.display(stream, leader, starter);
    }

    for(const File &file : this->files) {
        file.display(stream, leader, starter);
    }
}
