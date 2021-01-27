cmake_minimum_required(VERSION 2.8)
project(cmake_examples_install)

# create library
add_library(cmake_examples_inst SHARED
    src/Hello.cpp
)

target_include_directories(cmake_examples_inst
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)

# create executable
add_executable(cmake_examples_inst_bin
    src/main.cpp
)

target_link_libraries(cmake_examples_inst_bin
    PRIVATE
        cmake_examples_inst
)

# installing
install(TARGETS cmake_examples_inst_bin
    DESTINATION bin)

install(TARGETS cmake_examples_inst
    # in windows may add follow comment line
    # RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib)

install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/
    DESTINATION include)

install(FILES cmake-examples.conf
    DESTINATION etc)

# test install
# make install DESTDIR=/tmp/stage

# delete installed files
# sudo xargs rm < install_manifest.txt