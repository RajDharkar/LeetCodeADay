## Notes

We utilize a stack to figure out the open and closed parentheses, brackets, or other delimiters.

A stack is Last In, First Out, or LIFO, meaning that when we put data in a stack, the last data added is processed first.

For the test case `{{[]()}[]}`, we can create a stack as follows:

1. **[{]** — We push the first `{` onto the stack.
2. **[{, {]** — We push the second `{` onto the stack.
3. **[{, {, []** — We encounter `[`, so we push it onto the stack.
4. **[{, {]** — We encounter `]`, so we pop `[`.
5. **[{, {, (]** — We encounter `(`, so we push it onto the stack.
6. **[{, {]** — We encounter `)`, so we pop `(`.
7. **[{]** — We encounter `}`, so we pop `{`.
8. **[{, []** — We push another `[`.
9. **[{, [, ]** — We encounter `]`, so we pop `[`.
10. **[{]** — We encounter `}`, so we pop `{`.

Since the stack is empty at the end, this confirms that our delimiters are balanced.