#!/usr/bin/env python
import pytest
from app import create_app


@pytest.fixture()
def app():
    test_app = create_app()
    yield test_app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_get_request(client):
    """
    Given a Flask app
    When a GET request is sent to the hello endpoint
    Then a JSON response of hello world is returned
    """
    response = client.get("/api/v1/hello")
    expected_response = '{"Hello":"World"}'
    assert response.status_code == 200
    assert expected_response.encode() in response.data


def test_post_request(client):
    """
    Given a Flask app
    When a POST request is sent to the hello endpoint
    Then an HTML response of greeting the requester is returned
    """
    response = client.post("/api/v1/hello/pytest")
    expected_response = "<h1>Hello, pytest!</h1>"
    assert response.status_code == 200
    assert expected_response.encode() in response.data
