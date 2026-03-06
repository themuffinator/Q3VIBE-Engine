baseq3a_common_compile_args = []
if is_windows
  baseq3a_common_compile_args += [
    '-DWIN32',
    '-D_CRT_SECURE_NO_WARNINGS',
  ]
elif is_darwin
  baseq3a_common_compile_args += [
    '-DID_INLINE=inline',
    '-DPATH_SEP=\'/\'',
  ]
endif

if cc.has_argument('-fno-strict-aliasing')
  baseq3a_common_compile_args += ['-fno-strict-aliasing']
endif

baseq3a_module_deps = []
if not is_windows
  m_dep = cc.find_library('m', required : false)
  if m_dep.found()
    baseq3a_module_deps += [m_dep]
  endif
endif

baseq3a_includes = include_directories(
  '.',
  'game',
  'cgame',
  'ui',
  'q3_ui',
)

baseq3a_runtime_common = static_library(
  'q3vibe_baseq3a_common',
  files(
    'game/q_math.cpp',
    'game/q_shared.cpp',
  ),
  include_directories : baseq3a_includes,
  c_args : baseq3a_common_compile_args,
  cpp_args : baseq3a_common_compile_args,
  pic : true,
)

baseq3a_common_dep = declare_dependency(
  compile_args : baseq3a_common_compile_args,
  include_directories : baseq3a_includes,
  link_with : baseq3a_runtime_common,
)

baseq3a_qagame_sources = files(
  'game/g_main.cpp',
  'game/ai_chat.cpp',
  'game/ai_cmd.cpp',
  'game/ai_dmnet.cpp',
  'game/ai_dmq3.cpp',
  'game/ai_main.cpp',
  'game/ai_team.cpp',
  'game/ai_vcmd.cpp',
  'game/bg_lib.cpp',
  'game/bg_misc.cpp',
  'game/bg_pmove.cpp',
  'game/bg_slidemove.cpp',
  'game/g_active.cpp',
  'game/g_arenas.cpp',
  'game/g_bot.cpp',
  'game/g_client.cpp',
  'game/g_cmds.cpp',
  'game/g_combat.cpp',
  'game/g_items.cpp',
  'game/g_mem.cpp',
  'game/g_misc.cpp',
  'game/g_missile.cpp',
  'game/g_mover.cpp',
  'game/g_rotation.cpp',
  'game/g_session.cpp',
  'game/g_spawn.cpp',
  'game/g_svcmds.cpp',
  'game/g_syscalls.cpp',
  'game/g_target.cpp',
  'game/g_team.cpp',
  'game/g_trigger.cpp',
  'game/g_utils.cpp',
  'game/g_unlagged.cpp',
  'game/g_weapon.cpp',
)

baseq3a_cgame_sources = files(
  'cgame/cg_main.cpp',
  'game/bg_lib.cpp',
  'game/bg_misc.cpp',
  'game/bg_pmove.cpp',
  'game/bg_slidemove.cpp',
  'cgame/cg_consolecmds.cpp',
  'cgame/cg_draw.cpp',
  'cgame/cg_drawtools.cpp',
  'cgame/cg_effects.cpp',
  'cgame/cg_ents.cpp',
  'cgame/cg_event.cpp',
  'cgame/cg_info.cpp',
  'cgame/cg_localents.cpp',
  'cgame/cg_marks.cpp',
  'cgame/cg_players.cpp',
  'cgame/cg_playerstate.cpp',
  'cgame/cg_predict.cpp',
  'cgame/cg_scoreboard.cpp',
  'cgame/cg_servercmds.cpp',
  'cgame/cg_snapshot.cpp',
  'cgame/cg_syscalls.cpp',
  'cgame/cg_view.cpp',
  'cgame/cg_weapons.cpp',
)

baseq3a_ui_sources = files(
  'q3_ui/ui_main.cpp',
  'game/bg_misc.cpp',
  'game/bg_lib.cpp',
  'q3_ui/ui_addbots.cpp',
  'q3_ui/ui_atoms.cpp',
  'q3_ui/ui_cdkey.cpp',
  'q3_ui/ui_cinematics.cpp',
  'q3_ui/ui_confirm.cpp',
  'q3_ui/ui_connect.cpp',
  'q3_ui/ui_controls2.cpp',
  'q3_ui/ui_credits.cpp',
  'q3_ui/ui_demo2.cpp',
  'q3_ui/ui_display.cpp',
  'q3_ui/ui_gameinfo.cpp',
  'q3_ui/ui_ingame.cpp',
  'q3_ui/ui_loadconfig.cpp',
  'q3_ui/ui_menu.cpp',
  'q3_ui/ui_mfield.cpp',
  'q3_ui/ui_mods.cpp',
  'q3_ui/ui_network.cpp',
  'q3_ui/ui_options.cpp',
  'q3_ui/ui_playermodel.cpp',
  'q3_ui/ui_players.cpp',
  'q3_ui/ui_playersettings.cpp',
  'q3_ui/ui_preferences.cpp',
  'q3_ui/ui_qmenu.cpp',
  'q3_ui/ui_removebots.cpp',
  'q3_ui/ui_saveconfig.cpp',
  'q3_ui/ui_serverinfo.cpp',
  'q3_ui/ui_servers2.cpp',
  'q3_ui/ui_setup.cpp',
  'q3_ui/ui_sound.cpp',
  'q3_ui/ui_sparena.cpp',
  'q3_ui/ui_specifyserver.cpp',
  'q3_ui/ui_splevel.cpp',
  'q3_ui/ui_sppostgame.cpp',
  'q3_ui/ui_spskill.cpp',
  'q3_ui/ui_startserver.cpp',
  'q3_ui/ui_syscalls.cpp',
  'q3_ui/ui_team.cpp',
  'q3_ui/ui_teamorders.cpp',
  'q3_ui/ui_video.cpp',
)

baseq3a_link_deps = [baseq3a_common_dep] + baseq3a_module_deps

if is_darwin
  baseq3a_qagame = shared_library(
    'qagame' + render_arch_string,
    baseq3a_qagame_sources,
    include_directories : baseq3a_includes,
    c_args : ['-DQAGAME'],
    cpp_args : ['-DQAGAME'],
    dependencies : baseq3a_link_deps,
    gnu_symbol_visibility : 'hidden',
    name_prefix : '',
  )

  baseq3a_cgame = shared_library(
    'cgame' + render_arch_string,
    baseq3a_cgame_sources,
    include_directories : baseq3a_includes,
    c_args : ['-DCGAME'],
    cpp_args : ['-DCGAME'],
    dependencies : baseq3a_link_deps,
    gnu_symbol_visibility : 'hidden',
    name_prefix : '',
  )

  baseq3a_ui = shared_library(
    'ui' + render_arch_string,
    baseq3a_ui_sources,
    include_directories : baseq3a_includes,
    dependencies : baseq3a_link_deps,
    gnu_symbol_visibility : 'hidden',
    name_prefix : '',
  )
else
  baseq3a_qagame = shared_module(
    'qagame' + render_arch_string,
    baseq3a_qagame_sources,
    include_directories : baseq3a_includes,
    c_args : ['-DQAGAME'],
    cpp_args : ['-DQAGAME'],
    dependencies : baseq3a_link_deps,
    gnu_symbol_visibility : 'hidden',
    name_prefix : '',
  )

  baseq3a_cgame = shared_module(
    'cgame' + render_arch_string,
    baseq3a_cgame_sources,
    include_directories : baseq3a_includes,
    c_args : ['-DCGAME'],
    cpp_args : ['-DCGAME'],
    dependencies : baseq3a_link_deps,
    gnu_symbol_visibility : 'hidden',
    name_prefix : '',
  )

  baseq3a_ui = shared_module(
    'ui' + render_arch_string,
    baseq3a_ui_sources,
    include_directories : baseq3a_includes,
    dependencies : baseq3a_link_deps,
    gnu_symbol_visibility : 'hidden',
    name_prefix : '',
  )
endif
