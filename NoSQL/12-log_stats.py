#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    total = collection.count_documents({})
    print(f"{total} logs")
    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        n = collection.count_documents({"method": m})
        print(f"\tmethod {m}: {n}")
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
