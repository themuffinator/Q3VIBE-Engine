project('libvorbis', 'c', version : 'vendored', license : 'BSD-3-Clause')

ogg_dep = dependency('ogg', fallback : ['ogg', 'ogg_dep'], required : true)

vorbis_sources = files(
  'upstream/lib/analysis.c',
  'upstream/lib/bitrate.c',
  'upstream/lib/block.c',
  'upstream/lib/codebook.c',
  'upstream/lib/envelope.c',
  'upstream/lib/floor0.c',
  'upstream/lib/floor1.c',
  'upstream/lib/info.c',
  'upstream/lib/lookup.c',
  'upstream/lib/lpc.c',
  'upstream/lib/lsp.c',
  'upstream/lib/mapping0.c',
  'upstream/lib/mdct.c',
  'upstream/lib/psy.c',
  'upstream/lib/registry.c',
  'upstream/lib/res0.c',
  'upstream/lib/sharedbook.c',
  'upstream/lib/smallft.c',
  'upstream/lib/synthesis.c',
  'upstream/lib/vorbisfile.c',
  'upstream/lib/window.c',
)

vorbis_includes = include_directories(
  'upstream/include',
  'upstream/lib',
)

vorbis_lib = static_library(
  'q3vibe_vendor_vorbis',
  vorbis_sources,
  include_directories : vorbis_includes,
  dependencies : [ogg_dep],
)

vorbis_dep = declare_dependency(
  include_directories : vorbis_includes,
  dependencies : [ogg_dep],
  link_with : vorbis_lib,
)

vorbisfile_dep = vorbis_dep
