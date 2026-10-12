"""I asked the AI how to correctly apply the tag in the output."""

def tagcheck(tag: str, line: str) -> str:
    tags = {"a", "abbr", "b", "body", "caption", "cite", "code", "div",
            "form", "h1", "h2", "h3", "h4", "h5", "h6", "header", "i", "s"}

    if tag in tags:
        return f"<{tag}>{line}</{tag}>"
    return "Wrong tag"

tag = str(input())
line = str(input())

print(tagcheck(tag, line))
