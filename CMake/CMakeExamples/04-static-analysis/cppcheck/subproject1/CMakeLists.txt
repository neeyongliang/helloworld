project(subprojec1)
set(SOURCES main1.cpp)

include(${CMAKE_SOURCE_DIR}/cmake/analysis.cmake)
add_analysis(${PROJECT_NAME} SOURCES)

add_executable(${PROJECT_NAME} ${SOURCE})