import pytest
import requests


class TestJsonPlaceHolder:
    """Collection of tests for JsonPlaceHolder API : https://jsonplaceholder.typicode.com"""

    @pytest.mark.parametrize("userId,userName", [
        (1, "Leanne Graham"), (5, "Chelsey Dietrich"),
        (8, "Nicholas Runolfsdottir V"), (4, "Patricia Lebsack")
    ])
    def test_check_user_name_by_id(self, base_url, userId, userName):
        """Getting users by userId and validating name of user"""

        response = requests.get(base_url + f"users/{userId}")
        assert response.ok

        res_json = response.json()
        assert res_json['id'] == userId
        assert res_json['name'] == userName

    @pytest.mark.parametrize("userCount", [10])
    def test_get_all_users(self, base_url, userCount):
        """Checking user count from API"""

        response = requests.get(base_url + "users")
        assert response.ok
        assert len(response.json()) == userCount

    @pytest.mark.parametrize("comment", [500])
    def test_get_all_comments(self, base_url, comment):
        """Checking 500 comments on the page"""
        response = requests.get(base_url + "comments")
        assert response.ok
        assert len(response.json()) == comment

    @pytest.mark.parametrize("emails", [[
        "Presley.Mueller@myrl.com", "Dallas@ole.me", "Mallory_Kunze@marie.org",
        "Meghan_Littel@rene.us", "Carmen_Keeling@caroline.name"
    ]])
    def test_get_comment_emails(self, base_url, emails):
        """Checking emails from posts id=2"""
        response = requests.get(base_url + "posts/2/comments/")
        assert response.ok
        res_json = response.json()
        compare_email = []

        for item in range(len(res_json)):
            email_item = res_json[item]['email']
            compare_email.append(email_item)
        assert compare_email == emails

    @pytest.mark.parametrize("Id, index", [(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5)])
    def test_api_todos(self, base_url, Id, index):
        response = requests.get(
            base_url + "todos/"
        ).json()
        assert len(response) > 0
        assert response[index]['id'] == Id
