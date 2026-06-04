[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.test
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.sdk_path =
android.ndk_path =
android.archs = arm64-v8a,armeabi-v7a
android.debug = 1
