class BrowserHistory:
    def __init__(self):
        self.capacity = 10
        self.history = []   # our array-based stack

    # ── helpers ──────────────────────────────────────────
    def _isFull(self):
        return len(self.history) == self.capacity

    def _isEmpty(self):
        return len(self.history) == 0

    # ── primitive operations ──────────────────────────────
    def visitPage(self, url):
        """Push a new URL onto the stack."""
        if self._isFull():
            print(f"  History full! Cannot visit '{url}'")
            return
        self.history.append(url)
        print(f"  Visited  --> {url}")

    def goBack(self):
        """Pop the current page and return to the previous one."""
        if self._isEmpty():
            print("  Cannot go back — no history available.")
            return
        left = self.history.pop()
        print(f"  Going back... (left '{left}')")

    def currentPage(self):
        """Peek at the top of the stack (active page)."""
        if self._isEmpty():
            print("  No page is currently open.")
            return
        print(f"  Current page --> {self.history[-1]}")


# ── Test Case ─────────────────────────────────────────────
print("=" * 45)
print("       Browser History Simulation")
print("=" * 45)

browser = BrowserHistory()

print("\n[ Navigating to pages... ]")
browser.visitPage("pageA.com")
browser.visitPage("pageB.com")
browser.visitPage("pageC.com")

print("\n[ Pressing Back button... ]")
browser.goBack()                  # leaves pageC, goes to B

print("\n[ Checking current page... ]")
browser.currentPage()             # should be pageB.com

print("\n[ Pressing Back button again... ]")
browser.goBack()                  # leaves pageB, goes to A

print("\n[ Checking current page... ]")
browser.currentPage()             # should be pageA.com

print("\n[ Pressing Back two more times... ]")
browser.goBack()                  # leaves pageA
browser.goBack()                  # stack empty — edge case

print("\n[ Checking current page on empty history... ]")
browser.currentPage()

print("\n" + "=" * 45)