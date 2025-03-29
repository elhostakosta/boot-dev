from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line


def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            content = content.replace("# ", "<h1>")
            content += "</h1>"
            return content 
        case (DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"
        case (DocFormat.HTML, DocFormat.MD):
            content = (content.replace("<h1>", "# ")).replace("</h1>", "")
            return content
        case _:
            raise Exception("Invalid type")
