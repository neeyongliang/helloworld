cmake_minimum_required(VERSION 2.8)

project(hello_cmake)

add_executable(hello_cmake main.cpp)

# if installed clang-9 in system, you can
# mkdir build && cd build
# cmake .. -DCMAKE_C_COMPILER=clang-9 -DCMAKE_CXX_COMPILER=clang++-9 && make
