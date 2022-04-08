# Design system like Robinhood / Zerodha

## Requirements
* User should be able to buy / sell stocks
* User should be able to cancel / schedule his orders
* System should differentiate between multiple lots of same stock bought at different times
* Deposit / Withdraw money

### Entities
* User
* Admin
* Order
  * OrderType
  * buy / sell
  * status
  * Order Parts


### Services
* Register / Cancel Account
* Search Stocks
* Order Service
* Payment Service