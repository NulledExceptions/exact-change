from itertools import product
from math import ceil 


class MarketCombos(object):

    def find_combinations(self,total,price_list):
        matches = []


        # Max combinations should be equal to the total amount divided
        # by the lowest cost item and then rounded up to integer.
        ## Multiply by 100 to avoid dividing by a fraction
        max_combinations = ceil(total * 100 / (min(price_list) * 100))

        # Iterate number of item combinations
        for num_items in range(1, max_combinations + 1):

            # Iterate cartesian product of item combinations
            for combination in product(price_list, repeat=num_items):

                # Compare sum of items in combination to total
                ## Check 2 decimals for currency
                if format(sum(combination),'.2f') == format(total,'.2f'):

                    # Check if combination already in match list
                    ## Sort list to avoid duplicates 
                    if sorted(combination) not in matches:
                        matches.append(sorted(combination))
        
        return matches



def main():
    import argparse
    import sys
    import csv

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="filepath", required=True,  help="must include --file /path/to/file.csv")
    args = parser.parse_args()
    
    try:
        csvfile = open(args.filepath,'r')
    except Exception as e:
        print('Error opening file: {}'.format(e) )
        sys.exit(0)

    csv_in = csv.DictReader(csvfile,fieldnames=["name","price"],delimiter=',')

    item_dict = {}

    # Iterate csv
    for index,row in enumerate(csv_in):
        try:
            # Strip dollar sign from price 
            price = float(row['price'].replace('$','')) 
            name = row['name']
        except Exception:
            continue

        if price <= 0:
            continue
        # Set first row as total or append to item dictionary
        if index == 0:
            total = price
        else:
            # If two items have the same price, the names are combined 
            # with 'or' for simplicity
            if price in item_dict:
                item_dict[price] = ' or '.join([item_dict[price], name])
            else:
                item_dict[price] = name

    price_list = item_dict.keys()
    ob = MarketCombos()
    matches = ob.find_combinations(total,price_list)
    


    if not matches:
        print('No combination of dishes are equal to the total price')
    else:
        print('Exact change matches found: {}'.format(len(matches)))
        for exact_match in matches:
            item_names = [item_dict[iprice] for iprice in exact_match]
            print(item_names)


if __name__ == "__main__":
    main()
    