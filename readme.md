This repository contains a custom build configuration for Godot 4 targeting 2D web projects, optimized to achieve the smallest possible web builds size based on my specific needs.

The configuration disables the following features by default: 3D support, multiplayer systems, image formats other than PNG and WebM, built-in 2D and 3D physics engines, XR/VR capabilities, and advanced text rendering. These components are grouped in the configuration file by category, so they can easily be toggled on or off as needed.

GDExtension support is enabled and nothreads mode is active.

# Official Godot 4 build WASM file sizes ( v4.4):
**template_debug:** 55.5 MB (Zipped: 11.1 MB)
- godot-side wasm file : 53.0 MB

**template_release:** 46.8 MB (Zipped: 10.2 MB)
- godot-side wasm file : 44.3 MB

# Results:
**template_debug:** 33.8 MB (Zipped: 6.5 MB)
 - godot-side wasm file : 28.9 MB

**template_release**: 31.1 MB (Zipped: 6.1 MB)
 - fodot-side wasm file: 26.6 MB



# How to Use? 
This repository was created for my personal use. However, if you're looking for a similar build configuration — either identical or with a few modifications — feel free to use this project.

Make sure you have all required Godot build dependencies and **Emscripten** properly installed on your system.

Fork the project, then run:
```bash
./build.sh
```

