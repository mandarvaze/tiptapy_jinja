import json
from jinja2 import FileSystemLoader, Environment, select_autoescape
from jsons import olist_json, image_json, simple_json


def init_env(path='templates/'):
    return Environment(loader=FileSystemLoader(path),
                       autoescape=select_autoescape(
                           enabled_extensions=('jinja2'))
                       )


class BaseDoc:

    node_type = 'base'
    templates_path = 'base-templates-dir'

    def __init__(self):
        templates = init_env()
        self.t = templates.get_template(f'{self.node_type}.html')


    def render(self, in_data):
        node = in_data if isinstance(in_data, dict) else json.loads(in_data)
        return self.t.render(node=node)


class Doc(BaseDoc):

    node_type = "doc"
    template_path = 'templates/'


class NewsletterDoc(BaseDoc):

    node_type = "nldoc"
    template_path = 'templates/newsletter'


doc = Doc()
nldoc = NewsletterDoc()


if __name__ == "__main__":
    print(doc.render(olist_json))
