import os
import json
import pytest

import project


@pytest.fixture
def client():
    project.app.config['TESTING'] = True
    client = project.app.test_client()

    yield client


def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'hello': 'world!'}
