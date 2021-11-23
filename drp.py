import os
import dropbox
import datetime

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

with open("source.html") as f:
  template = f.read()

p = pages.split()[1]
t = str(datetime.datetime.now())
finished = os.environ.get("FINISHED")
when = os.environ.get("WHEN")
with open("build/index.html", "w") as f:
  f.write(template.format(date=t, pages=p, finished=finished, when=when))
