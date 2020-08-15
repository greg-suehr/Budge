const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

app.listen(3001, () => {
	console.log('app is running on port 3001');
})

var test_database = {
	transactions: [
  {
    id: 1,
    date: '06/28/2019',
    desc: 'POS PURCHASE          POS61007500  1124221 GIANT-EAGLE #0           PITTSBURGH   PA',
    memo: '',
    payee: '',
    outflow: 18.01,
    inflow: 0.00
  },
  {
    id: 2,
    date: '06/28/2019',
    desc: 'DEBIT CARD PURCHASE   XXXXX6868 PPAP FIRST AVENUE 212     PITTSBURGH  PA',
    memo: '',
    payee: '',    
    outflow: 12.00,
    inflow: 0.00
  },
  {
    id: 3,
    date: '06/29/2019',
    desc: 'ACH CREDIT      XXXXX5139R32 GRANT STREET GRO DIRECT DEP',
    memo: '',
    payee: '',
    outflow: 0.00,
    inflow: 2106.62
  }]
}

app.get('/', (request, resp) => {
	resp.status(200).json("hi");
})

app.get('/view', (request, resp) => {
	// TODO: grab a single user's transactions
	resp.status(200).json(test_database.transactions);
})

app.post('/add', (request, resp) => {
	const { date, desc, memo, payee, outflow, inflow } = request.body;

	// calculate the next transaction id on the fly 
	var old_count = test_database.transactions.length;
	var next_id = test_database.transactions[old_count - 1].id + 1

	test_database.transactions.push(
	  { 
	  	id: next_id,
	  	date: date,
	  	desc: desc,
	  	memo: memo,
	  	payee: payee,
	  	outflow: outflow,
	  	inflow: inflow
	  }
	);

	if (test_database.transactions.length > old_count) {
		resp.status(200).json(test_database.transactions);
	} else {
		resp.status(400).json('error adding transaction');
	}
})


app.post('/edit/:id', (request, resp) => {
	const { id } = request.params;
	const { date, desc, memo, payee, outflow, inflow } = request.body;
	let found = false;

	test_database.transactions.forEach(txn => {
		if (txn.id == id) {
			if (date) { txn.date = date; }
			if (desc) { txn.desc = desc; }
			if (memo) { txn.memo = memo; }
			if (payee) { txn.payee = payee; }
			if (outflow || outflow === 0.00) { txn.outflow = outflow; }
			if (inflow || inflow === 0.00) { txn.inflow = inflow; }

			found = true;
			return resp.status(200).json(test_database.transactions)
		}
	})
	if (!found) { return resp.status(400).json("no transction with id = " + id) }
})

/*
/ --> res = connected
/view     --> GET = all transactions
/view/123 --> GET = all transactions matching '123'
/add      --> POST = transaction
/edit/{id}--> POST = transaction
*/