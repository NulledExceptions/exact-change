# exact-change

exact-change determines whether a list of menu items can sum up to the total amount of money provided.  

## Getting Started

### Prerequisites

python3.6+


### Usage
Can be imported as class or called directly passing csv file with flag -f 
```
python3 exact_change.py [-h] -f /path/to/file.csv
```

## Additional notes

Menu items can be ordered more than once.  If two items have the same price, the output will show "a or b" to remove unncessary duplication

To find matches, every item combination(cartesian product) is summed and checked against the total.  The number of combinations is equal to the total amount / divided by the lowest price item.

This could be optimized by removing duplicate checks and continuing if partial sum is greater than total.  As number of items N increases or the price amounts become small, this may become an issue. 


