"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    """Create stylesheet and javascript bundles."""
    assets.auto_build = True
    assets.debug = True
    common_style_bundle = Bundle(
        "src/less/*.less",
        filters="less,cssmin",
        output="dist/css/style.css",
        extra={"rel": "stylesheet/less"},
    )
    home_style_bundle = Bundle(
        "home_bp/less/home.less",
        filters="less,cssmin",
        output="dist/css/home.css",
        extra={"rel": "stylesheet/less"},
    )

    js_bundle = Bundle(
        'src/js/map_yandex.js',
        output='dist/js/map_yandex.js'
    )

    # Register style bundle
    assets.register("common_style_bundle", common_style_bundle)
    assets.register("home_style_bundle", home_style_bundle)

    # Register js bundle
    assets.register('main_js', js_bundle)

    # Build styles and javascript
    if app.config["FLASK_ENV"] == "development":
        common_style_bundle.build()
        home_style_bundle.build()
        js_bundle.build()
    return assets
