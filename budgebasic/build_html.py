
def wrap_table_element(element):
    """helper method used in transaction_row, ..."""
    if element == None: element = "---"
    return "<td>" + str(element)[0:20] + "</td>"

def wrap_table_row(row, css_class, id):
    """helper method used in transaction_row, ..."""
    return '<tr class="%s table-row" id="%s-%s">' % (css_class, css_class, id) + row + '</tr>'

def transaction_row(transaction):
    """
    """
    transaction_row = '<th><input type="checkbox"></input></th>'
    transaction_row += '<td><img src="https://cdn1.iconfinder.com/data/icons/social-17/48/photos2-512.png" height="32" width="32"></td>'

    for field in ['date', 'description', 'memo', 'outflow', 'inflow']:
        transaction_row += wrap_table_element(transaction[field])
    transaction_row += '<td>&#9658;</td>'  # right facing arrow
    return wrap_table_row(transaction_row, "transaction", transaction['transaction_id'])

# <tr class="transaction table-row" id="transaction_id-1">
#  <th>
# <input type="checkbox"></input>
# </th>
# <td>Aug 31</td>
# <td>
# <img src="https://icon-library.net/images/cabin-512_72443.png" height="32" width="32"> -- :(
# </td>
# <td>Check #952</td>
# <td><em>Gail Hartley</em></td>
#  <td>($952.00)</td>
# <td>--</td>
# <td>&#9658;</td> <!-- right facing arrow -->
#  </tr>


html = '<html><head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="style.css"><title>Transactions | Budge</title></head><body><div style="display: flex"><div class="budget-card" id="budget-card" style="width:30%;"><div class="card" id="my_budget_card"><div class="card-body" style="width: 100%;"><img src="https://icon-library.net/images/avatar-icon/avatar-icon-6.jpg" height="60" width="60"><h5 class="card-title">My Budget</h5><div id="button_box"> <!-- style="display: flex"> --><a href="#" class="btn btn-primary" id="budget_view_button">Budget</a><a href="#" class="btn btn-primary" id="reports_view_button">Reports</a><a href="#" class="btn btn-primary" id="transactions_view_button">Transactions</a><a href="#" class="btn btn-primary" id="categories_view_button">Categories</a><a href="#" class="btn btn-primary" id="account_view_button">My Account</a></div></div></div></div><div class="budget-view" id="budget_view" style="width:70%;"><div class="budget-summary-view" id="budget_summary_view"></div><table class="transaction-table table" id="transaction_table"><thead class="table-nav" id="transaction_table_nav"></thead><tbody class="table-results" id="transaction_table_results">'

import sqlite3

conn = sqlite3.connect("budge.db")
conn.row_factory = sqlite3.Row
c = conn.cursor()
transactions = c.execute("select * from transactions")
for transaction in transactions:
    html += transaction_row(transaction)
html += '</tbody></table></div></div><body></html>'

print(html)
