import requests
import unittest
import server
import json
from collections import Counter

class TestWordCountApp(unittest.TestCase):

    def get_count(self, text, words_excluded):
        cnt = Counter()
        for word in text.split():
            if word not in words_excluded:
                cnt[word] += 1
        return dict(cnt)

    def get_request_data(self):
        rv = self.app.get('/')
        data = json.loads(rv.data)
        count = self.get_count(data.get('text'), data.get('words'))
        request_data = {"words": count, "text": data.get("text"), "token": data.get("token")}
        return request_data

    def setUp(self):
        self.app = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_default_route_gives_json(self):
        rv = self.app.get('/')
        assert rv.status_code == 200

    def test_correct_data_gives_200(self):
        request_data = self.get_request_data()
        headers = [("Content-Type", "application/json")];
        rv = self.app.post('/', headers=headers, data=json.dumps(request_data))
        assert rv.status_code == 200

    def test_incorrect_token_gives_400(self):
        request_data = self.get_request_data()
        request_data["token"] = 0
        headers = [("Content-Type", "application/json")];
        rv = self.app.post('/', headers=headers, data=json.dumps(request_data))
        assert rv.status_code == 400

    def test_incorrect_text_gives_400(self):
        request_data = self.get_request_data()
        request_data["text"] = "hello world"
        headers = [("Content-Type", "application/json")];
        rv = self.app.post('/', headers=headers, data=json.dumps(request_data))
        assert rv.status_code == 400

    def test_incorrect_word_count_gives_400(self):
        request_data = self.get_request_data()
        request_data["words"] = {}
        headers = [("Content-Type", "application/json")];
        rv = self.app.post('/', headers=headers, data=json.dumps(request_data))
        assert rv.status_code == 400
