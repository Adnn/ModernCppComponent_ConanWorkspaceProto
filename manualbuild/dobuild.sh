#!sh

set -e

echo  $(pwd)
echo  $RT

mkdir build_up
cmake -DBoost_ROOT=$BOOST_ROOT -S $RT/up -B build_up
cmake --build build_up --config release
mkdir build_down
cmake -DBoost_ROOT=$BOOST_ROOT -DMyRepository_DIR=$(pwd)/build_up/ -S $RT/down -B build_down
cmake --build build_down --config release
