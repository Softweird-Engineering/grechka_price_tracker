"""
Product NamedTuple. Defines structure of parsing result.
"""
import collections

product_fields = ['title', 'cost', 'price', 'weight', 'image_link', 'website_url', 'website_title', 'manufacturer']
Product = collections.namedtuple("Product", product_fields)

Product.__doc__ = """
Product: buckwheat
fields description:
- title : displayed title
- price : overall cost of 1 entity
- cost : cost of 1 kg
- weight : weight of certain entity
- image_link : link to external image of product
- website_url : website url with product
- website_title : displaying title of certain website
- manufacturer : company
"""