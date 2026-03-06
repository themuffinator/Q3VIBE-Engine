baseq3a_common_c_args = []
if is_windows
  baseq3a_common_c_args += [
    '-DWIN32',
    '-D_CRT_SECURE_NO_WARNINGS',
  ]
elif is_darwin
  baseq3a_common_c_args += [
    '-DID_INLINE=inline',
    '-DPATH_SEP=\'/\'',
  ]
endif

if cc.has_argument('-fno-strict-aliasing')
  baseq3a_common_c_args += ['-fno-strict-aliasing']
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
    'game/q_math.c',
    'game/q_shared.c',
  ),
  include_directories : baseq3a_includes,
  c_args : baseq3a_common_c_args,
  pic : true,
)

baseq3a_common_dep = declare_dependency(
  compile_args : baseq3a_common_c_args,
  include_directories : baseq3a_includes,
  link_with : baseq3a_runtime_common,
)

baseq3a_qagame_sources = files(
  'game/g_main.c',
  'game/ai_chat.c',
  'game/ai_cmd.c',
  'game/ai_dmnet.c',
  'game/ai_dmq3.c',
  'game/ai_main.c',
  'game/ai_team.c',
  'game/ai_vcmd.c',
  'game/bg_lib.c',
  'game/bg_misc.c',
  'game/bg_pmove.c',
  'game/bg_slidemove.c',
  'game/g_active.c',
  'game/g_arenas.c',
  'game/g_bot.c',
  'game/g_client.c',
  'game/g_cmds.c',
  'game/g_combat.c',
  'game/g_items.c',
  'game/g_mem.c',
  'game/g_misc.c',
  'game/g_missile.c',
  'game/g_mover.c',
  'game/g_rotation.c',
  'game/g_session.c',
  'game/g_spawn.c',
  'game/g_svcmds.c',
  'game/g_syscalls.c',
  'game/g_target.c',
  'game/g_team.c',
  'game/g_trigger.c',
  'game/g_utils.c',
  'game/g_unlagged.c',
  'game/g_weapon.c',
)

baseq3a_cgame_sources = files(
  'cgame/cg_main.c',
  'game/bg_lib.c',
  'game/bg_misc.c',
  'game/bg_pmove.c',
  'game/bg_slidemove.c',
  'cgame/cg_consolecmds.c',
  'cgame/cg_draw.c',
  'cgame/cg_drawtools.c',
  'cgame/cg_effects.c',
  'cgame/cg_ents.c',
  'cgame/cg_event.c',
  'cgame/cg_info.c',
  'cgame/cg_localents.c',
  'cgame/cg_marks.c',
  'cgame/cg_players.c',
  'cgame/cg_playerstate.c',
  'cgame/cg_predict.c',
  'cgame/cg_scoreboard.c',
  'cgame/cg_servercmds.c',
  'cgame/cg_snapshot.c',
  'cgame/cg_syscalls.c',
  'cgame/cg_view.c',
  'cgame/cg_weapons.c',
)

baseq3a_ui_sources = files(
  'q3_ui/ui_main.c',
  'game/bg_misc.c',
  'game/bg_lib.c',
  'q3_ui/ui_addbots.c',
  'q3_ui/ui_atoms.c',
  'q3_ui/ui_cdkey.c',
  'q3_ui/ui_cinematics.c',
  'q3_ui/ui_confirm.c',
  'q3_ui/ui_connect.c',
  'q3_ui/ui_controls2.c',
  'q3_ui/ui_credits.c',
  'q3_ui/ui_demo2.c',
  'q3_ui/ui_display.c',
  'q3_ui/ui_gameinfo.c',
  'q3_ui/ui_ingame.c',
  'q3_ui/ui_loadconfig.c',
  'q3_ui/ui_menu.c',
  'q3_ui/ui_mfield.c',
  'q3_ui/ui_mods.c',
  'q3_ui/ui_network.c',
  'q3_ui/ui_options.c',
  'q3_ui/ui_playermodel.c',
  'q3_ui/ui_players.c',
  'q3_ui/ui_playersettings.c',
  'q3_ui/ui_preferences.c',
  'q3_ui/ui_qmenu.c',
  'q3_ui/ui_removebots.c',
  'q3_ui/ui_saveconfig.c',
  'q3_ui/ui_serverinfo.c',
  'q3_ui/ui_servers2.c',
  'q3_ui/ui_setup.c',
  'q3_ui/ui_sound.c',
  'q3_ui/ui_sparena.c',
  'q3_ui/ui_specifyserver.c',
  'q3_ui/ui_splevel.c',
  'q3_ui/ui_sppostgame.c',
  'q3_ui/ui_spskill.c',
  'q3_ui/ui_startserver.c',
  'q3_ui/ui_syscalls.c',
  'q3_ui/ui_team.c',
  'q3_ui/ui_teamorders.c',
  'q3_ui/ui_video.c',
)

baseq3a_link_deps = [baseq3a_common_dep] + baseq3a_module_deps

if is_darwin
  baseq3a_qagame = shared_library(
    'qagame' + render_arch_string,
    baseq3a_qagame_sources,
    include_directories : baseq3a_includes,
    c_args : ['-DQAGAME'],
    dependencies : baseq3a_link_deps,
    gnu_symbol_visibility : 'hidden',
    name_prefix : '',
  )

  baseq3a_cgame = shared_library(
    'cgame' + render_arch_string,
    baseq3a_cgame_sources,
    include_directories : baseq3a_includes,
    c_args : ['-DCGAME'],
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
    dependencies : baseq3a_link_deps,
    gnu_symbol_visibility : 'hidden',
    name_prefix : '',
  )

  baseq3a_cgame = shared_module(
    'cgame' + render_arch_string,
    baseq3a_cgame_sources,
    include_directories : baseq3a_includes,
    c_args : ['-DCGAME'],
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
