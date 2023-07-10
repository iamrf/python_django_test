import csv
import json
import redis


def update_price_data():
    redis_client = redis.Redis(host='redis', port=6379, db=0)

    with open('price_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            time = row['Time']
            stock = row['Stock']
            price = row['Price']
            
            # Retrieve existing stock data from Redis
            stock_data =redis_client.get(stock)
            if stock_data:
                stock_data = json.loads(stock_data.decode('utf-8'))
            else:
                stock_data = {}
            
            # Update time and price history
            if 'time' in stock_data:
                stock_data['time'].append(time)
                stock_data['price'].append(price)
            else:
                stock_data['time'] = [time]
                stock_data['price'] = [price]

            # Save the updated stock data in Redis
            redis_client.set(stock, json.dumps(stock_data))


if __name__ == '__main__':
    update_price_data()