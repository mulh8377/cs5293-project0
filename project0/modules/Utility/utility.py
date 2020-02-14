import toss_hash as th
import toss_download as td


if __name__ == "__main__":
    res = th.toss64_encoder("hello world")
    print(res)
    dec = th.toss64_decoder(res)
    print(dec)

    print(th.toss64_equality(dec, res))

    print(td.get_report("http://normanpd.normanok.gov/filebrowser_download/657/2020-02-11%20Daily%20Incident%20Summary.pdf", "../../../tests/"))