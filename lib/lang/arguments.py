#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[lib/lang/arguments.py]

"""

def get_args_kwargs(tokenized_block, pipe):
    args = tokenized_block[0][1:]
    kwargs = {s.split(":")[0]:s.split(":")[1] for s in tokenized_block[1]}
    try:
        if tokenized_block[0][1:][0].startswith("--"):
            selectors = tokenized_block[0][1:][0].split(",")
            if "--arg" in selectors:
                args = pipe.getstack_args(-1) + args[1:]
            elif "--kw" in selectors:
                kwargs.update(pipe.getstack_kwargs(-1))
    except IndexError:
        pass
    return args, kwargs