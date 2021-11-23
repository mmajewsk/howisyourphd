import os
import dropbox

token = os.environ.get("DRP_AUTH_TOKEN")
print(token[:3])
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

with open("pages.txt", "w") as f:
    f.write(pages)
