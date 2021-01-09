import json

import requests


class QueryError(Exception):
    pass


class QueryMaker:
    def __init__(self, session):
        self._session = session

    def exec(self, query):
        job_id = self._create_job(query)
        query_result_id = self._wait_for_job(job_id)
        rows = self._get_rows(query_result_id)
        return rows

    def _get_headers(self):
        return {
            'Cookie': self._session.cookie,
        }

    def _create_job(self, query):
        data = {
            'data_source_id': 4,
            'max_age': 0,
            'parameters': {},
            'query': query,
        }
        with requests.post("https://explore.duneanalytics.com/api/query_results",
                           data=json.dumps(data),
                           headers=self._get_headers()) as response:
            return response.json()['job']['id']

    def _wait_for_job(self, job_id):
        while True:
            url = f"https://explore.duneanalytics.com/api/jobs/{job_id}"
            with requests.get(url, headers=self._get_headers()) as response:
                data = response.json()['job']

            if data['status'] == 1:
                raise QueryError("Execution has not started")

            elif data['status'] == 2:
                continue

            elif data['status'] == 3:
                return data['query_result_id']

            elif data['status'] == 4:
                raise QueryError(data['error'])

    def _get_rows(self, query_result_id):
        url = f"https://explore.duneanalytics.com/api/query_results/{query_result_id}"
        with requests.get(url, headers=self._get_headers()) as response:
            return response.json()['query_result']['data']['rows']
