import os
from css_html_js_minify import css_minify, js_minify

def minimize_css(file_path):
    """Minimizes a CSS file and saves the output with '_min' appended to the filename.

    Args:
        file_path (str): Path to the CSS file.
    """
    try:
        with open(file_path, 'r') as file:
            css_content = file.read()

        minimized_css = css_minify(css_content)
        base_name, ext = os.path.splitext(file_path)
        output_file = f"{base_name}_min{ext}"

        with open(output_file, 'w') as file:
            file.write(minimized_css)

        print(f"CSS minimized: {output_file}")
    except Exception as e:
        print(f"Error minimizing CSS: {e}")


def minimize_js(file_path):
    """Minimizes a JavaScript file and saves the output with '_min' appended to the filename.

    Args:
        file_path (str): Path to the JavaScript file.
    """
    try:
        with open(file_path, 'r') as file:
            js_content = file.read()

        minimized_js = js_minify(js_content)
        base_name, ext = os.path.splitext(file_path)
        output_file = f"{base_name}_min{ext}"

        with open(output_file, 'w') as file:
            file.write(minimized_js)

        print(f"JavaScript minimized: {output_file}")
    except Exception as e:
        print(f"Error minimizing JavaScript: {e}")


if __name__ == "__main__":
    # Example usage
    css_file = "../output/style.css"  # Replace with the actual CSS file path
    js_file = "../output/script.js"    # Replace with the actual JS file path

    minimize_css(css_file)
    minimize_js(js_file)
