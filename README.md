# Android-Tutorial

A extremly simple guide to try Android Development.


# 1 Android 初步了解

## 1.1 系统架构和应用组件

Android 公司成立于 2003 年，并且于 2005 年被 Google 收购。

时至今日，Android 已经发布了十几个版本了。

Android 操作系统可以简单地划分成四层：

* 系统内核层：基于Linux内核，为各种硬件提供底层驱动，显示、声音、传感器、网络、供电等；
* 系统运行层：Android Dalvik 虚拟机或者 ART 运行环境；各种C/C++库，SQLite库提供数据库支持，OpenGL|ES库提供3D绘图支持，WebKit库提供浏览器内核支持等；
* 应用框架层：Android自带核心应用以及开发者构建应用所以来的各种API；
* 应用软件层：所有从应用市场安装的、开发者开发的各种应用软件。

Android 系统上的应用开发需要用到四大组件：

* Activity：所有程序的活动界面；
* Service：所有程序的后台活动；
* BroadcastReceiver：所有应用接受各处广播消息；
* ContentProvider：所有应用之间的数据共享。

## 1.2 依赖工具和开发环境

Android 应用程序的开发需要依赖以下几个工具:

* JDK，也就是 Java Development Kit，针对 Java 开发人员的软件开发工具包，包含了 Java 的运行环境、工具集合、基础类库等；
* Android SDK，是 Google 提供的 Android 开发工具包，需要引入该工具包才能使用 Android 的 API；
* Android Stuido，专门用于开发 Android 应用程序的集成开发环境。


```text
腾讯： https://mirrors.cloud.tencent.com/AndroidSDK/

阿里： https://mirrors.aliyun.com/android.googlesource.com/
```


大家可以自行在自己电脑上搭建相关环境，也可以直接使用机房所提供的虚拟开发环境。


## 1.3 第一个 Android 项目
