#!/usr/bin/env python
import json
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
    expected_response = {"Hello": "World"}
    assert response.status_code == 200
    assert json.dumps(expected_response) == json.dumps(json.loads(response.data))


def test_post_request(client):
    """
    Given a Flask app
    When a POST request is sent to the hello endpoint
    Then a JSON response of the request payload is returned
    """
    expected_response = {"Hello": "pytest"}
    response = client.post(
        "/api/v1/hello",
        data=json.dumps(expected_response),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    assert json.dumps(expected_response) == json.dumps(json.loads(response.data))
