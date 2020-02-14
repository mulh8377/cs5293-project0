import httpclient
import os
import nimpy

proc get_report(u: string, path: string): string {.exportpy.} =
 let c = HttpClient()
 downloadFile(c, u, path)
 return path