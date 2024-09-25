# Wagtail FA SVG

[![Python](https://img.shields.io/badge/python-3.10+-4d4076.svg)](https://www.python.org/downloads/)
[![Wagtail](https://img.shields.io/badge/wagtail-5.0+-4d4076)](https://github.com/wagtail/wagtail)
[![License](https://img.shields.io/badge/license-MIT-4d4076)](https://github.com/vsakkas/wagtail-fa-svg/blob/master/LICENSE)

Font Awesome SVG icons for Wagtail.

## Installation

To install, run the following command:

```bash
poetry add wagtail-fa-svg
```

> [!TIP]
> Make sure you're using the latest version to access the latest Font Awesome icons.

## Usage

Add `wagtail_fa_svg` to your installed apps:

```python
INSTALLED_APPS = [
    "wagtail_fa_svg",
]
```

Create a hook in your `wagtail_hooks.py` file to register icons:

```python
from wagtail import hooks

@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        "wagtail-fa-svg/v6/brands/github.svg",
        "wagtail-fa-svg/v6/regular/pilcrow.svg",
        "wagtail-fa-svg/v5/solid/columns.svg",
    ]
```

> [!NOTE]
> Both Font Awesome 5 and 6 icons are supported.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/vsakkas/wagtail-fa-svg/blob/master/LICENSE) file for details.

The Font Awesome icons and related files are licensed under the [Font Awesome Free License](https://fontawesome.com/license/free).
