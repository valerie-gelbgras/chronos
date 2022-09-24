# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from chronos_app import app
from components.layout import get_layout


if __name__ == '__main__':
    app.layout = get_layout()
    # app.config.suppress_callback_exceptions = True
    app.run_server(debug=True)
