#include "parse.hpp"

#include "error/error.hpp"

void Parse::print(std::ostream &stream) const {
    for(const Error &error : this->errors)
        error.print(stream);
}
