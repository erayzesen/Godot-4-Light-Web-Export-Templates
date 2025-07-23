# custom.py - Minimal web export with GDExtension and 2D support for Godot

#Rendering
vulkan = "no"       # Disable Vulkan (not used on web)
module_gdextension_enabled = "yes"  # Enable GDExtension support

#3D
disable_3d = "yes"  # Disable 3D modules
module_gridmap_enabled = "no" # Disable 3d GridMap classes
module_csg_enabled = "no" # Disable Constructive Solid Geometry
module_camera_enabled = "no" # 3D Camera

#GUI and Text
module_text_server_adv_enabled="no" # Advanced text server for not-latin languages.
module_text_server_fb_enabled="yes" # Simple text server
#disable_advanced_gui = "yes" # Advanced GUI Features 

# Disable XR/VR modules
module_openxr_enabled = "no"
module_webxr_enabled = "no"
module_mobile_vr_enabled = "no"

# Disable multiplayer/networking modules
module_multiplayer_enabled = "no"
module_enet_enabled = "no"
module_websocket_enabled = "no"
module_webrtc_enabled = "no"
module_upnp_enabled = "no" #p2p local multiplayer
module_mbedtls_enabled = "no" # SSL/TLS support for the network connections
module_jsonrpc_enabled = "no" # Disables JSON-RPC protocol support.(It's not about native JSON operations)


# File formats
module_jpg_enabled = "no"   # Disable JPG support
module_bmp_enabled = "no"
module_tga_enabled = "no"
module_gltf_enabled = "no"
module_ktx_enabled = "no"
module_tinyexr_enabled = "no"
module_squish_enabled = "no" #S3TC/DXT and RGTC/BCn texture compression format support for 3d graphics
module_hdr_enabled = "no" # HDR image format support
module_dds_enabled = "no" #DirectDraw Surface Image Format 
module_basis_universal_enabled = "no" # *.basis, *.ktx2 image formats 


# Helper Modules
module_regex_enabled = "no" #Regex support
module_vhacd_enabled = "no" # 3d mesh partition operatotions
module_navigation_enabled = "no" # 2D and 3D Navigation classes
module_meshoptimizer_enabled = "no"

#Disable Physics 
module_godot_physics_2d_enabled = "no"
module_godot_physics_3d_enabled = "no"
module_jolt_physics_enabled = "no"
module_raycast_enabled = "no"


# # Compression and archive support
minizip = "no"
module_zip_enabled = "no"

# Disable video/audio codecs not used
module_theora_enabled = "no" #.ogv media
module_vorbis_enabled = "no" #.ogg media




