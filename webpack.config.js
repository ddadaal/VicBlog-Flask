//require('os').networkInterfaces = () => ({});
var webpack = require("webpack");
module.exports = {
  entry: [
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/dev-server',
    'react-hot-loader/patch',
    './src/index.tsx'
  ],
  output: {
    path: __dirname,
    filename: './dist/bundle.js',
  },
  resolve: {
    extensions: ["", ".webpack.js", ".web.js", ".ts", ".tsx", ".js", ".jsx", "css"],

  },
  module: {
    loaders: [{
      test: /\.tsx?$/, loaders: ['babel-loader', 'awesome-typescript-loader'], exclude: /node_modules/,
    },{
      test: /\.css$/, // Only .css files
      loader: 'style!css' // Run both loaders
    }, {
      test: /\.(png|jpg)$/,
      loader: 'url?limit=25000'
    }
      , {
      test: /\.json$/,
      loader: 'json'
    }]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ],
  externals: {
    "react": "React",
    "react-dom": "ReactDOM"

  },
};
