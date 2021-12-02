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

_olist_json = {
  "type": "doc",
  "content": [
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


