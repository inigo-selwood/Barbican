#include <iostream>
#include <filesystem>

#include "filesystem/filesystem.hpp"

int main() {
    Directory root = Directory(std::filesystem::current_path(), nullptr);
    std::cout << root << '\n';
}
