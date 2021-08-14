#pragma once

#include <ostream>

class Error {

public:

    Error();

    void print(std::ostream &stream) const;

private:

    std::string message;

};
