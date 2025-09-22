from src.views.user_finder_view import UserFinderView
from src.views.http_types.http_request import HttpRequest

class UserFinderMock():
    def find_by_person_name(self, person_name: str) -> dict:
        formatted_users = [{"person_name": "random_name", "age": 30, "height": 175}]
        return {
            "Type": "User",
            "count": len(formatted_users),
            "attributes": formatted_users
        }


def test_handle_find_by_person_name():
    user_finder = UserFinderMock()
    view = UserFinderView(user_finder)

    request = HttpRequest(param={"person_name": "random_name"}, body={"person_name": "random_name"})
    expected_result = [{"person_name": "random_name", "age": 30, "height": 175}]

    response = view.handle_find_by_person_name(request)

    assert response.status_code == 200
    assert response.body["attributes"] == expected_result

    print(response)
