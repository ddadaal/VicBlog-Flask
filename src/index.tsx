import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Router, Route, hashHistory, IndexRoute,browserHistory } from 'react-router';
import { Provider } from 'react-redux';
import { About } from './components/About';
import { App } from './containers/App';
import "./assets/css/main.css";

ReactDOM.render(
    <App/>,
    document.getElementById("app")
);