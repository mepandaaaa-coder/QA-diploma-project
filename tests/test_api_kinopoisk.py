import allure
from units.api_client import ApiClient

BASE_URL = "https://api.kinopoisk.dev"
API_KEY = "N7ZA1K7-TC8MG4F-K1K6RPY-3K6CJFP"

api = ApiClient(base_url=BASE_URL, token=API_KEY)


@allure.epic("API Тестирование Кинопоиска")
@allure.feature("REST API (api.kinopoisk.dev)")
class TestKinopoiskAPI:

    @allure.story("Тест 1: Получение случайного фильма")
    def test_get_random_movie(self) -> None:
        with allure.step("Запросить случайный фильм через API-клиент"):
            response = api.get("/v1.4/movie/random")

        with allure.step("Проверить статус 200 и наличие ID"):
            assert response.status_code == 200
            data = response.json()
            assert "id" in data or "kinopoiskId" in data

    @allure.story("Тест 2: Поиск фильмов с фильтрацией")
    def test_search_movies_with_filter(self) -> None:
        with allure.step("Отправить запрос с фильтром по рейтингу"):
            response = api.get(
                "/v1.4/movie",
                params={"page": 1, "limit": 10, "rating.kp": "7-10"},
            )

        with allure.step("Проверить наличие списка фильмов в поле docs"):
            assert response.status_code == 200
            data = response.json()
            assert "docs" in data
            assert len(data["docs"]) > 0

    @allure.story("Тест 3: Получение фильма по ID")
    def test_get_movie_by_id(self) -> None:
        movie_id = 789374
        with allure.step(f"Запросить фильм с ID {movie_id}"):
            response = api.get(f"/v1.4/movie/{movie_id}")

        with allure.step("Проверить успешность ответа"):
            assert response.status_code == 200
            data = response.json()
            assert (
                data.get("id") == movie_id
                or data.get("kinopoiskId") == movie_id
            )

    @allure.story("Тест 4: Негативный тест — запрос несуществующего ID")
    def test_get_non_existent_movie_negative(self) -> None:
        invalid_id = 14999999
        with allure.step(f"Запросить несуществующий ID {invalid_id}"):
            response = api.get(f"/v1.4/movie/{invalid_id}")

        with allure.step("Проверить код ошибки"):
            assert response.status_code in [404]

    @allure.story("Тест 5: Негативный тест — запрос без токена")
    def test_unauthorized_request_negative(self) -> None:
        with allure.step(
            "Отправить запрос без заголовка "
            "авторизации (use_auth=False)"
        ):
            response = api.get("/v1.4/movie/random", use_auth=False)

        with allure.step("Проверить статус 401 Unauthorized"):
            assert response.status_code == 401
