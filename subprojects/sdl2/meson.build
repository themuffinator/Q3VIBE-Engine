project('sdl2', 'c', version : 'vendored', license : 'zlib')

sdl2_includes = include_directories('upstream/include/SDL2')

if host_machine.system() == 'windows'
  sdl2_link_args = []

  if host_machine.cpu_family() == 'x86_64'
    sdl2_link_args += [join_paths(meson.current_source_dir(), 'upstream', 'windows', 'mingw', 'lib64', 'libSDL264.dll.a')]
  elif host_machine.cpu_family() == 'x86'
    sdl2_link_args += [join_paths(meson.current_source_dir(), 'upstream', 'windows', 'mingw', 'lib32', 'libSDL2.dll.a')]
  else
    error('The vendored SDL2 wrapper currently supports x86 and x86_64 Windows only.')
  endif

  sdl2_dep = declare_dependency(
    include_directories : sdl2_includes,
    link_args : sdl2_link_args,
  )
elif host_machine.system() == 'darwin'
  sdl2_dep = declare_dependency(
    include_directories : sdl2_includes,
    link_args : [
      join_paths(meson.current_source_dir(), 'upstream', 'macosx', 'libSDL2-2.0.0.dylib'),
    ],
  )
else
  error('No vendored Linux SDL2 library is bundled. Install the system SDL2 development package.')
endif
