
class Browser:
    def __init__(self):
        self.history = []
        self.current_page = None

    def visit_page(self, url):
        if self.current_page is not None:
            self.history.append(self.current_page)

        self.current_page = url
        print("Visited:", self.current_page)

    def back(self):
        if self.history:
            self.current_page = self.history.pop()
            print("Back to:", self.current_page)
        else:
            print("No previous page available!")

    def show_current_page(self):
        print("Current Page:", self.current_page)


browser = Browser()

browser.visit_page("www.google.com")
browser.visit_page("www.youtube.com")
browser.visit_page("www.github.com")

browser.back()
browser.back()

browser.show_current_page()
