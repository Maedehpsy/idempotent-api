# idempotent-api
Idempotent payment API with FastAPI and Redis
## Files

- `main.py` - API code
- `requirements.txt` - Dependencies

## How to run

```bash
pip install -r requirements.txt
redis-server
uvicorn main:app --reload
