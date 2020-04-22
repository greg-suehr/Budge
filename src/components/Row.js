import React from 'react';

const Row = ({ id, date, desc, outflow, inflow }) => {
	return (
	  <tr className='table-row transaction' id={'transaction-' + id}>
        <th>  &#9658; </th>
        <td> {date} </td>
        <td> {desc} </td>
        <td> {outflow} </td>
        <td> {inflow} </td>
        <td> &#9658; </td>  
      </tr>
		);
}

export default Row;