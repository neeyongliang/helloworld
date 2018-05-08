cmake_minimum_required(VERSION 3.6)
project(testProperty C)
set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES main.c)

add_executable(testProperty ${SOURCE_FILES})
# add gtk3 support
# pkg name can run follow command to check
# pkg-config --list-all | grep YOU_WANT_CHECK
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0)
pkg_check_modules(GLIB REQUIRED glib-2.0)

include_directories(${GLIB_INCLUDE_DIRS})
include_directories(${GTK3_INCLUDE_DIRS})

link_directories(${GTK3_LIBRARY_DIRS})

add_definitions(${GTK3_CFLAGS_OTHER})

target_link_libraries(${PROJECT_NAME} ${GLIB_LIBRARIES} ${GTK3_LIBRARIES})