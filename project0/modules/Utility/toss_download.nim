import nimpy

template with_open(name: string, mode: char, body: untyped) =
  let flag = if mode == 'w': fmWrite else: fmRead  # "flag" dont exist outside of this template
  let file {.inject.} = open(name, flag)   # Create and inject "file" variable, "file" variable exists outside of this template because {.inject.}
  body                                     # "body" is code passed as argument
  file.close()                             # Code after code passed as argument

proc open_file*(): seq[string] {.exportpy.} =
 var urls = newSeq[string]()
 let fp = "/home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/data/txt/urls.txt"
 with_open(fp, 'r'): # Mimic Python with open("file", mode='r') as file
    urls.add(file.readAll())# Code inside the template, this 2 lines are "body" argument on the template   # This line uses "file" variable

 return urls