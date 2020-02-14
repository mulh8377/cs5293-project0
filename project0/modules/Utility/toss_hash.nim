import base64
import nimpy

proc toss64_encoder(msg: string): string {.exportpy.} =
  assert msg.len > 0
  return encode(msg)

proc toss64_decoder(hash: string): string {.exportpy.} =
  assert hash.len > 0
  return decode(hash)

proc toss64_equality(msg: string, hash: string): bool {.exportpy.} =
  assert msg.len > 0
  assert hash.len > 0
  return encode(msg) == hash

