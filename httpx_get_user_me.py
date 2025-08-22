import httpx  # Импортируем библиотеку HTTPX


# Инициализируем JSON-данные, которые будем отправлять в API
login_payload = {
    "email": "test@test.com",
    "password": "test"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

access_token = login_response_data["token"]["accessToken"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

get_user_me= httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
get_user_me_data = get_user_me.json()

print("get_user_me_response:", get_user_me_data)
print("Status Code:", get_user_me.status_code)