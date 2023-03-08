import httpx


def assert_status_code(response: httpx.Response, status_code: int):
    try:
        full_response = response.json()
    except:
        full_response = response.text
    error_message = (
        f"assert {response.status_code} == {status_code}"
        f"\nFull response: {full_response}"
    )
    assert response.status_code == status_code, error_message
