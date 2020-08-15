import React, { Component } from 'react';
import Scroll from '../components/Scroll';
import RowList from '../components/RowList';
import Sidecard from '../components/SideCard';

class App extends Component {
  constructor ({transactions}) {
  	super()
  	this.state = {
  		transactions: transactions
    }
  }

  onRouteChange = (route) => {
    if (route === 'view') {
      this.setState({transactions: [{id:1, date:"test", desc:"test", memo:"test", payee:"test", outflow:"0.00", inflow:"0.00"}]})
    }
  }

  render () {
  	const { transactions } = this.state;

  	return (
  		<div>
  		  <Sidecard onRouteChange={this.onRouteChange}/>
        <Scroll>
  		    <RowList transactions={transactions}/>
        </Scroll>
  		</div>
  	);
  }
}

export default App;