import unittest

import os
import markdown


class TestMDI(unittest.TestCase):
    def test_vanilla(self):
        text = "I love &icon-html5; and &icon-css3;."
        expected = '<p>I love <i aria-hidden="true" class="icon-html5"></i> and <i aria-hidden="true" class="icon-css3"></i>.</p>'

        md = markdown.Markdown(extensions=["iconfonts"])
        converted_text = md.convert(text)

        self.assertEqual(converted_text, expected)

    def test_vanilla_mod(self):
        text = "I also love &icon-spinner:spin; &icon-spinner:2x,spin;\n&icon-spinner:large,spin; Sorry we have to load..."
        expected = '<p>I also love <i aria-hidden="true" class="icon-spinner icon-spin"></i> <i aria-hidden="true" class="icon-spinner icon-2x icon-spin"></i>\n<i aria-hidden="true" class="icon-spinner icon-large icon-spin"></i> Sorry we have to load...</p>'

        md = markdown.Markdown(extensions=["iconfonts"])
        converted_text = md.convert(text)

        self.assertEqual(converted_text, expected)

    def test_vanilla_user_mod(self):
        text = "I also love &icon-spinner:spin:red; &icon-spinner:2x,spin:bold;\n&icon-spinner:large,spin; Sorry we have to load..."
        expected = '<p>I also love <i aria-hidden="true" class="icon-spinner icon-spin red"></i> <i aria-hidden="true" class="icon-spinner icon-2x icon-spin bold"></i>\n<i aria-hidden="true" class="icon-spinner icon-large icon-spin"></i> Sorry we have to load...</p>'

        md = markdown.Markdown(extensions=["iconfonts"])
        converted_text = md.convert(text)

        self.assertEqual(converted_text, expected)

    def test_prefix_base_pairs_setting(self):
        text = "I also love &fa-spinner:2x,spin:red; &glyphicon-remove::bold;\n&fa-spinner:large,spin; Sorry we have to load..."
        expected = '<p>I also love <i aria-hidden="true" class="fa fa-spinner fa-2x fa-spin red"></i> <i aria-hidden="true" class="glyphicon glyphicon-remove bold"></i>\n<i aria-hidden="true" class="fa fa-spinner fa-large fa-spin"></i> Sorry we have to load...</p>'

        md = markdown.Markdown(
            extensions=["iconfonts"],
            extension_configs={
                "iconfonts": {
                    "prefix": "icon-",
                    "base": "icon",
                    "prefix_base_pairs": {
                        "fa-": "fa",
                        "glyphicon-": "glyphicon",
                    },
                }
            },
        )
        converted_text = md.convert(text)

        self.assertEqual(converted_text, expected)

    def test_prefix_base_pairs_setting_with_normal_prefix_and_base_settings(
        self
    ):
        text = "I also love &fa-spinner:2x,spin:red; &glyphicon-remove::bold;\n&icon-spinner:large,spin; Sorry we have to load..."
        expected = '<p>I also love <i aria-hidden="true" class="fa fa-spinner fa-2x fa-spin red"></i> <i aria-hidden="true" class="glyphicon glyphicon-remove bold"></i>\n<i aria-hidden="true" class="icon icon-spinner icon-large icon-spin"></i> Sorry we have to load...</p>'

        md = markdown.Markdown(
            extensions=["iconfonts"],
            extension_configs={
                "iconfonts": {
                    "prefix": "icon-",
                    "base": "icon",
                    "prefix_base_pairs": {
                        "fa-": "fa",
                        "glyphicon-": "glyphicon",
                    },
                }
            },
        )
        converted_text = md.convert(text)

        self.assertEqual(converted_text, expected)

    def test_custom_prefix(self):
        text = "I love &mypref-html5; and &mypref-css3;."
        expected = '<p>I love <i aria-hidden="true" class="mypref-html5"></i> and <i aria-hidden="true" class="mypref-css3"></i>.</p>'

        md = markdown.Markdown(
            extensions=["iconfonts"],
            extension_configs={"iconfonts": {"prefix": "mypref-"}},
        )
        converted_text = md.convert(text)

        self.assertEqual(converted_text, expected)

    def test_custom_prefix_mod(self):
        text = "I also love &mypref-spinner:spin; &mypref-spinner:2x,spin;\n&mypref-spinner:large,spin; Sorry we have to load..."
        expected = '<p>I also love <i aria-hidden="true" class="mypref-spinner mypref-spin"></i> <i aria-hidden="true" class="mypref-spinner mypref-2x mypref-spin"></i>\n<i aria-hidden="true" class="mypref-spinner mypref-large mypref-spin"></i> Sorry we have to load...</p>'

        md = markdown.Markdown(
            extensions=["iconfonts"],
            extension_configs={"iconfonts": {"prefix": "mypref-"}},
        )
        converted_text = md.convert(text)

        self.assertEqual(converted_text, expected)

    def test_base(self):
        text = "I love &icon-html5; and &icon-css3;."
        expected = '<p>I love <i aria-hidden="true" class="icon icon-html5"></i> and <i aria-hidden="true" class="icon icon-css3"></i>.</p>'

        md = markdown.Markdown(
            extensions=["iconfonts"],
            extension_configs={"iconfonts": {"base": "icon"}},
        )
        converted_text = md.convert(text)

        self.assertEqual(converted_text, expected)

    def test_complex(self):
        text = "I love &fa-html5; and &fa-css3;."
        expected = '<p>I love <i aria-hidden="true" class="fa fa-html5"></i> and <i aria-hidden="true" class="fa fa-css3"></i>.</p>'

        md = markdown.Markdown(
            extensions=["iconfonts"],
            extension_configs={"iconfonts": {"prefix": "fa-", "base": "fa"}},
        )
        converted_text = md.convert(text)

        self.assertEqual(converted_text, expected)


"""
# Save to file
BASE_DIR = os.path.realpath(os.path.dirname(__file__))
with open(os.path.join(BASE_DIR, 'output.txt'), "w") as text_file:
	text_file.write(str(converted_text))
"""


if __name__ == "__main__":
    unittest.main()
