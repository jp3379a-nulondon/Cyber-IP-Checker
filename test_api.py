import pytest
from cyber_input_checker import valid_ip, extract_stats

# use --- python -m pytest test_api.py -v --- to run test in command terminal

def test_smoke():
    """Smoke test - checks basic test functionality."""
    assert True
    assert 5 + 5 == 10
    assert 1 + 2 != 7

# Testing IP address input validity and data extracted from api call

def test_valid_ip_address():
    """This function tests that a valid IPv4 address should return True."""
    assert valid_ip("192.168.1.1") is True

def test_invalid_ip_address():
    """This function tests that an invalid IPv4 address should return False."""
    assert valid_ip("999.999.999.999") is False

def test_extract_stats():
    """This function tests that VT analysis statistics are extracted correctly."""
    
    ip_address = "192.168.1.1"
    ip_data = {
        "data": {
            "attributes": {
                "last_analysis_stats": {
                    "malicious": 2,
                    "suspicious": 1,
                    "undetected": 85,
                    "harmless": 12
                }
            }
        }
    }

    expected = {
        "ip_address": "192.168.1.1",
        "malicious": 2,
        "suspicious": 1,
        "undetected": 85,
        "harmless": 12
    }
    assert extract_stats(ip_address, ip_data) == expected