import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Router, Route, hashHistory, IndexRoute, browserHistory } from 'react-router';
import { Master } from './Master';
import { About } from '../components/About';
import { ArticleList, ArticlePage } from '../components/Article';
import "../assets/css/main.css";


export class App extends React.Component<undefined, undefined>{
    render() {
        return <Router history={hashHistory}>
            <Route path="/" component={Master}>
                <Route path="about" component={About} />
                <Route path="articles" >
                    <IndexRoute component={ArticleList} />
                    <Route path=":ID" component={ArticlePage} />
                </Route>
            </Route>
        </Router>;
    }
}