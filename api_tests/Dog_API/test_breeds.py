import requests
import pytest


class TestBreedAPI:
    """Class for testing API dog.ceo website"""

    def test_get_all_breeds(self):
        """Checking request for getting all breeds"""

        url = f"https://dog.ceo/api/breeds/list/all"
        response = requests.get(url)
        assert response.ok
        assert response.json().get('status') == 'success'

    @pytest.mark.parametrize("breeds", ["akita", "beagle", "african"])
    def test_by_breed_random_image(self, base_breed_url, request_method, breeds):
        """Checking breeds random images"""

        url = base_breed_url + f"{breeds}/images/random"
        response = request_method(url)
        assert response.ok
        assert response.json().get('status') == 'success'
        assert response.json().get('message').endswith('.jpg')

    @pytest.mark.parametrize("breeds,img_count", [("redbone", 3), ("entlebucher", 4), ("shiba", 5)])
    def test_by_breed_multiple_random_images(self, base_breed_url, request_method, breeds, img_count):
        """Checking random images and count of images"""

        url = base_breed_url + f"{breeds}/images/random/{img_count}"
        response = request_method(url)
        assert response.ok
        assert response.json().get('status') == 'success'
        assert len(response.json().get('message')) == img_count
        for img in response.json().get('message'):
            assert img.endswith('.jpg') or img.endswith('.jpeg')

    def test_random_image(self, base_url, request_method):
        """Get random image of dog"""

        url = base_url + f"image/random/"
        response = request_method(url)
        assert response.ok
        assert response.json().get('status') == 'success'
        assert response.json().get('message').endswith('.jpg')

    @pytest.mark.parametrize("dog_output", [["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]])
    def test_sub_breed(self, base_breed_url, request_method, dog_output):
        """Get all sub-breeds for hound dog"""
        url = base_breed_url + f"hound/list"
        response = request_method(url)
        assert response.ok
        assert response.json().get('status') == 'success'
        assert response.json().get('message') == dog_output
