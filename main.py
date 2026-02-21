from fastapi import FastAPI, Header
import redis
import json
import time

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.post("/pay")
def pay(amount: int, idempotency_key: str = Header(None)):
    if not idempotency_key:
        return {"error": "Idempotency-Key required"}
    
    key = f"idemp:{idempotency_key}"
    locked = redis_client.set(key, json.dumps({"status": "processing"}), nx=True, ex=3600)
    
    if not locked:
        return {"status": "already_processed", "result": json.loads(redis_client.get(key))}
    
    time.sleep(2)
    result = {"amount": amount, "status": "success", "transaction_id": "txn_12345"}
    redis_client.set(key, json.dumps(result), ex=3600)
    
    return {"status": "processed", "result": result}
