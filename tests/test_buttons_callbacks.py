from dash._callback_context import context_value
from dash._utils import AttributeDict
from dash import no_update
import pytest

from src.chronos.components import buttons


@pytest.mark.parametrize("button_id, n_clicks_start, n_clicks_reset, n_click_lap, table_state, timer_state, start_button_state, expected",
                         [
                             ("start-button", 0, 0, 0, [], '00:00:00.000', '', ('START', 'success', True, no_update, no_update, no_update)),
                             ("start-button", 1, 0, 0, [], '00:00:00.000', 'START', ('PAUSE', 'danger', False, no_update, no_update, no_update)),
                             ("start-button", 2, 0, 0, [], '00:00:00.000', 'PAUSE', ('START', 'success', True, no_update, no_update, no_update)),
                             ("reset-button", 0, 1, 0, [], '00:00:00.000', '', ('START', 'success', True, 0, [], 0)),
                             ("reset-button", 1, 1, 0, [], '00:00:00.000', 'START', ('START', 'success', True, 0, [], 0)),
                             ("reset-button", 1, 1, 1, ['Dummy', 'Dummy', 'Dummy'], '00:00:00.100', 'PAUSE', ('START', 'success', True, 0, [], 0)),
                             ("laps-button", 1, 0, 1, [], '00:00:00.100', 'PAUSE', (no_update, no_update, no_update, no_update, [], no_update))
                             ])
def test_update_callback(button_id, n_clicks_start, n_clicks_reset, n_click_lap, table_state, timer_state, start_button_state, expected):
    context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": f"{button_id}.n_clicks"}]}))
    output = buttons.update(n_clicks_start, n_clicks_reset, n_click_lap, start_button_state, table_state, timer_state)
    assert output == expected


def test_update_callback_for_lap_click():
    button_id = "laps-button"
    context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": f"{button_id}.n_clicks"}]}))
    (output_1, output_2, output_3, output_4, output_5, output_6) = buttons.update(n_clicks_start=1, n_clicks_reset=0, n_clicks_lap=2, start_button_state='PAUSE', table_state=[], timer_state='00:00:00.000')
    assert output_1 == no_update
    assert output_2 == no_update
    assert output_3 == no_update
    assert output_4 == no_update
    assert len(output_5) == 2
    output_5[0] = """Thead(Tr([Th('Lap #'), Th('Time')]))"""
    output_5[1] = """Tbody([Tr([Td('2'), Td('00:00:00.000')])])"""
    assert output_6 == no_update
