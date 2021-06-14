# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self):
        # Insert the node as before
        pass

    def __str__(self):
        return f"{self.children}-{self.handler}"


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        pass

    def find(self):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        pass


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root, not_found_root):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie()
        self.root_handler = root
        self.not_root_handler = not_found_root

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        current_node = self.router.root
        path = path.split('/')
        for url in path:
            if url and not current_node.children.get(url):
                current_node.children[url] = RouteTrieNode()

                current_node = current_node.children[url]
        current_node.handler = handler

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        current_node = self.router.root

        if path == '/':
            return self.root_handler
        path = path.split('/')[1:]
        for url in path:
            if url not in current_node.children:
                return self.not_root_handler
            current_node = current_node.children[url]

        return current_node.handler if current_node.handler else self.not_root_handler

    def split_path(self):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        pass

    def __str__(self):
        children_list = []
        current_node = self.router.root

        while current_node.children:
            for key, value in current_node.children.items():
                children_list.append([key, str(value)])
            # children_list.append(current_node.children.items())
            key = list(current_node.children.keys())[0]
            current_node = current_node.children[key]

        return f"root_handler: {self.root_handler}" \
               f"not_root_handler: {self.not_root_handler}" \
               f"router: {children_list}"


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route


# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
