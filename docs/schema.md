# Budge Schema


### transactions


### tags

Tags are a way to organize and report on transactions within a budget.


### transaction_tags

A transaction can be associated with many tags.


### categories

A category is a "special" tag. Each transaction can only be associated with a
single category-tag within a pay_period (within a budget?).

Mapping transactions to a single category-tag simplifies the building of tables
and charts. Odd transactions can be mapped by default to the uncategorized tag.

A standard budget groups transactions by monthly pay_periods with category-tags
like (bills, savings, loans, spending). 

Many tags will fit neatly in a single category-tag, but could span across
category-tags. For example:
  - bills {rent, electric, water, car}
  - savings {}
  - loans {}
  - spending {groceries, fastfood, books, booze, car}
  - `uncategorized` {car}


### pay_periods

Pay periods are another way to organize and report on  transacionts

The standard pay period is a month of transactions. You can also use pay periods
to group transactions for a project or client.


### transaction_pay_periods

A transaction can belong to many pay periods.


### budgets

A pay period belongs to a single budget.


### imports

An import represents an influx of transaction to a budget and are associated with
an account.


### accounts

  > How do accounts overlap with pay_periods for the per-client use case?


### budget_accounts


### users


### user_accounts

  > Confusing bridge table name from ambiguous `accounts` table name.