#! /usr/bin/env python3

def hello_world(name1="Ion", name2="Maria") -> str:
    return f"Hello World {name1} {name2}"

print(hello_world(name2="Maria", name1="Ion"))
hello_world()