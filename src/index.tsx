import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Router, Route, hashHistory, IndexRoute,browserHistory } from 'react-router';
import { Master } from './Master';
import { About } from './components/About';
import "./css/main.css";

ReactDOM.render(
    <Router history={hashHistory}>
    <Route path="/" component={Master}>
        <Route path="/about" component={About}/>
    </Route>
    </Router>,
    document.getElementById("app")

);