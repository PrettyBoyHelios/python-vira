import json
import os
import tempfile

import requests
from dotenv import load_dotenv


class ViraAPI:
    def __init__(self, url=""):
        if url == "":
            load_dotenv()
            url = os.getenv("API_URL")
            if url == "":
                raise Exception("no base url provided for Vira API")
        self.base_url = url

    def get_invoice_files(self, letter):
        facturama_id = letter['cfdi']
        pdf = requests.get("{}/cfdi/{}.pdf".format(self.base_url, facturama_id)).content
        xml = requests.get("{}/cfdi/{}.xml".format(self.base_url, facturama_id)).content
        return pdf, xml

    def create_notification(self, title, body, uid, admin=True):
        data = {"title": title, "body": body}
        print("{}/services/notifications".format(self.base_url))
        res = requests.post("{}/services/notifications".format(self.base_url), json=data, headers={"uid": uid})
        print(res)

    def get_original_letter(self, letter_id):
        og_letter_path = requests.get("{}/services/letters/pdf/{}".format(self.base_url, letter_id)).text
        og_letter_path = og_letter_path.replace("\"", "")
        print(og_letter_path)
        og_letter = requests.get(og_letter_path).content
        print(og_letter)
        pdf_path = tempfile.NamedTemporaryFile(suffix='.pdf').name
        with open(pdf_path, 'wb') as f:
            print("temp of letter: ", pdf_path)
            f.write(og_letter)
        return og_letter, pdf_path

    def update_letter(self, letter_id, letter):
        data = json.dumps(letter)
        res = requests.put("{}/services/letters/{}".format(self.base_url, letter_id), json=letter)
        return res
