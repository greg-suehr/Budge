import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css'
import './index.css';
// import RowList from './components/RowList';
// import Sidebar from './components/Sidebar';
import App from './containers/App';
import * as serviceWorker from './serviceWorker';

// test data
import { transactions } from './transactions';

ReactDOM.render(
  <App transactions={transactions}/>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
