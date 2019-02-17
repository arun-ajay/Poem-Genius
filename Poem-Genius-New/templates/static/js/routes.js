import React from 'react';
import { HashRouter, Route, hashHistory } from 'react-router-dom';
import Home from './components/Home';
// import more components
export default (
    <HashRouter history={hashHistory}>
     <div>
      <Route path='/home' component={Home} />
     </div>
    </HashRouter>
);
