"""Convert stacked single-line // comments into /* */ block comments.

A "stacked" comment is a run of two or more consecutive lines that each begin
(after optional leading whitespace) with //. Each such run is rewritten as one
/* ... */ block: the first line's // becomes /*, the marker is stripped from the
following lines, and */ is appended to the last line. Lone single-line // comments
and inline trailing comments (code before the //) are left untouched.

Leading whitespace and line endings (LF or CRLF) are preserved exactly, so the
diff is limited to the comment lines themselves. // that appears inside a string
literal (e.g. the glob "data/players/*") is never a line-start comment, so it is
safely ignored.

Usage:
    python scripts/block_comments.py <file.nvgt> [more_files ...]
"""
import re, sys


def convert(path):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        data = f.read()

    # Split ONLY on \n so joining with \n reproduces the file byte-for-byte.
    # CRLF lines keep a trailing '\r' as part of the element.
    parts = data.split('\n')

    def body_of(part):
        return part[:-1] if part.endswith('\r') else part

    def is_comment(part):
        return re.match(r'^\s*//', body_of(part)) is not None

    out = []
    i, n = 0, len(parts)
    changed_blocks = 0
    while i < n:
        if is_comment(parts[i]):
            j = i
            while j < n and is_comment(parts[j]):
                j += 1
            runlen = j - i
            if runlen >= 2:
                changed_blocks += 1
                for k in range(i, j):
                    part = parts[k]
                    cr = '\r' if part.endswith('\r') else ''
                    body = body_of(part)
                    if k == i:
                        body = re.sub(r'^(\s*)//', r'\1/*', body, count=1)   # open
                    else:
                        body = re.sub(r'^(\s*)// ?', r'\1', body, count=1)   # strip marker (+ one space)
                    if k == j - 1:
                        body = body + ' */'                                  # close
                    out.append(body + cr)
            else:
                out.extend(parts[i:j])
            i = j
        else:
            out.append(parts[i]); i += 1

    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(out))
    return changed_blocks


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    for path in argv[1:]:
        blocks = convert(path)
        print(f"{path}: converted {blocks} block(s)")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
