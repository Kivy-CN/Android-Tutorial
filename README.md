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


## 1.3 编程语言的选择

Java 是最流行的编程语言之一，也是 Android 开发所使用的编程语言。
Kotlin 是由 JetBrains 开发的一种基于 JVM 的静态类型编程语言，用于 Android 开发。
从 2017 年 2 月开始，Google 宣布将 Android 开发从 Java 迁移到 Kotlin。
C++ 和 Rust 也是 Android 开发中可以使用的编程语言。
这两者一般用于对内存管理要求较高或者需要执行高性能计算的场景，比如硬件驱动或者游戏开发等领域。

## 1.4 跨平台的挑战

用 Java 或者 Kotlin 开发 Android 应用程序，所写的代码自然就只能用于 Android 操作系统了。
有没有办法能开发一个可以在 Android 操作系统上运行，又可以在其他操作系统上运行的程序呢？

人类社会的大部分问题，都可能有前面的人已经想到过了。
人类社会的很多的问题，也可能有前面的人已经探索过了。

针对跨平台开发，就有很多跨平台开发框架，比如：
* Qt：跨平台高性能图形界面程序开发框架，使用C、C++语言，支持 Windows、Linux、macOS、iOS、Android 操作系统；好处是性能强大，功能丰富；弱势是学习曲线陡峭，体积庞大。
* React Native：跨平台移动应用开发框架，使用 JavaScript，支持 Android 和 iOS 操作系统；好处是确实具有很好的跨平台特性；弱势是性能一般，功能有限，且可能一处编码、处处调试，这也是其他使用 JavaScript 框架的通病。
* Kivy：跨平台移动应用开发框架，使用 Python 语言，支持 Windows、Linux、macOS、iOS、Android 操作系统；好处是使用 Python 上手简单，缺点类似 React Native。
* BeeWare：跨平台移动应用开发框架，使用 Python 语言，支持 Windows、Linux、macOS、iOS、Android 操作系统；好处是使用 Python 简单，缺点是对硬件传感器等方面的支持尚不足。

## 1.5 本次课程的选择

本次课程，分为三个部分。

第一部分体验并使用 Kotlin 编程语言，创建一个最简单的应用程序，初步了解 Android 移动端应用开发。

第二部分使用 Java 编程语言，编译并安装一个基于 TensorFlow Lite 的样例程序，初步体验移动设备上的机器学习和计算机视觉应用。

第三部分，使用 Python 语言，开发一个简单的跨平台移动应用程序，进行文本的变换和简单加密。具体的框架包括[`Briefcase`](https://briefcase.readthedocs.io/)、[`The BeeWare Project`](https://beeware.org/)。


