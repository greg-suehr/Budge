import React from 'react';

const SideCard = (props) => {
  return (
       <div className='sidecard' id='sidecard'>
        <div className='card'>
          <div className='card-body'>
            <img src='https://icon-library.net/images/avatar-icon/avatar-icon-6.jpg' height='60' width='60'/>
            <h5 className='card-title'>My Budget</h5>
            <div className='buttonBox' id='button_box'>
              <a href='#' className='btn btn-primary' id='budget_view_button' name='budget_view_button'>Budget</a>
              <a href='#' className='btn btn-primary' id='reports_view_button' name='reports_view_button'>Reports</a>
              <a href='#' className='btn btn-primary' id='transactions_view_button' name='transactions_view_button'>Transactions</a>
              <a href='#' className='btn btn-primary' id='categories_view_button' name='categories_view_button'>Categories</a>
              <a href='#' className='btn btn-primary' id='account_view_button' name='account_view_button'>My Account</a>
            </div>
          </div>
        </div>
      </div> 
    );
}

export default SideCard;