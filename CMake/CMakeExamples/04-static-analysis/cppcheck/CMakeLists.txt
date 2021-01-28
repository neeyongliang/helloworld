cmake_minimum_required(VERSION 2.9)
project(cppcheck_analysis)

set(CMAKE_MODULE_PATH
${CMAKE_SOURCE_DIR}/cmake/modules
${CMAKE_MODULE_PATH})

find_package(CppCheck)

set(ALL_ANALYSIS_TARGETS)

add_subdirectory(subproject1)
add_subdirectory(subproject2)

if (CPPCHECK_FOUND)
    add_custom_target(analysis)
    ADD_DEPENDENCIES(analysis ${ALL_ANALYSIS_TARGETS})
    set_target_properties(analysis PROPERTIES EXCLUDE_FROM_ALL TRUE)
    message("analysis targets are ${ALL_ANALYSIS_TARGETS}")
endif()
