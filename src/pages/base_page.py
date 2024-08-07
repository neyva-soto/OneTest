class BasePage(object):

    def __init__(self, context):
        self.context = context

    def find_element(self, locator):
        return self.context.page.locator(locator)