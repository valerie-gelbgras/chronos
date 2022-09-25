# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com


try:
    from chronos_app import app
except:
    print("test")

from components.layout import get_layout


if __name__ == '__main__':
    app.layout = get_layout()
    app.run_server(debug=True)
