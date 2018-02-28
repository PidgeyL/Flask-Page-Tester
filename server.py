from flask     import Flask, render_template

class WebServer:
    app = Flask(__name__, static_folder   = "static",
                          template_folder = "templates")

    def __init__(self, page, page_vars = None):
        self.page      = page
        self.page_vars = page_vars or {}

    def index(self):
        return render_template(self.page, **self.page_vars)

    def start(self):
        self.app.add_url_rule('/', view_func=self.index, methods=['GET'])
        host, port = ('127.0.0.1', 5000)
        self.app.run(host=host, port=port)



if __name__ == '__main__':
    import argparse
    _ap = argparse.ArgumentParser(description='Test pages')
    _ap.add_argument('page', type=str,            help='Page to test')
    _ap.add_argument('vars', type=str, nargs='?', help='Variable file (.py)')
    args = _ap.parse_args()

    if args.vars:
        mod = __import__(args.vars.split('.')[0])
        server = WebServer(args.page, mod.page_vars)
    else:
        server = WebServer(args.page)
    
    server.start()
