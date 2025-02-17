from app import app, pages
import os
import shutil
import json
import xml.etree.ElementTree as ET
import urllib.parse;

client = app.test_client();

def load(path, sitemap):
    res = client.get(path)
    if path.endswith("index"):
        path = path.replace("index", "")
    elif path == "404":
        f = open(f"{os.getcwd()}/dist/404.html", "wb")
        sitemap["urlset"].append({"url":{"loc": f"/404.html"}})
        f.write(res.data)  
        f.close()
        return
    else:
        path += "/"
    try:
        os.makedirs(f"{os.getcwd()}/dist/{path}")
    except:
        pass
    f = open(f"{os.getcwd()}/dist/{path}index.html", "wb")
    sitemap["urlset"].append({"url":{"loc": f"/{path}"}})
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
XML = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset>';
for url in sitemap["urlset"]:
    XML += f"<url><loc>{oPackage["homepage"]}{url["url"]["loc"]}</loc></url>"
XML += "</urlset>"
element = ET.XML(XML)
ET.indent(element)
f = open(f"{os.getcwd()}/dist/sitemap.xml", "w")
f.write(ET.tostring(element, encoding='unicode'))
f.close()
parsed_url = urllib.parse.urlparse(oPackage["homepage"])
f = open(f"{os.getcwd()}/dist/CNAME", "w")
f.write(parsed_url.netloc)
f.close()