from http import HTTPStatus

import pytest
import allure
from allure_commons.types import Severity  # Импортируем enum Severity из Allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExercisesResponseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesQuerySchema
from fixtures.courses import CourseFixture
from clients.exercises.exercises_client import ExercisesClient
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema
from tools.allure.tags import AllureTag  # Импортируем enum с тегами
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.EXERCISES)
# Добавили feature
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)  # Добавили тег
    @allure.title("Create exercise")
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    def test_create_exercise(
        self,
        exercises_client:ExercisesClient,
        function_course:CourseFixture,
    ):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get exercise")
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    def test_get_exercise(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture,
    ):
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)
        assert_get_exercise_response(response_data,function_exercise.response)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Update exercise")
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_update_exercise(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture,
    ):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)
        assert_update_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Delete exercise")
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_delete_exercise(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture,
    ):
        delete_response = exercises_client.delete_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)
        assert_exercise_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.title("Get exercises")
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    def test_get_exercises(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture,
        function_course: CourseFixture,
    ):
        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_get_exercises_response(response_data, [function_exercise.response])

        validate_json_schema(response.json(), response_data.model_json_schema())
