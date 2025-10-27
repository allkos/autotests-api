import allure


from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, ExerciseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.courses import assert_course
from tools.assertions.errors import assert_internal_error_response
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("EXERCISES_ASSERTIONS")


@allure.step("Check create exercise response")
def assert_create_exercise_response(
    create_exercise_request: CreateExerciseRequestSchema,
    create_exercise_response: CreateExerciseResponseSchema,
):

    """
    Проверяет, что ответ на создание курса соответствует данным запроса.

    :param create_exercise_request: Данные, отправленные в запросе.
    :param create_exercise_response: Ответ API после создания задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create exercise response")
    exercise=create_exercise_response.exercise

    assert_equal(exercise.title, create_exercise_request.title, "title")
    assert_equal(exercise.max_score, create_exercise_request.max_score, "max_score")
    assert_equal(exercise.min_score, create_exercise_request.min_score, "min_score")
    assert_equal(exercise.description, create_exercise_request.description, "description")
    assert_equal(exercise.estimated_time, create_exercise_request.estimated_time, "estimated_time")
    assert_equal(exercise.course_id, create_exercise_request.course_id, "course_id")
    assert_equal(exercise.order_index, create_exercise_request.order_index, "order_index")


@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check exercise")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check get exercise response")
def assert_get_exercise_response (
    get_exercise_response: GetExerciseResponseSchema,
    create_exercise_response: CreateExerciseResponseSchema
    ):
    """
    Проверяет, что ответ на получение задания соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных задания.
    :param create_exercise_response: Ответ API при создании задания.
    :raises AssertionError: Если данные задания не совпадают.
    """
    logger.info("Check get exercise response")
    assert_exercise (get_exercise_response.exercise, create_exercise_response.exercise)


@allure.step("Check update exercise response")
def assert_update_exercise_response(
        update_exercise_request: UpdateExerciseRequestSchema,
        update_exercise_response: UpdateExerciseResponseSchema,
):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param request: Исходный запрос на обновление задания.
    :param response: Ответ API с обновленными данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check update exercise response")
    exercise=update_exercise_response.exercise

    assert_equal(exercise.title, update_exercise_request.title, "title")
    assert_equal(exercise.max_score, update_exercise_request.max_score, "max_score")
    assert_equal(exercise.min_score, update_exercise_request.min_score, "min_score")
    assert_equal(exercise.order_index, update_exercise_request.order_index, "order_index")
    assert_equal(exercise.description, update_exercise_request.description, "description")
    assert_equal(exercise.estimated_time, update_exercise_request.estimated_time, "estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    logger.info("Check exercise not found response")

    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get exercises response")
def assert_get_exercises_response(
    get_exercises_response: GetExercisesResponseSchema,
    create_exercises_responses: list[CreateExerciseResponseSchema]
):

    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка заданий.
    :param create_exercises_responses: Список API ответов при создании заданий.
    :raises AssertionError: Если данные не совпадают.
    """
    logger.info("Check get exercises response")
    assert_length(get_exercises_response.exercises, create_exercises_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercises_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)
