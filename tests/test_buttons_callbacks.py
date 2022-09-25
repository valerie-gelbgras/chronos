from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
from dash import no_update
import pytest

from src.chronos.components import buttons

@pytest.mark.parametrize("button_id, n_clicks_start, n_clicks_reset, start_button_state, expected", 
    [("start-button", 0, 0, '', ('START', 'success', True, no_update)),
     ("start-button", 1, 0, 'START', ('PAUSE', 'danger', False, no_update)),
     ("start-button", 2, 0, 'PAUSE', ('START', 'success', True, no_update)),
     ("reset-button", 0, 1, '', ('START', 'success', True, 0)),
     ("reset-button", 1, 1, 'START', ('START', 'success', True, 0))
    ]
)
def test_update_callback(button_id, n_clicks_start, n_clicks_reset, start_button_state, expected):
    context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": f"{button_id}.n_clicks"}]}))
    output = buttons.update(n_clicks_start, n_clicks_reset, start_button_state)
    assert output == expected
