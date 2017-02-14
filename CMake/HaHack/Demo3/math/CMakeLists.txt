cmake_minimum_required(VERSION 3.2)
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
# aux_source_directory(. DIR_LIB_SRCS)
set(DIR_LIB_SRCS MainFunc.h MainFunc.c)
# 生成链接库
add_library (MathFunctions ${DIR_LIB_SRCS})