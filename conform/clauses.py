import ast


class Clause(object):
    pass


def assert_not_none(var, exception_type='Exception', exception_msg='Generic Exception'):
    return ast.If(
        test=compare_is(var, 'None'),
        body=[
            ast.Raise(
                type=ast.Call(
                    func=ast.Name(id=exception_type, ctx=ast.Load(), lineno=1, col_offset=0),
                    args=[ast.Str(s=exception_msg, lineno=1, col_offset=0)],
                    keywords=[],
                    starargs=None,
                    kwargs=None,
                    lineno=1,
                    col_offset=0),
                inst=None,
                tback=None,
                lineno=1,
                col_offset=0
            )
        ],
        orelse=[],
        lineno=1,
        col_offset=0
    )


def return_static(var):
    return ast.Return(value=ast.Name(id=var, ctx=ast.Load(), lineno=1, col_offset=0), lineno=1, col_offset=0)


def return_static_if(test, static):
    return ast.If(
        test=test,
        body=[return_static(static)],
        orelse=[],
        lineno=1,
        col_offset=0,
    )


def compare_is(left, right, invert=False):
    return ast.Compare(
        left=ast.Name(id=left, ctx=ast.Load(), lineno=1, col_offset=0),
        ops=[ast.Is() if not invert else ast.IsNot()],
        comparators=[ast.Name(id=right, ctx=ast.Load(), lineno=1, col_offset=0)],
        lineno=1,
        col_offset=0)


def stmt_if(test, body, orelse=None):
    return ast.If(
        test=test,
        body=body,
        orelse=orelse or [],
        lineno=1,
        col_offset=0
    )


def stmt_return(value):
    return ast.Return(value=value, lineno=1, col_offset=0)


def call(func, args):
    return ast.Call(
        func=func,
        args=args,
        keywords=[],
        starargs=None,
        kwargs=None,
        lineno=1,
        col_offset=0
    )


def name(v):
    return ast.Name(id=v, ctx=ast.Load(), lineno=1, col_offset=0)


def attr(left, right):
    return ast.Attribute(value=name(left), attr=right, lineno=1, col_offset=0, ctx=ast.Load())


def str(s):
    return ast.Str(s=s, lineno=1, col_offset=0)
