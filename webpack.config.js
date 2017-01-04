require('os').networkInterfaces = () => ({})
module.exports = {
  entry: {
    app:"./src/index.tsx"
  },
  output: {
    path: __dirname,
    filename: './dist/bundle.js',
  },
  resolve: {
    extensions: ["", ".webpack.js", ".web.js", ".ts", ".tsx", ".js",".jsx"],

  },
  module: {
    loaders: [{
      test: /\.tsx?$/, loaders: ['babel-loader', 'ts-loader'], exclude: /node_modules/,
    },{
      test: /\.css$/, // Only .css files
      loader: 'style!css' // Run both loaders
    }]
  },
  externals: {
        "react": "React",
        "react-dom": "ReactDOM"

    },
};
