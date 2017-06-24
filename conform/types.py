from __future__ import absolute_import

import ast
from types import FunctionType, CodeType

from conform import clauses


class BaseType(object):
    def __init__(self, required=False):
        self.required = required

    def compile_load(self, name='f'):
        ast_clauses = []
        for clause in self._compile_load_clauses():
            for ast_clause in clause().compile():
                ast_clauses.append(ast_clause)

        func = ast.FunctionDef(
                name=name,
                args=ast.arguments(
                    args=[ast.Name(id='value', ctx=ast.Param(), lineno=1, col_offset=9)],
                    vararg=None,
                    kwarg=None,
                    defaults=[],
                    ),
                body=ast_clauses,
                decorator_list=[],
                lineno=1,
                col_offset=0)

        module_ast = ast.Module(body=[func])

        module_code = compile(module_ast, "<not_a_file>", "exec")
        function_code = [c for c in module_code.co_consts if isinstance(c, CodeType)][0]
        return FunctionType(function_code, globals())

    def _compile_load_clauses(self):
        base = []

        if self.required:
            base.append(clauses.EnsureNotNone)

        return base


class TextType(BaseType):
    def _compile_load_clauses(self):
        return super(TextType, self)._compile_load_clauses()
