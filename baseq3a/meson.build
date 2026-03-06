baseq3a_stage_command = [
  python,
  '-c',
  'import pathlib, shutil, sys; dst = pathlib.Path(sys.argv[2]); dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(sys.argv[1], dst)',
]

baseq3a_qagame_staged = custom_target(
  'stage_baseq3a_qagame',
  input : baseq3a_qagame,
  output : 'qagame' + render_arch_string + game_module_ext,
  command : baseq3a_stage_command + ['@INPUT@', '@OUTPUT@'],
  build_by_default : true,
)

baseq3a_cgame_staged = custom_target(
  'stage_baseq3a_cgame',
  input : baseq3a_cgame,
  output : 'cgame' + render_arch_string + game_module_ext,
  command : baseq3a_stage_command + ['@INPUT@', '@OUTPUT@'],
  build_by_default : true,
)

baseq3a_ui_staged = custom_target(
  'stage_baseq3a_ui',
  input : baseq3a_ui,
  output : 'ui' + render_arch_string + game_module_ext,
  command : baseq3a_stage_command + ['@INPUT@', '@OUTPUT@'],
  build_by_default : true,
)
