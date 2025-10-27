import allure
from httpx import Request, Response

from tools.logger import get_logger  # Импортируем функцию для создания логгера

# Инициализируем логгер один раз на весь модуль
logger = get_logger("HTTP_CLIENT")


def log_request_event_hook(request: Request):  # Создаем event hook для логирования запроса
    """
    Логирует информацию об отправленном HTTP-запросе.

    :param request: Объект запроса HTTPX.
    """
    # Пишем в лог информационное сообщение о запроса
    logger.info(f'Make {request.method} request to {request.url}')


def log_response_event_hook(response: Response):  # Создаем event hook для логирования ответа
    """
    Логирует информацию о полученном HTTP-ответе.

    :param response: Объект ответа HTTPX.
    """
    # Пишем в лог информационное сообщение о полученном ответе
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )