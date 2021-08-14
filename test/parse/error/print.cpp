#include "error.hpp"

void Error::print(std::ostream &stream) const {
    stream << this->message;
}
