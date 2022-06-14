import pytest
from config import app

def test_admin_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/')

        assert response.status_code == 200


def test_source_of_data_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/source_of_data/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/source_of_data/')

        assert response.status_code == 200


def test_address_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/address/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/address/')

        assert response.status_code == 200


def test_customer_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/customer/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/customer/')

        assert response.status_code == 200


def test_invoice_page():
    """
    GIVEN a Flask app to provide a common database
    WHEN the '/admin/invoice/' page is requested (GET)
    THEN Check that the respond is valid
    """

    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get('/admin/invoice/')

        assert response.status_code == 200