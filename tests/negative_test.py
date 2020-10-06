import json

import requests


def test_check_contactlist_status_with_invalid_id():
    get_response = requests.get("http://3.13.86.142:3000/contacts/1")
    expected_value = 404
    assert get_response.status_code == expected_value


def test_check_contactlist_body_with_invalid_id():
    get_response = requests.get("http://3.13.86.142:3000/contacts/1")
    expected_text = "Not Found"
    assert get_response.text == expected_text


def test_add_contact_with_missing_firstname():
    url = "http://3.13.86.142:3000/contacts"
    data_to_be_added = {
        "_id": "5f361af51707340476576421",
        "firstName": "",
        "lastName": "Smith",
        "email": "Jsmith@thinkingtester.com",
        "location": {
            "city": "Banska Bystrica, SS",
            "country": "Slovakia"
        },
        "employer": {
            "jobTitle": "Software Automation Tester",
            "company": "Tesla"
        },
        "__v": 0
    }
    headers = {'Content-Type': 'application/json'}
    get_response = requests.post(url, json=data_to_be_added)
    expected_status_code = 400
    expected_text = {
        "err": "Contacts validation failed: firstName: First Name is required"
    }
    print("*******")
    print(get_response.content)
    print(get_response.json())
    # assert get_response.status_code == expected_status_code
    assert get_response.json() == expected_text


def test_add_contact_with_missing_email():
    url = "http://3.13.86.142:3000/contacts"

    data_to_be_added = {
        "_id": "5f361af51707340476576421",
        "firstName": "Jonas",
        "lastName": "Smith",
        "email": "",
        "location": {
            "city": "Banska Bystrica, SS",
            "country": "Slovakia"
        },
        "employer": {
            "jobTitle": "Software Automation Tester",
            "company": "Tesla"
        },
        "__v": 0
    }

    get_response = requests.post(url, json=data_to_be_added)

    expected_text = {
        "err": "Contacts validation failed: email: Email is required"
    }
    assert get_response.json() == expected_text


def test_email_in_standard_format():
    url = "http://3.13.86.142:3000/contacts"
    data_to_be_added = {
        "_id": "5f361af51707340476576421",
        "firstName": "Jonas",
        "lastName": "Smith",
        "email": "Jsmith@thinkingtester",
        "location": {
            "city": "Banska Bystrica, SS",
            "country": "Slovakia"
        },
        "employer": {
            "jobTitle": "Software Automation Tester",
            "company": "Tesla"
        },
        "__v": 0
    }

    get_response = requests.post(url, json=data_to_be_added)
    expected_text = {
        "err": "Contacts validation failed: email: Validator failed for path `email` with value `Jsmith@thinkingtester`"
    }

    assert get_response.json() == expected_text


def test_delete_contact_with_invalid_id():
    url = "http://3.13.86.142:3000/contacts/1"

    get_response = requests.delete(url)

    expected_text = "Not Found"

    assert get_response.text == expected_text
