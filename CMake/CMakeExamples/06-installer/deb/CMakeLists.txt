cmake_minimum_required(VERSION 3.5)

project(cmake_examples_deb)

# set a project version
set (deb_example_VERSION_MAJOR 0)
set (deb_example_VERSION_MINOR 2)
set (deb_example_VERSION_PATCH 2)
set (deb_example_VERSION "${deb_example_VERSION_MAJOR}.${deb_example_VERSION_MINOR}.${deb_example_VERSION_PATCH}")

# create a library
add_library(cmake_examples_deb SHARED src/Hello.cpp)
target_include_directories(cmake_examples_deb
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)

# create an executable
add_executable(cmake_examples_deb_bin src/main.cpp)
target_link_libraries( cmake_examples_deb_bin
    PUBLIC
        cmake_examples_deb
)

# Install
install (TARGETS cmake_examples_deb_bin
    DESTINATION bin)
install (TARGETS cmake_examples_deb
    # uncomment following line for Windows
    # RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib)
install (FILES cmake-examples.conf
    DESTINATION etc)

set(CPACK_GENERATOR "DEB")
set(CPACK_DEBIAN_PACKAGE_MAINTAINER "wikinee")
set(CPACK_PACKAGE_VERSION ${deb_example_VERSION})

include(CPack)
