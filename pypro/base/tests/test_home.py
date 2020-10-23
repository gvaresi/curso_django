from django.test import Client


def test_status_code(client: Client):
    resp = client.get('/')
    # assert resp.status_code == 200 # linha original com mensagem 'Ola Django'
    assert resp.status_code == 404
