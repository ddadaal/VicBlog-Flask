import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { About } from './components/About';
import { AppContainer } from 'react-hot-loader';
import { Routes } from './Routes';
import { Router, hashHistory, browserHistory} from 'react-router';
import "./assets/css/main.css";


const content = (<Router history={browserHistory} routes={Routes}/>);

const renderRoot = ()=>{
    ReactDOM.render(<AppContainer>{content}</AppContainer>,document.getElementById("app"));
};
renderRoot();

if ((module as any).hot) {
  console.log("call");
  (module as any).hot.accept('./Routes',renderRoot);
}