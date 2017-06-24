from __future__ import absolute_import, print_function

import ast
from types import FunctionType, CodeType

import six

from conform import clauses


class BaseType(object):
    def __init__(self, required=False):
        self.required = required

    def compile_load(self, name='f'):
        # First gather a set of clauses
        _clauses = []

        if self.required:
            _clauses.append(clauses.assert_not_none(
                'value',
            ))
        else:
            _clauses.append(clauses.return_static_if(
                clauses.compare_is('value', 'None'),
                'None'
            ))

        for clause in self._compile_load_clauses():
            _clauses.append(clause)

        # _clauses.append(clauses.return_static('value'))

        print(_clauses)

        # Now we generate a function with a body containing our clauses
        func = ast.FunctionDef(
                name=name,
                args=ast.arguments(
                    args=[ast.Name(id='value', ctx=ast.Param(), lineno=1, col_offset=9)],
                    vararg=None,
                    kwarg=None,
                    defaults=[],
                ),
                body=_clauses,
                decorator_list=[],
                lineno=1,
                col_offset=0)

        module_ast = ast.Module(body=[func])

        module_code = compile(module_ast, "<not_a_file>", "exec")
        function_code = [c for c in module_code.co_consts if isinstance(c, CodeType)][0]
        return FunctionType(function_code, globals())


class TextType(BaseType):
    def _compile_load_clauses(self):
        if six.PY2:
            # If the instance is that of a string (e.g. raw bytes) we must decode
            #  it as a unicode string.
            yield clauses.stmt_if(
                clauses.call(clauses.name('isinstance'), [clauses.name('value'), clauses.name('str')]),
                [clauses.stmt_return(
                    clauses.call(clauses.attr('value', 'decode'), [clauses.str('utf-8')])
                )]
            )
            # Otherwise we just want to cast to unicode
            # TODO: try catch ?
            yield clauses.stmt_return(
                clauses.call(clauses.name('unicode'), [clauses.name('value')])
            )
        else:
            yield clauses.stmt_return(
                clauses.call(clauses.name('str'), [clauses.name('value')])
            )


class IntType(BaseType):
    def _compile_load_clauses(self):
        yield clauses.stmt_try_except(
            [clauses.stmt_return(clauses.call(clauses.name('int'), [clauses.name('value')]))],
            {
                'ValueError': [clauses.stmt_raise(clauses.call(
                    clauses.name('Exception'),
                    [clauses.str('bad number bro')]
                ))]
            }
        )
