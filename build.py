from app import app, pages
import os
import shutil
import json
import xml.etree.ElementTree as ET

client = app.test_client();

def load(path, sitemap):
    res = client.get(path)
    if path.endswith("index"):
        path = path.replace("index", "")
    else:
        path += "/"
    try:
        os.makedirs(f"{os.getcwd()}/dist/{path}")
    except:
        pass
    f = open(f"{os.getcwd()}/dist/{path}index.html", "wb")
    sitemap["urlset"].append({"url":{"loc": f"/{path}index.html"}})
    f.write(res.data)  
    f.close()

if os.path.exists(f"{os.getcwd()}/dist"):
    shutil.rmtree(f"{os.getcwd()}/dist")
shutil.copytree(f"{os.getcwd()}/static", f"{os.getcwd()}/dist/static")
sitemap = {"urlset":[]};
for page in pages:
    load(page.path, sitemap)

fin = open(f"{os.getcwd()}/package.json")
oPackage = json.load(fin)
fin.close()
XML = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">';
for url in sitemap["urlset"]:
    XML += f"<url><loc>{oPackage["homepage"]}{url["url"]["loc"]}</loc></url>"
XML += "</urlset>"
element = ET.XML(XML)
ET.indent(element)
f = open(f"{os.getcwd()}/dist/sitemap.xml", "w")
f.write(ET.tostring(element, encoding='unicode'))
f.close()
