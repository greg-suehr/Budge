import React from 'react';
import Row from './Row';

const RowList = ({transactions}) => {
    return (
      <div className="budgetView">
        <table className="table transactionTable" id="transactionTable">
        <thead className="table-nav" id="transactionTableNav"></thead>
        <tbody className="table-results" id="transactionTableResults">
        {
	    transactions.map((transaction) => {
	    return (
	      <Row 
	        key={'transaction-' + transaction.id} // TODO: enumerate and set key = 'transaction-' + i
	        id={transaction.id}
	        date={transaction.date}
	        desc={transaction.desc}
   	        outflow={transaction.outflow}
            inflow={transaction.inflow}
	       />
		    );
	      })
	    }
	    </tbody>
        </table>
      </div>
    );
}

export default RowList;