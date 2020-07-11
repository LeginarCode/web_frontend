const path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');

module.exports = {
  entry: "./src/index.js",
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        loader: "babel-loader",
        options: { presets: ["@babel/env"] }
      },
      {
        test: /\.css$/i,
        use: [
          { loader: 'style-loader' },
          { loader: 'css-loader' },
        ]
      },
      {
        test: /\.scss$/i,
        use:[
          {loader: 'style-loader'},
          {loader: 'css-loader' },
          {loader: 'sass-loader' },
        ]
      },
      {
          test:/\.(png|jpe?g|gif)$/i,
          use: [
              {
                  loader: 'file-loader',
              },
          ],
      },
    ]
  },
  resolve: { extensions: ["*", ".js", ".jsx"] },
  output: {
    path: path.resolve(__dirname, "dist"),
	publicPath: '/dist/',
    filename: "bundle.js"
  },
  plugins: [
	new webpack.HotModuleReplacementPlugin(),
	 new CleanWebpackPlugin(),
	new HtmlWebpackPlugin({
		title: 'Production',
	}),
  ],
};
