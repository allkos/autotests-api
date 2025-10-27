from httpx import Client

from config import settings
from clients.event_hooks import log_request_event_hook, log_response_event_hook


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        timeout=settings.http_client.timeout,  # Таймаут теперь берётся из настроек
        base_url=settings.http_client.client_url,  # Базовый URL также из настроек
        event_hooks={
            "request": [log_request_event_hook],  # Логируем исходящие HTTP-запросы
            "response": [log_response_event_hook]  # Логируем полученные HTTP-ответы
        }

    )