class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []
    
    def add_product(self, product: str):
        self.products.append(product)
        
    def get_by_letter(self, letter: str):
        first_letter_lst =[ele for ele in self.products if ele.startswith(letter)]
        return first_letter_lst
    
    def __repr__(self):
        sorted_lst = sorted(self.products)
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(sorted_lst)
    
    
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)