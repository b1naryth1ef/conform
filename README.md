# conform

conform is a data modeling and validation library that is aimed at being (perhaps overly) performant.

## how

Unlike other data modeling libraries which use pesky meta programming, conform uses meta-meta programming by generating AST nodes and compiling them into functions that can be used at runtime. This avoids extra loops or if statements that are generally seen within other modeling loaders.

## that... is the worst

yup.
