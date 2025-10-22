from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, ExerciseSchema
from tools.assertions.base import assert_equal


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
    exercise=create_exercise_response.exercise

    assert_equal(exercise.title, create_exercise_request.title, "title")
    assert_equal(exercise.max_score, create_exercise_request.max_score, "max_score")
    assert_equal(exercise.min_score, create_exercise_request.min_score, "min_score")
    assert_equal(exercise.description, create_exercise_request.description, "description")
    assert_equal(exercise.estimated_time, create_exercise_request.estimated_time, "estimated_time")
    assert_equal(exercise.course_id, create_exercise_request.course_id, "course_id")
    assert_equal(exercise.order_index, create_exercise_request.order_index, "order_index")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


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
    assert_exercise (get_exercise_response.exercise, create_exercise_response.exercise)
