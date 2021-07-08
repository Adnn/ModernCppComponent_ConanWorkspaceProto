#project(beta VERSION "${CMAKE_PROJECT_VERSION}")
set(TARGET_NAME beta)

set(${TARGET_NAME}_HEADERS
    Foo.h
    multiply.h
)

# Creates the library target
add_library(${TARGET_NAME} INTERFACE)

add_library(myrepo::${TARGET_NAME} ALIAS ${TARGET_NAME})

# Custom target to show source files in IDEs
add_custom_target(${TARGET_NAME}_ide
                  SOURCES ${${TARGET_NAME}_HEADERS})

# Defines target requirements
target_include_directories(${TARGET_NAME}
    INTERFACE
        "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../>"
        "$<INSTALL_INTERFACE:include/${TARGET_NAME}>")

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
        DESTINATION lib/cmake/${PROJECT_NAME}/${TARGET_NAME})
