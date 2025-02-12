def statement_generator(statement, decoration):
    """Add decorations to the start and end of headings"""
    ends = decoration * 3
    print(f"{ends} {statement} {ends}")


statement_generator("Roll It 13", "🐟")
statement_generator("Round results", "=")
