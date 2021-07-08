from conans import ConanFile, CMake, tools

from os import path


class DownConan(ConanFile):
    # Recipe meta-information
    name = "down"
    license = "MIT"
    url = "https://github.com/Adnn/ModernCppComponent_codecheck"
    description = "A Conan recipe for {Sonat} code-check repository"
    topics = ("demonstration")

    # Which generators are run when obtaining the code dependencies
    generators = "cmake_paths", "cmake"

    # The default "hash" mode would result in different recipe revisions for Linux and Windows
    # because of difference in line endings
    revision_mode = "scm"

    # (overridable) defaults for consumers
    build_policy = "missing"

    # Package variability:
    # Changing those values will result in distinct packages for the same recipe
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "build_tests": [True, False],
    }
    default_options = {
        "shared": False,
        "build_tests": False,
    }

    # Code dependencies
    requires = "myrepository/0.0.0",

    # Build dependencies
    #   CMake will not need to be installed system-wide to build the project
    #   And if it was installed in a non-compatible version, this line will take precedence
    build_requires = "cmake/3.15.7"


    # Build procedure: code retrieval
    #   Git's repository origin remote and its current revision are captured by recipe export
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto",
        "submodule": "recursive",
    }

    def _generate_cmake_configfile(self):
        with open("cmakeuserconfig.cmake", "w") as outfile:
            # not using path.join because on Windows it uses '\', which starts an escape sequence
            outfile.write("include(\"{}\")\n".format("conan/customconan.cmake"))
            outfile.write("set({} {})\n".format(
                "BUILD_tests",
                self.options.build_tests))


    # shared CMake configuration
    def _configure_cmake(self):
        cmake = CMake(self)
        #cmake.definitions["CMAKE_PROJECT_Down_INCLUDE"] = \
        #    path.join(self.source_folder, "conan", "customconan.cmake")
        #cmake.definitions["BUILD_tests"] = self.options.build_tests
        cmake.configure()
        return cmake


    def generate(self):
        self._generate_cmake_configfile()


    # Build procedure: actual build
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()


    # Packaging procedure
    def package(self):
        cmake = self._configure_cmake()
        cmake.install()


    # Package-consumer instructions
    def package_info(self):
        pass
