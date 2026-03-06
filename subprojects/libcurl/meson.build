project('libcurl', 'c', version : 'vendored', license : 'curl')

if host_machine.system() != 'windows'
  error('The vendored libcurl wrapper currently supports Windows only.')
endif

if host_machine.cpu_family() != 'x86_64'
  error('The vendored libcurl wrapper currently supports Windows x86_64 only.')
endif

cc = meson.get_compiler('c')
curl_includes = include_directories('upstream/windows/include')
curl_lib_dir = join_paths(meson.current_source_dir(), 'upstream', 'windows', 'vs2017', 'lib64')

curl_lib_name = 'libcurl_a'
if get_option('debug')
  curl_lib_name = 'libcurl_a_debug'
endif

libcurl_dep = declare_dependency(
  include_directories : curl_includes,
  compile_args : [
    '-DCURL_STATICLIB',
  ],
  dependencies : [
    cc.find_library('crypt32', required : true),
  ],
  link_args : [
    join_paths(curl_lib_dir, curl_lib_name + '.lib'),
  ],
)
