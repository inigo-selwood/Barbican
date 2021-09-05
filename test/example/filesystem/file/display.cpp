#include <ostream>
#include <string>

#include "file.hpp"

std::ostream &operator<<(std::ostream &stream, const File &file) {
    file.display(stream, "", false);
    return stream;
}

void File::display(std::ostream &stream,
        const std::string &leader,
        const bool &final) const {

    std::string starter = "";
    if(final)
        starter = "╰─ ";
    else
        starter = "├─ ";

    stream << leader << starter << this->name << '\n';
}
