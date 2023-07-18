import csv
import json
import time
import redis
import random

def calculate_performance(stock_price):
	time.sleep(3)
	return random.randint(1,99)

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
                # If no existing data, initialize a empty dict object
                stock_data = {}

            # Update time and price history
            if 'time' in stock_data:
                stock_data['time'].append(time)
                stock_data['price'].append(price)
            else:
                stock_data['time'] = [time]
                stock_data['price'] = [price]
                
            # Check if the price has changed
            if 'last_price' in stock_data and stock_data['last_price'] == price:
                # Price hasn't changed, skip performance calculation
                continue

            # Calculate performance metric
            performance = calculate_performance(price)

            # Save the performance value and last price in stock_data
            stock_data['performance'] = performance
            stock_data['last_price'] = price

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
