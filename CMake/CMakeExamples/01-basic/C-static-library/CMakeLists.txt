cmake_minimum_required(VERSION 2.8)
project(hello_library)

# for static library
add_library(hello_library STATIC
    src/Hello.cpp
)

# link library
target_include_directories(hello_library
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)

# add executable with above source
add_executable(hello_binary
    src/main.cpp
)

target_link_libraries(hello_binary
    PRIVATE
        hello_library
)