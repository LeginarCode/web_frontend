const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",
  mode: "development",
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
    path: path.resolve(__dirname, "dist/"),
    publicPath: "/dist/",
    filename: "bundle.js"
  },
  devServer: {
    contentBase: path.join(__dirname, "public/"),
    port: 3000,
    publicPath: "http://localhost:3000/dist/",
    watchContentBase: true,
    hotOnly: true,
    open: true,
    historyApiFallback:true,
  },
  plugins: [new webpack.HotModuleReplacementPlugin()]
};