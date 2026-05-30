import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)

    assert dash_duo.find_element(
        "#dashboard-header"
    ).is_displayed()


def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    assert dash_duo.find_element(
        "#sales-chart"
    ).is_displayed()


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    assert dash_duo.find_element(
        "#region-selector"
    ).is_displayed()