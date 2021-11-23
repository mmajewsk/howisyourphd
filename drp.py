import os
import dropbox

token = os.environ.get("DRP_AUTH_TOKEN")
dbx = dropbox.Dropbox(token)


with open("dis.pdf", "wb") as f:
    metadata, res = dbx.files_download(path="/Apps/Overleaf/phd_thesis_mmajewski/dissertation.pdf")
    f.write(res.content)
stream = os.popen('pdfinfo dis.pdf | grep "Pages:"')
pages = stream.read()

if os.path.exists("dis.pdf"):
  os.remove("dis.pdf")
else:
  print("The file does not exist")

with open("build/pages.html", "w") as f:
    f.write(pages)
