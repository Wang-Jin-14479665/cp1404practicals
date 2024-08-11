from wikipedia import wikipedia

title = input("Enter a Wikipedia page title or search phrase (or just press enter to exit): ")
while title != "":
    print(title)

    try:
        page = wikipedia.page(title, auto_suggest=True)
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")
    except wikipedia.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.PageError:
        print(f"Page id \"{title}\" does not match any pages. Try another id!\n")

    title = input("Enter a Wikipedia page title or search phrase (or just press enter to exit): ")
print("Thank you.")