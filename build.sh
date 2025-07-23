 emcc --clear-cache

cd godot

scons -c

#DEFAULT WEB TEMPLATE OPTION: no threads, dlink_enabled
# scons platform=web target=template_debug dlink_enabled=yes threads=no  #debug
# scons platform=web target=template_release dlink_enabled=yes threads=no  production=yes #release

#LIGHTWEIGHT WEB TEMPLATE OPTION: no threads, dlink_enabled
scons platform=web profile=../custom.py build_profile=../custom.build target=template_debug  threads=no dlink_enabled=yes   #debug
scons platform=web profile=../custom.py build_profile=../custom.build target=template_release threads=no dlink_enabled=yes  production=yes lto=full debug_symbols=no #release


#scons platform=web target=template_release build_profile=../custom.build use_llvm=yes use_lto=yes threads=no -j4 

cd ..

rm -rf web_export_template

mv godot/bin web_export_template