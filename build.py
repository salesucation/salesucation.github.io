from app import app, pages
import os
import shutil

client = app.test_client();

def load(path):
    res = client.get(path)
    if path.endswith("index"):
        path = path.replace("index", "")
    try:
        os.makedirs(f"{os.getcwd()}/dist/{path}")
    except:
        pass
    f = open(f"{os.getcwd()}/dist/{path}/index.html", "wb")
    f.write(res.data)  
    f.close()

if os.path.exists(f"{os.getcwd()}/dist"):
    shutil.rmtree(f"{os.getcwd()}/dist")
shutil.copytree(f"{os.getcwd()}/static", f"{os.getcwd()}/dist/static")
for page in pages:
    load(page.path)
