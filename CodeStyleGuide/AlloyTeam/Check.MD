代码规范检测
------
by AlloyTeam Code Guide

原文:[AlloyTeam Code Guide](http://alloyteam.github.io/CodeGuide/#check)

资料:[Google Code Guide](http://alloyteam.github.io/JX/doc/specification/google-javascript.xml)

# sublime3插件
### 安装node包
- jscs: npm install jscs -g

- jshint: npm install jshint -g

- csscomb: npm install csscomb -g

- csslint: npm install csslint -g

### 安装gem包
- scss-lint: gem install scss_lint

- 安装sublime 3 [Package Control](https://packagecontrol.io/installation#st3)

按下 ctrl+\`

```
复制粘贴以下代码 import urllib.request,os,hashlib; h = 'eb2297e1a458f27d836c04bb0cbaf282' + 'd0e7a3098092775ccb37ca9d6b2e4b7d'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

### 安装sublime3插件

按下 ctrl+shift+p，输入'ip'（Install Package),输入以下插件的名字，按顺序逐个进行安装：

- EditorConfig
- Sass
- SublimeLinter
- SublimeLinter-jscs
- SublimeLinter-jshint
- SublimeLinter-csslint
- SublimeLinter-contrib-scss-lint
- JSFormat
- CSScomb


### 插件的配置文件
将以下配置文件分别下载后放入项目根目录下：
- EditorConfig [download](http://alloyteam.github.io/CodeGuide/.editorconfig)
- JSCS [download](http://alloyteam.github.io/CodeGuide/.jscsrc)
- JSHint [download](http://alloyteam.github.io/CodeGuide/.jshintrc)

```
注意：全局变量需要手动加到配置文件的globals属性里，例：
{
    "globals": {
        "ImageHandle": true
    }
}
```

- CSSLint [download](http://alloyteam.github.io/CodeGuide/.csslintrc)
- SCSS-Lint [download](http://alloyteam.github.io/CodeGuide/.scss-lint.yml)


### 编辑器及插件设置

- sublime3 自身

```
Preferences->Setting-User，增加下面两个配置：
    "translate_tabs_to_spaces": true,
    "word_wrap": true
}
```

点击右下角的Spaces->Convert Indentation to Spaces可以将文件中的所有tab转换成空格

- JSFormat

Preferences->Package Settings->JSFormat->Setting-User，[下载](http://alloyteam.github.io/CodeGuide/jsformat_setting_user.json)

配置好后格式化的默认快捷键是 ctrl+alt+f

- SublimeLinter
    - 右键->SublimeLinter->Lint Mode，有4种检查模式，建议选择 Load/save
    - 右键->SublimeLinter->Mark Style，建议选择 Outline
    - 右键->SublimeLinter->Choose Gutter Theme，建议选择 Blueberry-round
    - 右键->SublimeLinter->Open User Settings，将linter里面jscs的args改成 ["--verbose"]，将linter里面csslint的ignore改成 "box-model,adjoining-classes,box-sizing,compatible-vendor-prefixes,gradients,text-indent,fallback-colors,star-property-hack,underscore-property-hack,bulletproof-font-face,font-faces,import,regex-selectors,universal-selector,unqualified-attributes,overqualified-elements,duplicate-background-images,floats,font-sizes,ids,important,outline-none,qualified-headings,unique-headings"

当光标处于有错误的代码行时，详细的错误信息会显示在下面的状态栏中
右键->SublimeLinter可以看到所有的快捷键，其中 ctrl+k, a 可以列出所有错误

- CSScomb

Preferences->Package Settings->CSScomb->Setting-User，[下载](http://alloyteam.github.io/CodeGuide/csscomb_setting_user.json)
配置好后格式化的默认快捷键是 ctrl+shift+c

------

# grunt插件
在项目中安装grunt插件:
- jscs npm install grunt-jscs --save-dev
- jshint npm install grunt-contrib-jshint --save-dev
- csslint npm install grunt-contrib-csslint --save-dev
- scss-lint npm install grunt-scss-lint --save-dev

插件的配置:

```
JSCS{

    options: {
        config: true,
        verbose: true
    },
    files: {
        src: [...]
    }
}

JSHint {
    options: {
        jshintrc: true
    },
    files: {
        src: [...]
    }
}

CSSLint {
    options: {
        csslintrc: '.csslintrc'
    },
    files: {
        src: [...]
    }
}

SCSS-Lint {
    options: {
        config: '.scss-lint.yml'
    },
    files: {
        src: [...]
    }
}
```
