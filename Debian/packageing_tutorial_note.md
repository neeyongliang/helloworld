packaging_tutorial_note
------

镜像下载: https://cdimage.debian.org/cdimage/

打包手册: packing-tutorial.en.pdf

01. 查看deb文件

    `$ ar tv wget_1.12-2.1_i386.deb`

02. 需要的工具

    `build-essentail, devscripts`

03. 一般的打包流程
    
    A. 获取源码

        - 从debian源仓库 -> apt-get source PACKAGE_NAME
        - 从web -> dget
        - 从上游 -> dh_make

    B. 编译源码
        - debuild
        - dpkg-buildpackage

    C. 安装或上传

04. 禁用GPG
    
    编包的时候，加上参数 -us -uc

05. 构建格式
    - all： 全平台使用相同的内容
    - any： 针对不同平台分辨构建

06. 编译依赖
    ```
    apt-get build-dep MY_PACKAGE
    mk-build-deps -ir MY_PACKAGE
    ```

07. Ubuntu也可以使用的工具
    - Package Overview
    - Package Tracking System
    - 通过PTS接受launchpad缺陷邮件

08. quick rebuild

    `$ fackroot debian/rules binary`

    或

    `$ fackroot debian/rules build`

    这种编包方法只能用于测试！
    