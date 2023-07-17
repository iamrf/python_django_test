import csv
import json
import redis

def update_price_data():
    print("Updating price data...")

    redis_client = redis.Redis(host='redis', port=6379, db=0)

    with open('price_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            time = row['Time']
            stock = row['Stock']
            price = row['Price']

            # Print current row data
            print(f"Processing: Time={time}, Stock={stock}, Price={price}")

            # Retrieve existing stock data from Redis
            stock_data_str = redis_client.get(stock)
            if stock_data_str:
                stock_data = json.loads(stock_data_str.decode('utf-8'))
            else:
                # If no existing data, initialize with default values
                stock_data = {
                    'id': 0,
                    'price': [],
                    'time': [],
                    'performance': 0,
                }

            # Update time and price history
            stock_data['time'].append(time)
            stock_data['price'].append(price)

            # Save the updated stock data in Redis
            try:
                redis_client.set(stock, json.dumps(stock_data))
                print('Saved successfuly !!!!!!!!')
            except:
                print('Error on saving !!!!!!!!')

            # Print the updated data
            print(f"Updated data for Stock={stock}: {stock_data}")

    print("Price data update completed.")

if __name__ == '__main__':
    update_price_data()
