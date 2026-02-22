# 🔒 Idempotent Payment API

Zero-duplicate transaction handling for Django applications using idempotency key pattern.

## 🎯 Problem

| Scenario | Result |
|----------|--------|
| User clicks "Pay" twice | Double charge 💸 |
| Network timeout + retry | Duplicate order |
| Race condition | Data inconsistency |

## ✅ Solution

Idempotency Key + Redis Distributed Lock

## 🚀 Quick Start

```bash
docker-compose up
