#include <ostream>
#include <string>

#include "directory.hpp"

#include "../file/file.hpp"

std::ostream &operator<<(std::ostream &stream, const Directory &directory) {
    directory.display(stream, "", true, true);
    return stream;
}

void Directory::display(std::ostream &stream,
        const std::string &leader,
        const bool &final,
        const bool &root) const {

    std::string starter = "";
    if(root == false) {
        if(final)
            starter = "╰─ ";
        else
            starter = "├─ ";
    }

    stream << leader << starter << this->name << '\n';

    std::string new_leader = "";
    if(root == false) {
        if(final)
            new_leader = leader + "   ";
        else
            new_leader = leader + "│  ";
    }

    int index = 0;
    int count = this->files.size() + this->directories.size();
    for(const auto &directory : this->directories) {
        bool final_directory = (index + 1) == count;
        directory.display(stream, new_leader, final_directory, false);
        index += 1;
    }

    for(const auto &file : this->files) {
        bool final_file = (index + 1) == count;
        file.display(stream, new_leader, final_file);
        index += 1;
    }
}
