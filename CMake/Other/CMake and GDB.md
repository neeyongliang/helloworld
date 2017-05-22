 CMAKE and GDB
 -----

cmake中有CMAKE_BUILD_TYPE变量,可以的取值是 Debug Release RelWithDebInfo 和 MinSizeRel。

当这个变量值为 Debug 的时候,CMake 会使用变量 CMAKE_CXX_FLAGS_DEBUG 和 CMAKE_C_FLAGS_DEBUG
中的字符串作为编译选项生成 Makefile;

set(CMAKE_BUILD_TYPE "Debug")
SET(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")