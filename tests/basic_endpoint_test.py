import requests
import pytest_html


def test_check_status_code_contactlist():
    get_response = requests.get("http://3.13.86.142:3000/contacts")
    assert get_response.status_code == 200


def test_content_type_contactlist():
    get_response = requests.get("http://3.13.86.142:3000/contacts")
    expected_value = "application/json; charset=utf-8"
    assert get_response.headers['Content-Type'] == expected_value


def test_country_field_present_in_contact():
    get_response = requests.get("http://3.13.86.142:3000/contacts/5f1b3f051707340476573cd5")
    response_body = get_response.json()
    expected_value = "Spain"
    assert response_body["location"].get("country") == expected_value


def test_check_email_field_in_contact():
    get_response = requests.get("http://3.13.86.142:3000/contacts/5f1b3f051707340476573cd5")
    response_body = get_response.json()
    expected_value = "mali@redpoints.com"
    assert response_body["email"] == expected_value


def test_number_of_fields_in_contact():
    get_response = requests.get("http://3.13.86.142:3000/contacts/5f1b3f051707340476573cd5")
    response_body = get_response.json()
    expected_value = 2
    assert len(response_body["location"]) == expected_value


def test_add_new_contact_into_contactlist():
    url = "http://3.13.86.142:3000/contacts"
    data_to_be_added = {
        "_id": "5f361af51707340476576415",
        "firstName": "Jonas",
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

    get_response = requests.post(url, json=data_to_be_added)
    expected_status_code = 200
    assert get_response.status_code == expected_status_code


def test_check_new_contact_added_into_contactlist():
    url = "http://3.13.86.142:3000/contacts/5f361af51707340476576415"
    get_response = requests.get(url)
    expected_value = "Jonas"
    get_body = get_response.json()
    assert get_body["firstName"] == expected_value


def test_modify_newly_added_contact():
    url = "http://3.13.86.142:3000/contacts/5f361af51707340476576415"
    data_to_be_modified = {
        "_id": "5f361af51707340476576415",
        "firstName": "Simon",
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

    get_response = requests.put(url, json=data_to_be_modified)
    expected_status_code = 204
    assert get_response.status_code == expected_status_code


def test_check_new_contact_added_into_contactlist_after_update():
    url = "http://3.13.86.142:3000/contacts/5f361af51707340476576415"
    get_response = requests.get(url)
    expected_value = "Simon"
    get_body = get_response.json()
    assert get_body["firstName"] == expected_value


def test_delete_newly_added_contact_from_contactlist():
    url = "http://3.13.86.142:3000/contacts/5f361af51707340476576415"
    get_response = requests.delete(url)
    expected_status_code = 204
    assert get_response.status_code == expected_status_code
