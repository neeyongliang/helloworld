cmake_minimum_required(VERSION 3.4)

project(StyleDemo)

set(demo main.cpp)

add_subdirectory(src)

add_executable(demo main.cpp)

target_link_libraries(demo LibFunc)