Custom worker
To use it, change in docker-compose.yml

```
rq-worker:
  build: ./worker
  image: worker
  container_name: rq_worker
  depends_on:
    - redis-server
    - mongodb
```