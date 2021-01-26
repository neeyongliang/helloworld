cmake_minimum_required(VERSION 2.8)
project(hello_headers)

set(SOURCES
    src/hello.cpp
    src/main.cpp
)

add_executable(hello_headers ${SOURCES})

target_include_directories(hello_headers
    PRIVATE
        ${PROJECT_SOURCE_DIR}/include
)