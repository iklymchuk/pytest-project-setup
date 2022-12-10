import requests
import json

testing_env_companies_url = "http://127.0.0.1:8000/companies/"


def test_zero_companies():
    response = requests.get(url=testing_env_companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_create_company():
    response = requests.post(
        url=testing_env_companies_url,
        json={"name": "test company name"},
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("stutus") == "Layoffs"

    cleanup_company(company_id=response_content["id"])


def cleanup_company(company_id: str):
    response = requests.delete(url=f"testing_env_companies_url{company_id}")
    assert response.status_code == 204
