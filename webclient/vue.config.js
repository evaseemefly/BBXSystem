// vue.config.js
// const HtmlWebpackPlugin = require('html-webpack-plugin') //通过 npm 安装
const webpack = require('webpack') //访问内置的插件
const path = require('path')

module.exports = {
  // 选项...
  // baseUrl:
  //   process.env.NODE_ENV === 'production' ? '/production-sub-path/' : '/',
  // module: {
  //   loaders: [{}]
  // }
  configureWebpack: {
    plugins: [
      new webpack.ProvidePlugin({
        $: 'jquery',

        jQuery: 'jquery',

        'windows.jQuery': 'jquery'
      })
    ]
  }
}
