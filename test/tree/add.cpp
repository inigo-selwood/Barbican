#include "tree.cpp"

#include "../parse/parse.hpp"

void Tree::add(const std::string &directory) {
    this->directories.add(directory);
}
