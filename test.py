from lxml import etree  
  
html = '''  
<html>  
  <head>  
    <title>Example</title>  
  </head>  
  <body>  
    <h1>Welcome to Example.com</h1>  
    <p>This is an example paragraph.</p>  
  </body>  
</html>  
'''  
  
tree = etree.HTML(html)  
  
# 使用 xpath("*") 选择所有元素  
elements = tree.xpath("*")  

def d(node):
    for element in node:
        print(etree.tostring(element))
        if len(element):
            d(element)  
            

d(elements)