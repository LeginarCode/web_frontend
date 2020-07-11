const path = require('path');
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
  mode: "development",
  devServer: {
    contentBase: path.join(__dirname, 'public/'),
    port: 3000,
    publicPath: "http://localhost:3000/",
    watchContentBase: true,
	hotOnly: true,
    open: true,
    historyApiFallback:true,
	stats: 'errors-only',
  },
});
