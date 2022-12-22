if __name__ == "__main__":
    with open("input") as f:
        compile_chain([
            (Parser, "start"),
            (ToExpression, "start"),
            (Simplify, "start"),

            (Expand, "start"),
            (Simplify, "start"),
            (Simplify, "start"),
            (Simplify, "start"),

            (Expand, "start"),
            (Simplify, "start"),
            (Simplify, "start"),
            (Simplify, "start"),

            (Expand, "start"),
            (Simplify, "start"),
            (Simplify, "start"),
            (Simplify, "start"),
            (Simplify, "start"),

            #(RemoveUnusedTmps, "start"),
            (Pretty, "start"),
        ], f.read(), debug=True)
