
# Python Django Test
A sample microservice project with Django, Redis and Kafka to test your familiarities with these tools.

To see full info about this project, [Click Here](https://github.com/amogadasi/python_django_test/)

### Requirements

You need [Docker](https://docs.docker.com/get-docker/) installed on you machine to run **Redis** and **Apache Kafka** instances. [Python](https://www.python.org/downloads/) is also needed for various scripts in all the steps.

> **Note:** Preferably use Python 3.7+

## Included in the Project

- `services/`: Directory containing the Python scripts for various steps.
- `services/price_updater.py`: Python script for Step 1 to update price data in the Redis database.
- `services/price_data.csv`: Sample price data for three fictional stocks needed in the next steps.
- `redis/`: Directory containing the Docker configuration for Redis.
- `redis/redis_data.txt`: Initial data to be loaded into the Redis database.
- `redis/Dockerfile`: Dockerfile for the Redis container, now utilizing entrypoint.sh.
- `redis/entrypoint.sh`: Bash script for initializing Redis data and saving it to disk.
- `kafka/`: Directory containing the Docker configuration for Kafka.


## Step 1:

The first step involves building a Python script `price_updater.py` that updates the price data for three stocks (Stock1, Stock2, and Stock3) starting from 9:00:00 to 9:59:47. The script connects to the Redis database and updates the time and price history of each corresponding stock.

To run the Price Updater Service, execute the following commands in root directory:

```
docker-compose up --build -d
```


> **Changes:** Using `entrypoint.sh` Instead of `sleep 5`
- In the original Dockerfile for Redis, the use of `& sleep 5s` might cause issues as it runs the server in the background, and there could be a race condition between the server startup and the `redis-cli` command. To improve this, we introduced a new entrypoint.sh script.

`entrypoint.sh` waits for Redis to be ready before loading data into the database using the `redis-cli`. The script ensures that the database is populated correctly before the server starts. This avoids potential race conditions and ensures that data is successfully loaded into Redis.
