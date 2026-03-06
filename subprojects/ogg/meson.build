project('libogg', 'c', version : 'vendored', license : 'BSD-3-Clause')

ogg_sources = files(
  'upstream/src/bitwise.c',
  'upstream/src/framing.c',
)

ogg_includes = include_directories('upstream/include')

ogg_lib = static_library(
  'q3vibe_vendor_ogg',
  ogg_sources,
  include_directories : ogg_includes,
)

ogg_dep = declare_dependency(
  include_directories : ogg_includes,
  link_with : ogg_lib,
)
