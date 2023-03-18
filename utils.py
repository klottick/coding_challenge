import ast

# used https://docs.python.org/3.8/library/ast.html#


def get_function_text_from_file(path: str) -> dict:
    """Given a path to a python file, parses the functions within and returns them in a dictionary

    Args:
        path (str): path to the file to be parsed.

    Returns:
        dict: dictionary where keys are function names and values are the text of the function
    """
    ans = {}
    with open(path) as file:
        source = file.read()
        tree = ast.parse(source, type_comments=True)
        for node in ast.iter_child_nodes(tree):
            if type(node) == ast.FunctionDef:
                ans[node.name] = ast.get_source_segment(source, node, padded=True)
    return ans


if __name__ == "__main__":
    print(get_function_text_from_file("coding_challenge/questions.py"))
