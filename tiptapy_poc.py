import json
from jinja2 import FileSystemLoader, Environment, select_autoescape

simple_json = {
    "type": "doc",
    "content": [
        {
            "type": "text",
            "text": "Here is an example of simple formatted text"
        }
     ]
  }

olist_json = {
  "type": "doc",
  "content": [
    {
      "type": "title",
      "content": [
        {
          "type": "text",
          "text": "Scroll"
        }
      ]
    },
    {
      "type": "ordered_list",
      "attrs": {
        "order": 1
      },
      "content": [
        {
          "type": "list_item",
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": "One"
                }
              ]
            }
          ]
        },
        {
          "type": "list_item",
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": "Two"
                }
              ]
            }
          ]
        },
      ]
    }
  ]
}

image_json = {
  "type": "image",
  "attrs": {
    "src": {"image": "https://placekitten.com/200/301", "fallback": "https://placekitten.com/198/654"},
    "alt": "Sleepy Kitten",
    "caption": "Cute Kitty"
  }
}

renderers = {}
templates = Environment(loader=FileSystemLoader('templates/'),
                        autoescape=select_autoescape(
                            enabled_extensions=('jinja2'))
                        )


class BaseNode:

    template_path = 'node.jinja2'
    node_type = "prose-mirror_content-type"
    wrap_tag = ""
    css_class = ""

    def __init__(self):
        # self.t = templates[self.type] = templates.get_template(self.template_path)
        self.t = templates.get_template(self.template_path)

    def is_renderable(self, in_data):
        return True

    def render(self, in_data):
        if self.is_renderable(in_data):
            return self.t.render(wrap_tag=self.wrap_tag,
                                 css_class=self.css_class, node=in_data)
        return ''


class Doc(BaseNode):
    node_type = "doc"


def register_renderer(cls):
    renderers[cls.node_type] = cls()


def convert_any(in_data):
    typ = in_data.get("type")
    renderer = renderers.get(typ)
    return renderer.render(in_data)


def to_html(s):
    in_data = s if isinstance(s, dict) else json.loads(s)
    return convert_any(in_data)


if __name__ == "__main__":
    register_renderer(BaseNode)
    register_renderer(Doc)
    print(to_html(simple_json))
