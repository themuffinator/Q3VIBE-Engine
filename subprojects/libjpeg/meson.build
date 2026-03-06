project('libjpeg', 'c', version : 'vendored', license : 'IJG')

libjpeg_c_args = []
if host_machine.system() == 'windows'
  libjpeg_c_args += ['-D_CRT_SECURE_NO_WARNINGS']
endif

libjpeg_sources = files(
  'upstream/jaricom.c',
  'upstream/jcapimin.c',
  'upstream/jcapistd.c',
  'upstream/jcarith.c',
  'upstream/jccoefct.c',
  'upstream/jccolor.c',
  'upstream/jcdctmgr.c',
  'upstream/jchuff.c',
  'upstream/jcinit.c',
  'upstream/jcmainct.c',
  'upstream/jcmarker.c',
  'upstream/jcmaster.c',
  'upstream/jcomapi.c',
  'upstream/jcparam.c',
  'upstream/jcprepct.c',
  'upstream/jcsample.c',
  'upstream/jctrans.c',
  'upstream/jdapimin.c',
  'upstream/jdapistd.c',
  'upstream/jdarith.c',
  'upstream/jdatadst.c',
  'upstream/jdatasrc.c',
  'upstream/jdcoefct.c',
  'upstream/jdcolor.c',
  'upstream/jddctmgr.c',
  'upstream/jdhuff.c',
  'upstream/jdinput.c',
  'upstream/jdmainct.c',
  'upstream/jdmarker.c',
  'upstream/jdmaster.c',
  'upstream/jdmerge.c',
  'upstream/jdpostct.c',
  'upstream/jdsample.c',
  'upstream/jdtrans.c',
  'upstream/jerror.c',
  'upstream/jfdctflt.c',
  'upstream/jfdctfst.c',
  'upstream/jfdctint.c',
  'upstream/jidctflt.c',
  'upstream/jidctfst.c',
  'upstream/jidctint.c',
  'upstream/jmemmgr.c',
  'upstream/jmemnobs.c',
  'upstream/jquant1.c',
  'upstream/jquant2.c',
  'upstream/jutils.c',
)

libjpeg_includes = include_directories('upstream')

libjpeg_lib = static_library(
  'q3vibe_vendor_jpeg',
  libjpeg_sources,
  include_directories : libjpeg_includes,
  c_args : libjpeg_c_args,
)

libjpeg_dep = declare_dependency(
  compile_args : ['-DUSE_SYSTEM_JPEG'],
  include_directories : libjpeg_includes,
  link_with : libjpeg_lib,
)
