import React, { Component } from 'react';
import RowList from '../components/RowList';
import Sidecard from '../components/SideCard';

class App extends Component {
  constructor ({transactions}) {
  	super()
  	this.state = {
  		transactions: transactions
  }
}

  render () {
  	const { transactions } = this.state;

  	return (
  		<div>
  		  <Sidecard/>
  		  <RowList transactions={transactions}/>
  		</div>
  	);
  }
}

export default App;