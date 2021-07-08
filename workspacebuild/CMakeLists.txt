cmake_minimum_required(VERSION 3.15)

project(WorkspaceBuild)

include(${CMAKE_BINARY_DIR}/conanworkspace.cmake)
conan_workspace_subdirectories()
