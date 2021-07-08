#project(alpha VERSION "${CMAKE_PROJECT_VERSION}")
set(TARGET_NAME alpha)

set(${TARGET_NAME}_HEADERS
    accumulate.h
    FooBar.h
    is_directory.h
    sum.h
)

set(${TARGET_NAME}_SOURCES
    accumulate.cpp
    sum.cpp
)

function(local_find)
    set(REQUIRED "REQUIRED")
    set(QUIET "QUIET")
    set(find_package "find_package")
    set(find_internal_package "#Internal component: find_package")
    configure_file(CMakeFinds.cmake.in CMakeFinds.cmake @ONLY)
    include(${CMAKE_CURRENT_BINARY_DIR}/CMakeFinds.cmake)
endfunction()
local_find()

function(config_find)
    set(find_package "find_dependency")
    set(find_internal_package "find_dependency")
    configure_file(CMakeFinds.cmake.in ${PROJECT_BINARY_DIR}/${TARGET_NAME}/${TARGET_NAME}FindUpstream.cmake @ONLY)
endfunction()
config_find()

# Creates the library target
add_library(${TARGET_NAME}
            ${${TARGET_NAME}_HEADERS}
            ${${TARGET_NAME}_SOURCES})

add_library(myrepo::${TARGET_NAME} ALIAS ${TARGET_NAME})

# Defines target requirements
target_include_directories(${TARGET_NAME}
    PUBLIC
        "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../>"
    INTERFACE
        "$<INSTALL_INTERFACE:include/${TARGET_NAME}>")

target_link_libraries(${TARGET_NAME}
    PUBLIC
        Boost::filesystem
        Boost::disable_autolinking
    INTERFACE
        myrepo::beta)

# Defines target properties
set_target_properties(${TARGET_NAME}
    PROPERTIES
        VERSION "${${TARGET_NAME}_VERSION}")

install(TARGETS ${TARGET_NAME} EXPORT ${TARGET_NAME}Targets)
install(FILES ${${TARGET_NAME}_HEADERS}
        DESTINATION include/${TARGET_NAME}/${TARGET_NAME})

# build tree
export(TARGETS ${TARGET_NAME}
       FILE ${PROJECT_BINARY_DIR}/${TARGET_NAME}/${TARGET_NAME}Targets.cmake
       NAMESPACE myrepo::)
configure_file(${PROJECT_SOURCE_DIR}/cmake/PackageConfig.cmake.in
               ${PROJECT_BINARY_DIR}/${TARGET_NAME}/${TARGET_NAME}Config.cmake
               @ONLY)

# install tree
install(EXPORT ${TARGET_NAME}Targets
        FILE ${TARGET_NAME}Targets.cmake
        DESTINATION lib/cmake/${PROJECT_NAME}/${TARGET_NAME}
        NAMESPACE myrepo::)
install(FILES ${PROJECT_BINARY_DIR}/${TARGET_NAME}/${TARGET_NAME}Config.cmake
        ${PROJECT_BINARY_DIR}/${TARGET_NAME}/${TARGET_NAME}FindUpstream.cmake
        DESTINATION lib/cmake/${PROJECT_NAME}/${TARGET_NAME})
