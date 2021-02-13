import json

class Kayitlar:
    def __init__(self):
        self.count = 0
        self.dct = {}

    def dictToJson(self, data):
        # Sözlük tipindeki veriyi json'a çevirir.
        return json.dumps(data)

    def jsonToDict(self, data):
        # Json formatındaki veriyi sözlüğe çevirir.
        self.count = 0
        null = {}
        try:
            for i in json.loads(data).keys():
                if int(i) > self.count:
                    self.count = int(i)
            self.count += 1
        except:
            return null
        return json.loads(data)

    def readFile(self, filePath):
        # Dosyayı okuyup içeriğini geri döndürecek
        try:
            f = open(filePath, "r")
            data = f.read()
            f.close()
            return data
        except FileNotFoundError:
            return None

    def writeFile(self, data, filePath):
        # Dosyayı oluşturup içine veri yazacak.
        with open(filePath, "w") as f:
            f.write(data)

    def addKayitlar(self, dct):
        lastDict = {}
        lastData = self.readFile("stdData.json")
        if lastData:
            lastDict = self.jsonToDict(lastData)
        lastDict[self.count] = dct
        newJson = self.dictToJson(lastDict)
        self.writeFile(newJson, "stdData.json")

    def deleteKayitlar(self, name, surname):
        readData = self.readFile("stdData.json")
        jsonData = self.jsonToDict(readData)
        for i in jsonData.keys():
            if jsonData[i]["adi"].lower() == name.lower() and jsonData[i]["soyadi"].lower() == surname.lower():
                del jsonData[i]
                break
            else:
                continue
        dictData = self.dictToJson(jsonData)
        self.writeFile(dictData,"stdData.json")

    def viewKayitlar(self, name, surname):
        readData = self.readFile("stdData.json")
        jsonData = self.jsonToDict(readData)
        for i in jsonData.keys():
            if jsonData[i]["adi"].lower() == name.lower() and jsonData[i]["soyadi"].lower() == surname.lower():
                print("Adı:",jsonData[i]["adi"],"\nSoyadı:",jsonData[i]["soyadi"],"\nYaşadığı Şehit:",jsonData[i]["sehir"],
                      "\nfirma:",jsonData[i]["firma"],"\nMail:",jsonData[i]["mail"],"\nTelefon:",jsonData[i]["tel"],
                      "\nDoğum Tarihi:",jsonData[i]["dogum_tarihi"])
                for a in range(len(jsonData[i]["gecmis"])):
                    print("Gecmis:",jsonData[i]["gecmis"][a])
                break
            else:
                continue

    def uptadeKayitlar(self,name, surname, data):
        readData = self.readFile("stdData.json")
        jsonData = self.jsonToDict(readData)
        for i in jsonData.keys():
            if jsonData[i]["adi"].lower() == name.lower() and jsonData[i]["soyadi"].lower() == surname.lower():
                jsonData[i] = data
                break
            else:
                continue
        dictData = self.dictToJson(jsonData)
        self.writeFile(dictData, "stdData.json")

    def allKayitlar(self):
        readData = self.readFile("stdData.json")
        jsonData = self.jsonToDict(readData)
        for i in jsonData.keys():
            print("\n","#" * 40)
            print("Adı:", jsonData[i]["adi"], "\nSoyadı:", jsonData[i]["soyadi"], "\nYaşadığı Şehit:",
                  jsonData[i]["sehir"],
                  "\nFirma:", jsonData[i]["firma"], "\nMail:", jsonData[i]["mail"], "\nTelefon:", jsonData[i]["tel"],
                  "\nDoğum Tarihi:", jsonData[i]["dogum_tarihi"])
            for a in range(len(jsonData[i]["gecmis"])):
                print("Gecmis:", jsonData[i]["gecmis"][a])
