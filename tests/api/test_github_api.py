import pytest


@pytest.mark.api
def test_user_exist(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_non_exist(github_api):
    req = github_api.get_user('kakorinviktor_repo')
    assert req['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    req = github_api.search_repo('become-qa-auto')
    assert req['total_count'] == 26


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    req = github_api.search_repo('viktorkakorin_repo_non_exist')
    assert req['total_count'] == 0
