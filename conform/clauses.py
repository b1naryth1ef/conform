import ast


class Clause(object):
    pass


class EnsureNotNone(Clause):
    def compile(self):
        yield ast.If(
                test=ast.Compare(
                    left=ast.Name(id='value', ctx=ast.Load(), lineno=1, col_offset=3),
                    ops=[ast.Is()],
                    comparators=[ast.Name(id='None', ctx=ast.Load(), lineno=1, col_offset=12)],
                    lineno=1,
                    col_offset=3),
                body=[
                    ast.Raise(
                        type=ast.Call(
                            func=ast.Name(id='Exception', ctx=ast.Load(), lineno=1, col_offset=24),
                            args=[ast.Str(s='test', lineno=1, col_offset=34)],
                            keywords=[],
                            starargs=None,
                            kwargs=None,
                            lineno=1,
                            col_offset=24),
                        inst=None,
                        tback=None,
                        lineno=1,
                        col_offset=18
                    )
                ],
                orelse=[],
                lineno=1,
                col_offset=0
            )
