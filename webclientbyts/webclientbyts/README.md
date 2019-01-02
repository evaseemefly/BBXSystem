# webclientbyts

## 项目参与者：

- [casablanca(evaseemefly)](https://github.com/evaseemefly)
- [stupidanimal(zhiwen)](https://github.com/stupidanimal)

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Run your tests

```
npm run test
```

### Lints and fixes files

```
npm run lint
```

## 项目概述

引入 typescript，准备重写 webclient 项目

## 项目目录介绍

- public 是 vue-cli3 约定的不参与打包的文件夹，编译时会直接复制到 dist 目录下。
- src 是源码文件夹。业务逻辑。
  - api 前后端的接口的封装文件。
  - common 一些公共的 ts 文件。
  - mixins 放置混合选项的文件。具体来说，相当于是公用函数的集合，在组件中引用时，可以作用于组件而不必书写重复的方法。
  - store vuex 状态管理文件。
  - views 所有的业务逻辑视图页面。
- dist 是 build 后生成的可发布文件

## 部分参考的文章汇总：

vue+ts 的脚手架搭建文章：

- 《vue + typescript 项目起手式》(https://github.com/kaorun343/vue-property-decorator)
- 《vue + typescript 进阶篇》(https://segmentfault.com/a/1190000011878086)
- 《almost 最好的 Vue + Typescript 系列 02 项目结构篇》(https://segmentfault.com/a/1190000013676789)

装饰器模式的介绍文章：

- 《ES7 Decorator 装饰者模式 》
  (http://taobaofed.org/blog/2015/11/16/es7-decorator/)
- 《设计模式——装饰模式（Decorator）》
  (https://blog.csdn.net/zhshulin/article/details/38665187)

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).
