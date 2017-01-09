# VicBlog with React

Personal blog now rewritten with React, Typescript and Ant-design!

Backend now remains unchanged, and frontend is my priority.


## Run this project

Just type `webpack` since hot reload hasn't been configured yet :( and you need to rebuild every time sources are changed.

Updated Jan 9, 2017:
Now webpack-dev-server is ready, so just run `npm start` to start the server, and the page will reload everytime sources are changed and recompiled.
Hot reload module seems to not working on Windows or WSL, so just auto-refresh is just a compromise :( 

----------

# RTBAW Environment Initialization Guide 

( Updated Jan 9, 2017 )

To initialize a minimal React+Typescript+Babel+Ant-design+Webpack project, go through the followings.

### What will be available?

React, Typescript, Babel,Webpack  and Ant-design components.

And webpack-dev-server and auto-refresh.

**Currently no hot-reload , since I have no idea about node.js and don't want to mess the structure :(**


### Structure
├── dist

│   └── bundle.js

├── index.html  // containing only header and one div element with id **app** to mount the app

├── package.json 

├── README.md

├── src

│   ├── components 

│   ├── index.tsx // App entry.

├── tsconfig.json

└── webpack.config.js

└── server.js

### Requisites

npm

### Steps
- `npm init`
- npm installs
    - `npm install -D @types/node`
    - `npm install -D babel-core`
    - `npm install -D babel-loader`
    - `npm install -D babel-polyfill`
    - `npm install -D babel-preset-es2015`
    - `npm install -D babel-preset-stage-0`
    - `npm install -D rimraf`
    - `npm install -D ts-loader`
    - `npm install -D typescript`
    - `npm install -D webpack`
    - `npm install -D react react-dom @types/react @types/react-dom`
    - `npm install -D style-loader css-loader`
    - `npm install -D babel-plugin-import` : Needed by ant-design to partially import components.
    - `npm install --save antd @types/antd`
    - `npm install -D webpack-dev-server`

- Modifications (IMPORTANT, since I spent too much time on these small but critical things.)

  **You can directly download the files to your project.**

  - server.js
    Simply copy and paste xD

  - tsconfig.json
```
  {
	  "compilerOptions": {
		    "module": "es2015", 
		    "target": "es2015",
		    "noImplicitAny": false,
		    "sourceMap": false,
		    "jsx":"preserve",
		    "moduleResolution": "node",
		    "allowSyntheticDefaultImports": false
		  },
	  "exclude": [
		    "node_modules"
	  ]
}
```
`"module": "es2015",`  Babel-plugin-import needs es6-typed module code form to work properly.

`"jsx":"preserve"`  Preserves es2015 and jsx for babel and babel-plugin-import.

`"allowSyntheticDefaultImports": true` Ignores all errors of *TS1192: Module has no default export.*

  - .babelrc
```
     {
     "presets": ["react","es2015","stage-0"],
     "plugins": [["import",
      {
        "libraryName": "antd",
        "style": "css"
      }]]
     }
```

  - package.json

```
    "scripts": {
         "start": "node server.js"
    },
```

  - webpack.config.js     
    
     Currently `Bash on Windows` has a bug about unimplemented `networkInterfaces()` preventing `css-loader` and `style-loader` from working. 

     The code in the first line by [this](http://m.blog.csdn.net/article/details?id=53021652) solves the problem, but it might slower the compliation.

     So if you are not on`Bash on Windows`, this is NOT NEEDED!

```     
     require('os').networkInterfaces = () => ({});

     module.exports = {
    entry: {
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/dev-server',
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
        test: /\.tsx?$/, loaders: ['babel-loader', 'ts-loader'], exclude: /node_modules/, //ts-loader first
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
```

- Packaging

  Just run `webpack`.
  
- Done

  And start the dev server by `npm start`

### Tested Environment

Bash on Windows (Windows version 14393 and Ubuntu version 16.04)
Windows (version 14393)
  








