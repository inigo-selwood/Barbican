#pragma once

#include "error/error.hpp"

class Parse {

private:

    std::vector<Error> errors;

    Parse();

    void print(std::ostream &stream) const;

};
