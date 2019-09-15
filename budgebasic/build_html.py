import sqlite3

conn = sqlite3.connect("budge.db")
conn.row_factory = sqlite3.Row

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
