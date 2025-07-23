This repository contains a custom build configuration for Godot 4 targeting 2D web projects, optimized to achieve the smallest possible web builds size based on my specific needs.

The configuration disables the following features by default: 3D support, multiplayer systems, image formats other than PNG and WebM, built-in 2D and 3D physics engines, XR/VR capabilities, and advanced text rendering. These components are grouped in the configuration file by category, so they can easily be toggled on or off as needed.

GDExtension support is enabled and nothreads mode is active.

**Note :** This is not an experiment in "how far can I push the limits by disabling and sacrificing most features." The goal is to build a configuration that keeps the features actually useful for my 2D web projects. For example, most advanced GUI features are disabled, but some are deliberately kept as exceptions. The custom.py file roughly lists which modules will be disabled. The custom.build file includes more detailed adjustments and exception selections.

In short, if you're making strictly 2D games, plan to use all of Godot's 2D features, won't be building a multiplayer game, and won't rely on Godot's built-in physics, then this configuration might work well for you too.

# Official Sizes ( v4.4):
**template_debug:** 55.5 MB (Zipped: 11.1 MB)
- godot-side wasm file : 53.0 MB

**template_release:** 46.8 MB (Zipped: 10.2 MB)
- godot-side wasm file : 44.3 MB

# Results:
**template_debug:** 33.8 MB (Zipped: 6.5 MB)
 - godot-side wasm file : 28.9 MB

**template_release**: 31.1 MB (Zipped: 6.1 MB)
 - fodot-side wasm file: 26.6 MB

 The results are still not bad compared to the official web builds, but even so, the output is still quite large for the web platform. Hopefully, more work will be done in the future to further reduce the size of Godot 4's web builds.



# How to Use? 
This repository was created for my personal use. However, if you're looking for a similar build configuration — either identical or with a few modifications — feel free to use this project.

Make sure you have all required Godot build dependencies and **Emscripten** properly installed on your system.

Fork the project, then run:
```bash
./build.sh
```



