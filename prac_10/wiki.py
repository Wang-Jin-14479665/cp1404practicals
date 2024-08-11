from wikipedia import wikipedia

title = input("Enter a Wikipedia page title or search phrase (or just press enter to exit): ")
while title != "":
    print(title)

    page = wikipedia.page(title, auto_suggest=False)
    print(f"Title: {page.title}")
    print(f"Summary: {page.summary}")
    print(f"URL: {page.url}")

    title = input("Enter a Wikipedia page title or search phrase (or just press enter to exit): ")
