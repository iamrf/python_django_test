FROM redis

COPY redis_data.txt /
COPY entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]
CMD ["redis-server", "--appendonly", "yes"]
