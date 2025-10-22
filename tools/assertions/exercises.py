from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
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
