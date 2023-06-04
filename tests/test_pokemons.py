import requests
import pytest

host = 'https://pokemonbattle.me:9104'
token = '4e22e163d77f56527da0554e14930b47'
def test_part_of_answer():
    answer_body = requests.get(f'{host}/trainers')
    assert answer_body.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', 'Троян')])
def test_parts_of_answer(key, value):
    answer = requests.get(f'{host}/trainers', params = {'trainer_id' : 4239})
    assert answer.json()[key] == value