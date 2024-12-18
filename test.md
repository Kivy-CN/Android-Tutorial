/home/hadoop/.cache/briefcase/tools/android_sdk/emulator/emulator "@beePhone" -dns-server 8.8.8.8
INFO    | Android emulator version 35.2.10.0 (build_id 12414864) (CL:N/A)
INFO    | Graphics backend: gfxstream
INFO    | Found systemPath /home/hadoop/.cache/briefcase/tools/android_sdk/system-images/android-31/default/x86_64/
INFO    | Duplicate loglines will be removed, if you wish to see each individual line launch with the -log-nofilter flag.
WARNING | Please update the emulator to one that supports the feature(s): Vulkan
INFO    | Increasing RAM size to 2048MB                                                                                                         
ERROR   | x86_64 emulation currently requires hardware acceleration!
CPU acceleration status: KVM requires a CPU that supports vmx or svm                                                                            
More info on configuring VM acceleration on Linux:                                                                                              
https://developer.android.com/studio/run/emulator-acceleration#vm-linux                                                                         
General information on acceleration: https://developer.android.com/studio/run/emulator-acceleration.      


# Remove existing AVD
avdmanager delete avd -n beePhone

# Download ARM system image
sdkmanager "system-images;android-31;google_apis;armeabi-v7a"

# Create new AVD with ARM image
avdmanager create avd -n beePhone -k "system-images;android-31;google_apis;armeabi-v7a"

# Run emulator with ARM
emulator -avd beePhone -no-accel

export ANDROID_SDK_ROOT="/home/hadoop/.cache/briefcase/tools/android_sdk"
export PATH="$ANDROID_SDK_ROOT/cmdline-tools/12.0/bin:$PATH"

export JAVA_HOME="/home/hadoop/.cache/briefcase/tools/java17"
export PATH="$JAVA_HOME/bin:$PATH"