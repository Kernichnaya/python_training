import jsonpickle
import json
import pytest
import os.path
import importlib
from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as cf:  # f
            target = json.load(cf)  # f
    return target

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    wef_config = load_config(request.config.getoption('--target'))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=wef_config['baseUrl'])
    fixture.session.ensure_login(username=wef_config['username'], password=wef_config['password'])
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_gr"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("data_co"):
            testdatacontact = load_form_module_contact(fixture[5:])
            metafunc.parametrize(fixture, testdatacontact, ids=[str(x) for x in testdatacontact])
        elif fixture.startswith("json_groups"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_contacts"):
            testdatacontact = load_form_json_contact(fixture[5:])
            metafunc.parametrize(fixture, testdatacontact, ids=[str(x) for x in testdatacontact])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def load_form_module_contact(module):
    return importlib.import_module("data.%s" % module).testdatacontact


def load_form_json_contact(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/contacts.json")) as f:
        return jsonpickle.decode(f.read())
