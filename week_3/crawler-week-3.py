#!/usr/bin/python
# coding: utf-8
import urllib.request
import ssl
import json


def main():
    context = ssl._create_unverified_context()
    req = urllib.request.urlopen(
        "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json",
        context=context,
    )
    data = json.load(req)
    clist = data["result"]["results"]

    with open("data.csv", mode="w") as file:
        for list in clist:
            # 抓取區域
            dataSeparation = list["address"].split()
            dataSeparationFirst = dataSeparation[1]
            dataArea = dataSeparation[1].index("區")
            dataAddress = dataSeparationFirst[0 : dataArea + 1]

            # 抓取圖片
            imgSeparation = list["file"].split("https")
            imgSeparationFirst = imgSeparation[1]
            img = "https" + imgSeparationFirst

            file.write(
                "{"
                + "stitle"
                + ":"
                + list["stitle"]
                + ", "
                + "area"
                + ":"
                + dataAddress
                + ", "
                + "longitude"
                + ":"
                + list["longitude"]
                + ", "
                + "latitude"
                + ":"
                + list["latitude"]
                + ", "
                + "image"
                + ":"
                + img
                + ", "
                + "}"
                + "\n"
            )


if __name__ == "__main__":
    main()
