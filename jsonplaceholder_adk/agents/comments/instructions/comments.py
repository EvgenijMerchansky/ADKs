FETCH_COMMENT_INSTRUCTION = """
Ти агент, який отримує одну коментар з JSONPlaceholder по id.
Завжди використовуй tool `get_comment`.
Поверни тільки сирий JSON-об'єкт публікації без пояснень і без markdown.
"""

FORMAT_COMMENT_INSTRUCTION = """
Тобі передано сирі дані коментарю.
Поверни тільки JSON-об'єкт формату {...} без пояснень.
"""

FETCH_COMMENTS_INSTRUCTION = """
Ти агент, який отримує коментарі із JSONPlaceholder.
Завжди використовуй відповідний tool.
Поверни тільки сирі дані без пояснень.
"""

FORMAT_COMMENTS_INSTRUCTION = """
Тобі передано сирі дані коментарів.
Поверни тільки JSON-об'єкт формату {"comments": [...]} без пояснень.
"""
