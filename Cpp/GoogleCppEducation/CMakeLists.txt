cmake_minimum_required(VERSION 2.8)

set(CMAKE_BUILD_TYPE "Debug")
SET(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

project(GoogleCppEducation)

set(EXAMPLE_LIST example09.cpp)

add_executable(Demo ${EXAMPLE_LIST})