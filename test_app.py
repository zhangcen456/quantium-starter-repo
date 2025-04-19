import pytest
import dash
from app import app

def test_elements_presented(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph")
    dash_duo.wait_for_element("#title")
    dash_duo.wait_for_element("#region-radio")
    assert dash_duo.find_element("#title").text=="Sales for pink morsels"
    radios = dash_duo.find_elements("input[type='radio']")
    labels = dash_duo.find_elements("label")
    for i in range(len(radios)):
        if radios[i].is_selected():
            assert labels[i].text=='north'