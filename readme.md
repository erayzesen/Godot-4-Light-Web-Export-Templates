This repository contains a custom build configuration for Godot 4 targeting 2D web projects, optimized to achieve the smallest possible web builds size based on my specific needs.

The configuration disables the following features by default: 3D support, multiplayer systems, image formats other than PNG and WebM, built-in 2D and 3D physics engines, XR/VR capabilities, and advanced text rendering. These components are grouped in the configuration file by category, so they can easily be toggled on or off as needed.

GDExtension support is enabled, advanced GUI support is enabled, and nothreads mode is active.

# Official Godot 4 build sizes ( v4.4):
Debug: 55.5 MB (Zipped: 11.1 MB)

Release: 46.8 MB (Zipped: 10.2 MB)

# Results:
Debug: 33.2 MB (Zipped: 7.2 MB)

Release: 30.8 MB (Zipped: 6.9 MB)

# Project-Specific Additional Optimization:
Keep in mind that this configuration is a general-purpose setup tailored for my own projects. Modules that might be used in my 2D projects have not been disabled.

However, you can further reduce the build size by using Godot’s built-in tool:
**Editor** → **Tools** → **Engine Compilation Configuration Editor**. 

This tool can automatically detect which modules are actually used in your project. If you save the result as custom.build in your project directory, it will be included in the build process and lead to an even smaller export template.

In some of my project-specific builds, I have managed to reduce the size down to approximately 5 MB(zipped).



# How to Use? 
This repository was created for my personal use. However, if you're looking for a similar build configuration — either identical or with a few modifications — feel free to use this project.

Make sure you have all required Godot build dependencies and **Emscripten** properly installed on your system.

Fork the project, then run:
```bash
./build.sh
```

