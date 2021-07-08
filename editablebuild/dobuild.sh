#!sh

set -e

# Layout file had to use undocumented entry
# see: https://github.com/conan-io/conan/issues/9231
conan editable add --layout=layout.ini ${RT}/up/conan myrepository/0.0.0
mkdir build_down
conan install -if build_down ${RT}/down/conan
conan build -sf ${RT}/down -if build_down -bf build_down ${RT}/down/conan

conan editable remove myrepository/0.0.0
