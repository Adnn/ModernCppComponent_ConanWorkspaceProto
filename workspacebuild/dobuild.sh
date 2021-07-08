#!sh

set -e
set -x

rm -rf build_workspace
mkdir build_workspace

conan workspace install -if build_workspace ws.yml

cmake -S . -B build_workspace
cmake --build build_workspace --config release
