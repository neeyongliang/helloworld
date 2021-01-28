cmake_minimum_required(VERSION 2.8)
project(cppcheck_analysis)

# use debug build as recommeded
set(CMAKE_BUILD_TYPE Debug)

# have make create a compile database
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_subdirectory(subproject1)
add_subdirectory(subproject2)