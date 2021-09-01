#include <ostream>
#include <string>

#include "file.hpp"

std::ostream &operator<<(std::ostream &stream, const File &file) {
    file.display(stream, "", "");
    return stream;
}

void File::display(std::ostream &stream,
        const std::string &leader,
        const std::string &starter) const {

    stream << leader << starter << this->name << '\n';
}
