import os
import time
import requests
import pytest

# Base URL for backend API
BASE = os.getenv("TEST_BASE", "http://host.docker.internal:8000")

def wait_for_backend(base, timeout=30):
    """Wait until backend health endpoint returns OK"""
    t0 = time.time()
    while time.time() - t0 < timeout:
        try:
            r = requests.get(f"{base}/api/health", timeout=3)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(1)
    return False

@pytest.mark.timeout(180)
def test_ingest_and_queries():
    base = BASE
    assert wait_for_backend(base), f"Backend not responding at {base}"

    # Step 1 - Ingest sample docs
    r = requests.post(f"{base}/api/ingest", timeout=120)
    assert r.status_code == 200, f"Ingest failed: {r.status_code} {r.text}"
    data = r.json()
    assert data.get("indexed_docs", 0) > 0
    assert data.get("indexed_chunks", 0) > 0

    # Step 2 - Ask first question
    q1 = "Can a customer return a damaged blender after 20 days?"
    r1 = requests.post(f"{base}/api/ask", json={"query": q1, "k": 4}, timeout=30)
    assert r1.status_code == 200
    j1 = r1.json()
    titles1 = [c.get("title", "") for c in j1.get("citations", [])]
    assert any("Return" in t or "Refund" in t for t in titles1), f"Unexpected titles: {titles1}"

    # Step 3 - Ask second question
    q2 = "What's the shipping SLA to East Malaysia for bulky items?"
    r2 = requests.post(f"{base}/api/ask", json={"query": q2, "k": 4}, timeout=30)
    assert r2.status_code == 200
    j2 = r2.json()
    titles2 = [c.get("title", "") for c in j2.get("citations", [])]
    assert any("Delivery" in t or "Shipping" in t for t in titles2), f"Unexpected titles: {titles2}"
