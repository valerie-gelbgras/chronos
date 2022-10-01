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
                             ])
def test_update_callback(button_id, n_clicks_start, n_clicks_reset, n_click_lap, table_state, timer_state, start_button_state, expected):
    context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": f"{button_id}.n_clicks"}]}))
    output = buttons.update(n_clicks_start, n_clicks_reset, n_click_lap, start_button_state, table_state, timer_state)
    assert output == expected


@pytest.mark.parametrize("start_button_state, n_clicks_lap, table_state, timer_state, table_updated, expected_element_in_updated_table, expected_row",
                         [
                             ('PAUSE', 1, [], '00:00:00.700', True, 2, """Tbody([Tr([Td('1'), Td('00:00:00.700')])])"""),
                             ('PAUSE', 2, ["""Thead(Tr([Th('Lap #'), Th('Time')]))""", """Tbody([Tr([Td('1'), Td('00:00:00.800')])])"""], '00:00:00.700', True, 3, """Tbody([Tr([Td('2'), Td('00:00:00.800')])])"""),
                             ('START', 3, ["""Thead(Tr([Th('Lap #'), Th('Time')]))""", """Tbody([Tr([Td('1'), Td('00:00:00.900')])])"""], '00:00:00.700', False, 2, """Tbody([Tr([Td('2'), Td('00:00:00.900')])])"""),
                            ])
def test_update_callback_for_lap_click(start_button_state, n_clicks_lap, table_state, timer_state, table_updated, expected_element_in_updated_table, expected_row):
    button_id = "laps-button"
    context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": f"{button_id}.n_clicks"}]}))
    (output_1, output_2, output_3, output_4, output_5, output_6) = buttons.update(n_clicks_start=1, n_clicks_reset=0, n_clicks_lap=n_clicks_lap, start_button_state=start_button_state, table_state=table_state, timer_state=timer_state)
    assert output_1 == no_update
    assert output_2 == no_update
    assert output_3 == no_update
    assert output_4 == no_update
    if table_updated:
        assert len(output_5) == expected_element_in_updated_table
        output_5[0] = """Thead(Tr([Th('Lap #'), Th('Time')]))"""
        output_5[-1] = expected_row
        output_6 == no_update
    else:
        assert output_5 == no_update
        assert output_6 == n_clicks_lap - 1
