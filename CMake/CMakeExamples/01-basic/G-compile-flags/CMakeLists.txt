cmake_minimum_required(VERSION 2.8)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DEx2" CACHE STRING "Set C++ Compiler Flags" FORCE)

project(complile_flags)

add_executable(cmake_examples_compile_flags main.cpp)

target_compile_definitions(cmake_examples_compile_flags
    PRIVATE EX3
)