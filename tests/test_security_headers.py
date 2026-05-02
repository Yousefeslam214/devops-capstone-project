"""Tests for security headers and CORS policy."""

from service import app


def test_root_returns_200():
    """Verify service root endpoint works."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_cors_headers_present():
    """Verify CORS headers are added."""
    client = app.test_client()
    response = client.get("/", headers={"Origin": "http://example.com"})
    assert response.headers.get("Access-Control-Allow-Origin") == "http://example.com"


def test_talisman_security_headers_present():
    """Verify security headers added by Talisman."""
    client = app.test_client()
    response = client.get("/")
    assert response.headers.get("X-Frame-Options") == "SAMEORIGIN"
    assert response.headers.get("X-Content-Type-Options") == "nosniff"
