import redis


redis = redis.Redis(
    host='localhost',
    port=6379,
    db=5
)
